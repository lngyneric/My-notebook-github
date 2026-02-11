#!/usr/bin/env python3
"""
Inspect Source Viewer
"""

import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from browser_utils import BrowserFactory

def inspect_viewer(notebook_id: str):
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python auth_manager.py setup")
        return

    print(f"🔍 Inspecting source viewer for notebook: {notebook_id}")
    
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
        
        # Try different selectors for the Sources tab
        try:
            # 1. Exact text match (avoid tooltips)
            print("    Trying exact text match...")
            page.get_by_text("Sources", exact=True).first.click(timeout=2000)
        except:
            print("    Exact text match failed, trying by class/structure...")
            try:
                # 2. Look for tab/navigation item
                page.locator("mat-tab-header").get_by_text("Sources").click(timeout=2000)
            except:
                print("    Tab header failed, trying by button role...")
                # 3. Try button with name Sources
                page.get_by_role("button", name="Sources").first.click()
        
        page.wait_for_timeout(2000)
        
        # Find sources (look for file icons or names we saw earlier)
        # We saw 'Global Learning & Development Project (GLAD)_RHQ.pdf'
        source_name = "Global Learning & Development Project (GLAD)_RHQ.pdf"
        print(f"  🖱️  Clicking source: {source_name}")
        
        source_el = page.get_by_text(source_name).first
        if source_el.is_visible():
            source_el.click()
            page.wait_for_timeout(5000) # Wait for viewer
            
            print("  👀 Viewer opened. Inspecting content...")
            
            # Save viewer HTML
            with open("debug_viewer.html", "w", encoding="utf-8") as f:
                f.write(page.content())
            
            # Check for download buttons (often look like download icon or 'Original source')
            print("    Searching for buttons...")
            buttons = page.get_by_role("button").all()
            for i, btn in enumerate(buttons):
                try:
                    if btn.is_visible():
                        aria_label = btn.get_attribute("aria-label") or ""
                        text = btn.inner_text()
                        if "download" in aria_label.lower() or "download" in text.lower():
                            print(f"      [MATCH] Button {i}: Label='{aria_label}', Text='{text}'")
                        else:
                            # Print only if it looks interesting
                            if i < 20: # Limit output
                                print(f"      Button {i}: Label='{aria_label}', Text='{text}'")
                except: pass
                
            # Check for text content in the viewer
            # Often in a container with class 'source-viewer' or similar
            print("\n    Page text preview:")
            print(page.locator("body").inner_text()[:2000])
            
        else:
            print(f"  ❌ Source '{source_name}' not found")

    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        if context: context.close()
        if playwright: playwright.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect source viewer")
    parser.add_argument("notebook_id", help="Notebook ID")
    args = parser.parse_args()
    
    inspect_viewer(args.notebook_id)
