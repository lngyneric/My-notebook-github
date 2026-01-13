#!/usr/bin/env python3
"""
Download NotebookLM Sources
Iterates through all sources in a notebook and saves their content to local files.
"""

import sys
import time
import argparse
import re
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from browser_utils import BrowserFactory

def sanitize_filename(name):
    """Sanitize filename to be safe for file system."""
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def download_sources(notebook_id: str, output_dir: str = "downloads"):
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python auth_manager.py setup")
        return

    # Create output directory
    out_path = Path(output_dir)
    out_path.mkdir(exist_ok=True)
    
    print(f"🔍 Downloading sources for notebook: {notebook_id}")
    print(f"📂 Output directory: {out_path.absolute()}")
    
    playwright = None
    context = None

    try:
        playwright = sync_playwright().start()
        context = BrowserFactory.launch_persistent_context(playwright, headless=True)
        page = context.new_page()
        
        url = f"https://notebooklm.google.com/notebook/{notebook_id}"
        print(f"  🌐 Navigating to {url}...")
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)
        
        # Open Sources tab
        print("  📂 Opening Sources tab...")
        try:
            page.get_by_text("Sources", exact=True).first.click(timeout=3000)
        except:
            print("    Retrying Sources tab click...")
            page.locator("mat-tab-header").get_by_text("Sources").click()
            
        page.wait_for_timeout(2000)
        
        # Find all source elements
        # Based on previous inspection, sources are likely list items or have checkboxes
        # We can find them by looking for the known source names or iterating through list items
        
        # Let's collect source names first
        source_names = []
        
        # Strategy: Look for checkboxes and get their parent text
        checkboxes = page.get_by_role("checkbox").all()
        
        # Skip the first checkbox if it's "Select all" (usually has aria-label or just first one)
        # But we saw 6 checkboxes for 5 sources + 1 select all.
        # Let's check the count.
        print(f"    Found {len(checkboxes)} checkboxes")
        
        potential_sources = []
        
        for i, cb in enumerate(checkboxes):
            # Get the container of the checkbox
            # The structure is likely: list-item > checkbox
            # We want the text sibling of the checkbox
            
            # Try to get the text from the row
            try:
                # Go up to the row/list-item
                # Assuming checkbox is inside the row
                row = cb.locator("xpath=./ancestor::*[contains(@class, 'mat-mdc-list-item') or contains(@class, 'source-item')]").first
                if not row.count():
                     # Fallback: parent of parent
                     row = cb.locator("..").locator("..")
                
                text = row.inner_text()
                # Clean up text (remove newlines, "Select all", etc.)
                clean_text = text.replace('\n', ' ').strip()
                
                # Filter out "Select all"
                if "Select all" in clean_text or not clean_text:
                    continue
                    
                # The text might contain "PDF", "Markdown", etc. We want the name.
                # Usually the name is the most prominent text.
                # Let's just use the whole text for now and sanitize later, or try to extract the name.
                
                # If we have specific names we know, we can match.
                # But we want to be generic.
                
                # Let's extract the first line or the part before the type (PDF/Markdown)
                lines = text.split('\n')
                name = lines[0].strip()
                if not name and len(lines) > 1:
                    name = lines[1].strip()
                    
                if name and name not in source_names:
                    source_names.append(name)
                    potential_sources.append(name)
                    print(f"    Found source: {name}")
            except Exception as e:
                print(f"    Error extracting source name for checkbox {i}: {e}")

        # If we couldn't find names via checkboxes, try the hardcoded list for this specific task
        if not potential_sources:
            print("    ⚠️ Could not auto-detect source names. Using known list.")
            potential_sources = [
                "Global Learning & Development Project (GLAD)_RHQ.pdf",
                "SCHHR-EN1.pdf",
                "SCH企业培训现状汇报",
                "全球学习与发展项目启动",
                "致Kaka：关于培训合作与预算"
            ]

        print(f"  📋 Processing {len(potential_sources)} sources...")
        
        for name in potential_sources:
            print(f"\n  ⬇️  Downloading: {name}")
            try:
                # Click the source
                # Use exact=True if possible, but some names might be truncated
                # Using get_by_text without exact=True might match parts
                el = page.get_by_text(name).first
                if not el.is_visible():
                    print(f"    ⚠️ Element not visible, scrolling...")
                    el.scroll_into_view_if_needed()
                
                el.click()
                
                # Wait for viewer
                # Look for "Back" button or the title in the viewer
                page.wait_for_timeout(3000)
                
                # Check if viewer is open (Back button visible)
                back_btn = page.get_by_role("button", name="Back").first
                if not back_btn.is_visible():
                    # Maybe it's "arrow_back" icon
                    back_btn = page.get_by_text("arrow_back").first
                
                if back_btn.is_visible():
                    print("    ✅ Viewer opened")
                    
                    # Extract content
                    # We want the main content.
                    # Usually in a scrollable container.
                    # Let's get the full body text and try to filter out the UI.
                    
                    # Better: Get the container that holds the text.
                    # Based on previous dump, the text starts after "Source guide" or the title.
                    
                    content = page.locator("body").inner_text()
                    
                    # Save to file
                    safe_name = sanitize_filename(name)
                    if not safe_name.endswith(('.txt', '.md', '.pdf')):
                        safe_name += ".txt"
                        
                    file_path = out_path / safe_name
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                        
                    print(f"    💾 Saved to: {file_path}")
                    
                    # Close viewer
                    print("    🔙 Closing viewer...")
                    back_btn.click()
                    page.wait_for_timeout(2000)
                    
                else:
                    print("    ❌ Viewer did not open")
                    
            except Exception as e:
                print(f"    ❌ Error processing {name}: {e}")
                # Try to recover: click Back if visible
                try:
                    page.get_by_role("button", name="Back").click(timeout=2000)
                except: pass

    except Exception as e:
        print(f"  ❌ Fatal Error: {e}")
    finally:
        if context: context.close()
        if playwright: playwright.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download notebook sources")
    parser.add_argument("notebook_id", help="Notebook ID")
    parser.add_argument("--output", "-o", default="downloads", help="Output directory")
    args = parser.parse_args()
    
    download_sources(args.notebook_id, args.output)
