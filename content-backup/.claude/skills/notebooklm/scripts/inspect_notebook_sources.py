#!/usr/bin/env python3
"""
Inspect Notebook Sources
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

def inspect_sources(notebook_id: str):
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python auth_manager.py setup")
        return

    print(f"🔍 Inspecting sources for notebook: {notebook_id}")
    
    playwright = None
    context = None

    try:
        playwright = sync_playwright().start()
        context = BrowserFactory.launch_persistent_context(playwright, headless=True)
        page = context.new_page()
        
        url = f"https://notebooklm.google.com/notebook/{notebook_id}"
        print(f"  🌐 Navigating to {url}...")
        page.goto(url, wait_until="domcontentloaded")
        
        print("  ⏳ Waiting for page to load...")
        page.wait_for_timeout(5000) # Wait for dynamic content
        
        # Save HTML for inspection
        debug_file = f"debug_notebook_{notebook_id}.html"
        # with open(debug_file, "w", encoding="utf-8") as f:
        #     f.write(page.content())
        # print(f"  💾 Saved HTML to {debug_file}")
        
        # Print visible text
        print("  📄 Page Text Content:")
        text = page.locator("body").inner_text()
        print(text[:2000]) # Print first 2000 chars
        
        # Try to find "Sources" or "docs"
        print("\n  🔍 Interaction test...")
        
        # Try to click the "Sources" tab
        sources_tab = page.get_by_text("Sources").first
        if sources_tab.is_visible():
            print("    Found 'Sources' tab, clicking...")
            sources_tab.click()
            page.wait_for_timeout(3000)
        else:
            print("    'Sources' tab not found")
            
        # Print text again to see if list expanded
        print("\n  📄 Page Text Content (After interaction):")
        text = page.locator("body").inner_text()
        print(text[:2000])
        
        # Look for checkboxes which usually accompany sources
        checkboxes = page.get_by_role("checkbox").all()
        print(f"\n    Found {len(checkboxes)} checkboxes")
        
        # If we find checkboxes, their labels are likely the source names
        for i, cb in enumerate(checkboxes):
            # Try to get the label or parent text
            try:
                # Get parent text
                parent = cb.locator("..")
                print(f"      [{i}] Checkbox Parent Text: {parent.inner_text()[:50]}")
            except: pass


    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        if context: context.close()
        if playwright: playwright.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect notebook sources")
    parser.add_argument("notebook_id", help="Notebook ID")
    args = parser.parse_args()
    
    inspect_sources(args.notebook_id)
