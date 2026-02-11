
import sys

filename = "debug_notebook_0a8f255f-f2e3-40cd-858a-221268bdfe00.html"
try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"File {filename} not found")
    sys.exit(1)

print(f"Total length: {len(content)}")

# Check for title
if "<title>NotebookLM</title>" in content:
    print("✅ Page title matches")
else:
    print("⚠️ Page title might be different")

# Search for potential source containers
search_terms = ["source", "Source", "list-item", "mat-list-item"]

for term in search_terms:
    print(f"\n--- Searching for '{term}' ---")
    start = 0
    count = 0
    while count < 5:
        idx = content.find(term, start)
        if idx == -1:
            break
        
        count += 1
        print(f"Match {count} at {idx}")
        start_ctx = max(0, idx - 100)
        end_ctx = min(len(content), idx + 200)
        print(f"Context: ...{content[start_ctx:end_ctx]}...")
        
        start = idx + 1
