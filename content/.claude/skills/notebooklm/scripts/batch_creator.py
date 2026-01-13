#!/usr/bin/env python3
"""
Batch Notebook Creator for NotebookLM
Automates the creation of notebooks via the web interface
"""

import sys
import time
import argparse
import re
from pathlib import Path
from typing import List, Dict, Any
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from browser_utils import BrowserFactory, StealthUtils
from notebook_manager import NotebookLibrary

class BatchCreator:
    def __init__(self, headless: bool = False):
        self.headless = headless
        self.auth = AuthManager()
        self.library = NotebookLibrary()

    def create_notebook(self, title: str) -> Dict[str, Any]:
        """Create a single notebook and return its details"""
        if not self.auth.is_authenticated():
            print("⚠️ Not authenticated")
            return None

        print(f"🔨 Creating notebook: {title}")
        
        playwright = None
        context = None

        try:
            playwright = sync_playwright().start()
            context = BrowserFactory.launch_persistent_context(
                playwright,
                headless=self.headless
            )
            page = context.new_page()
            
            # Go to dashboard
            print("  🌐 Opening dashboard...")
            page.goto("https://notebooklm.google.com/", wait_until="domcontentloaded")
            
            # Click "New Notebook"
            print("  🖱️  Clicking 'New Notebook'...")
            # Try different selectors for the new notebook button
            try:
                # 1. Try by text
                new_btn = page.get_by_text("New Notebook", exact=False).first
                if new_btn.is_visible():
                    new_btn.click()
                else:
                    # 2. Try by role
                    page.get_by_role("button", name="New Notebook").click()
            except Exception as e:
                print(f"  ❌ Could not find 'New Notebook' button: {e}")
                # Debug: print page content
                # print(page.content())
                return None

            # Wait for navigation to new notebook
            print("  ⏳ Waiting for notebook to load...")
            page.wait_for_url(re.compile(r"/notebook/"), timeout=20000)
            
            current_url = page.url
            notebook_id = current_url.split('/')[-1]
            print(f"  ✓ Created! ID: {notebook_id}")

            # Rename notebook
            print("  ✏️  Renaming...")
            try:
                # Usually the title is editable or there is an input
                # Strategy: Wait for title element, click it, type new name
                
                # Title selector varies, often in the top bar
                # Look for "Untitled notebook"
                title_el = page.get_by_text("Untitled notebook", exact=False).first
                if title_el:
                    title_el.click()
                    # It might turn into an input or be contenteditable
                    # Type the new title
                    page.keyboard.type(title)
                    page.keyboard.press("Enter")
                    print(f"  ✓ Renamed to '{title}'")
                else:
                    print("  ⚠️ Could not find title element to rename")
            except Exception as e:
                print(f"  ⚠️ Rename failed (non-critical): {e}")

            # Add to local library
            notebook_data = self.library.add_notebook(
                url=current_url,
                name=title,
                description=f"Auto-created notebook: {title}",
                topics=["General"]
            )
            
            print(f"  💾 Saved to local library")
            return notebook_data

        except Exception as e:
            print(f"  ❌ Error: {e}")
            return None
        finally:
            if context:
                context.close()
            if playwright:
                playwright.stop()

    def batch_create(self, titles: List[str]):
        """Create multiple notebooks"""
        print(f"🚀 Starting batch creation of {len(titles)} notebooks...")
        results = []
        
        for i, title in enumerate(titles):
            print(f"\n[{i+1}/{len(titles)}] Processing '{title}'...")
            result = self.create_notebook(title)
            if result:
                results.append(result)
            
            # Pause between creations to be safe
            if i < len(titles) - 1:
                print("  zzz Sleeping 5s...")
                time.sleep(5)
        
        print(f"\n✅ Batch complete! Created {len(results)}/{len(titles)} notebooks.")
        return results

def main():
    parser = argparse.ArgumentParser(description='Batch create NotebookLM notebooks')
    parser.add_argument('--titles', nargs='+', help='List of titles to create')
    parser.add_argument('--file', help='File containing titles (one per line)')
    parser.add_argument('--headless', action='store_true', help='Run headless')
    
    args = parser.parse_args()
    
    titles = []
    if args.titles:
        titles.extend(args.titles)
    
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                file_titles = [line.strip() for line in f if line.strip()]
                titles.extend(file_titles)
        except Exception as e:
            print(f"Error reading file: {e}")
            return

    if not titles:
        print("Please provide titles via --titles or --file")
        return

    creator = BatchCreator(headless=args.headless)
    creator.batch_create(titles)

if __name__ == "__main__":
    main()
