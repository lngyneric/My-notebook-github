#!/usr/bin/env python3
"""
List Remote Notebooks from NotebookLM Dashboard
"""

import sys
import time
import re
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from browser_utils import BrowserFactory

def list_remote_notebooks(headless: bool = True):
    """
    List all notebooks available in the NotebookLM dashboard
    """
    auth = AuthManager()

    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python auth_manager.py setup")
        return

    print("🔍 Scanning remote notebooks...")
    
    playwright = None
    context = None

    try:
        playwright = sync_playwright().start()
        
        # Launch persistent browser context
        context = BrowserFactory.launch_persistent_context(
            playwright,
            headless=headless
        )

        page = context.new_page()
        print("  🌐 Navigating to dashboard...")
        page.goto("https://notebooklm.google.com/", wait_until="domcontentloaded")
        
        # Debug info
        time.sleep(5) # Wait for redirects
        print(f"  📍 Current URL: {page.url}")
        print(f"  📄 Page Title: {page.title()}")

        # Check for login redirection
        if "accounts.google.com" in page.url:
             print("  ⚠️ Redirected to Google Login. Authentication might be expired.")
             return []

        # Wait for notebook list to load
        # Notebooks are usually in grid or list items. 
        # We'll look for elements that look like notebook cards.
        # Common selector might be 'a[href^="/notebook/"]' or similar.
        
        print("  ⏳ Waiting for notebook list...")
        
        # Debug: Print all links to see what we're working with
        all_links = page.query_selector_all('a')
        print(f"  🔍 Debug: Found {len(all_links)} total links on page")
        
        # Debug: Dump HTML to check structure
        with open("debug_dashboard.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("  💾 Saved page content to debug_dashboard.html")

        # Debug: Inspect specific known elements
        print("  🔍 Inspecting 'Our World in Data' element...")
        element = page.get_by_text("Our World in Data").first
        if element:
            try:
                print(f"    Found element: {element.evaluate('el => el.tagName')}")
                parent = element.locator("..")
                print(f"    Parent: {parent.evaluate('el => el.tagName')} class={parent.get_attribute('class')}")
                grandparent = parent.locator("..")
                print(f"    Grandparent: {grandparent.evaluate('el => el.tagName')} class={grandparent.get_attribute('class')}")
            except Exception as e:
                print(f"    Error inspecting element: {e}")

        try:
            # Try to wait for any project element
            # Look for elements with ID starting with 'project-' or class containing 'project-title'
            page.wait_for_selector('[id^="project-"], .project-title, .featured-project-title', timeout=5000)
        except:
            print("  ⚠️ Could not find notebook elements (timeout)")
            
            # Debug: Check for specific text indicating empty state or other errors
            content_text = page.locator("body").inner_text()
            if "Welcome to NotebookLM" in content_text:
                print("  ℹ️  Detected 'Welcome' page. You might not have any notebooks yet.")
            elif "Sign in" in content_text:
                print("  ⚠️ Detected 'Sign in' text. You might need to re-authenticate.")
            else:
                print("  ℹ️  Page content preview (first 200 chars):")
                print(f"  {content_text[:200].replace(chr(10), ' ')}...")

        # Extract notebook info
        # Strategy 1: Look for elements with id="project-UUID"
        project_elements = page.query_selector_all('[id^="project-"]')
        
        notebooks = []
        seen_ids = set()
        
        print(f"  ✓ Found {len(project_elements)} potential project elements")
        
        for el in project_elements:
            el_id = el.get_attribute('id')
            # ID format is usually "project-UUID" or "project-UUID-something"
            # e.g. "project-0d5cd576...-publisher"
            
            if not el_id:
                continue
                
            parts = el_id.split('-')
            if len(parts) < 2:
                continue
            
            # Extract UUID. It might be the second part, or more if it's mixed.
            # Usually project-UUID. UUID is 36 chars.
            # Let's try to find the UUID part.
            uuid_candidate = None
            for part in parts:
                if len(part) == 36: # Standard UUID length
                    uuid_candidate = part
                    break
            
            if not uuid_candidate:
                # Try to extract from string if it's like project-<uuid>
                match = re.search(r'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', el_id)
                if match:
                    uuid_candidate = match.group(1)
            
            if uuid_candidate and uuid_candidate not in seen_ids:
                seen_ids.add(uuid_candidate)
                
                # Try to find title
                # The element itself might be the title, or it might be near it.
                # Based on debug: <span class="project-button-title..." id="project-UUID-title">Title</span>
                title = ""
                
                # Check if this element is the title
                if "title" in el.get_attribute('class') or "name" in el.get_attribute('class'):
                    title = el.inner_text()
                else:
                    # Try to find a title element with this UUID
                    try:
                        title_el = page.query_selector(f'[id*="{uuid_candidate}"][class*="title"]')
                        if title_el:
                            title = title_el.inner_text()
                    except:
                        pass
                
                if not title:
                    title = f"Untitled ({uuid_candidate[:8]})"
                
                notebooks.append({
                    'title': title,
                    'url': f"https://notebooklm.google.com/notebook/{uuid_candidate}",
                    'id': uuid_candidate
                })

        # Strategy 2: If no IDs found, look for .project-title class
        if not notebooks:
             title_els = page.query_selector_all('.project-title, .featured-project-title')
             for el in title_els:
                 title = el.inner_text()
                 # We can't easily get ID if it's not in DOM, but we can list the title
                 notebooks.append({
                     'title': title,
                     'url': "Unknown URL",
                     'id': "unknown"
                 })

        # Print results
        print("\n📚 Remote Notebooks:")
        print("=" * 50)
        for nb in notebooks:
            print(f"Title: {nb['title']}")
            print(f"URL:   {nb['url']}")
            print(f"ID:    {nb['id']}")
            print("-" * 50)
        print(f"Total: {len(notebooks)}")
        
        return notebooks

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return []

    finally:
        if context:
            try:
                context.close()
            except:
                pass
        if playwright:
            try:
                playwright.stop()
            except:
                pass

if __name__ == "__main__":
    list_remote_notebooks()
