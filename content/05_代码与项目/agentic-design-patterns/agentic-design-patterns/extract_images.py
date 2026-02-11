import re
import base64
import os
import sys

# Force stdout flush
sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content\agentic-design-patterns\17-Chapter-11-Goal-Setting-And-Monitoring.md"
images_dir = r"c:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content\agentic-design-patterns\images"

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

print(f"Reading file: {file_path}")
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Read {len(content)} characters.")
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Check for existence of markers
if "[image1]:" in content:
    print("Found [image1]: marker")
else:
    print("Did NOT find [image1]: marker")

# Pattern to find base64 images
pattern = re.compile(r'\[(image\d+)\]:\s*<data:image/png;base64,([^>]+)>')

matches = pattern.findall(content)
print(f"Found {len(matches)} matches via regex.")

for img_id, b64_data in matches:
    img_filename = ""
    if img_id == "image1":
        img_filename = "chapter11_fig1.png"
    elif img_id == "image2":
        img_filename = "chapter11_fig2.png"
    else:
        continue
    
    save_path = os.path.join(images_dir, img_filename)
    try:
        # Remove newlines/spaces from base64 data just in case
        b64_data_clean = b64_data.replace('\n', '').replace(' ', '')
        img_data = base64.b64decode(b64_data_clean)
        with open(save_path, 'wb') as f_img:
            f_img.write(img_data)
        print(f"Saved {save_path} ({len(img_data)} bytes)")
    except Exception as e:
        print(f"Error saving {save_path}: {e}")

if len(matches) > 0:
    print("Updating file content...")
    new_content = content
    new_content = new_content.replace('![][image1]', '![Goal Setting and Monitor example](images/chapter11_fig1.png)')
    new_content = new_content.replace('![][image2]', '![Goal design patterns](images/chapter11_fig2.png)')
    
    # Remove the definition lines
    new_content = pattern.sub('', new_content)
    new_content = new_content.strip() + '\n'
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated markdown file successfully.")
    except Exception as e:
        print(f"Error writing file: {e}")
else:
    print("No matches found, file not updated.")
