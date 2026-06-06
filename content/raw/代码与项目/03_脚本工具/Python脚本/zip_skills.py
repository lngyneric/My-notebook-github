import os
import shutil

def zip_folders():
    base_dir = r'C:\Users\lingyun\Downloads\skills-main\skills-main\skills'
    
    # Ensure the directory exists
    if not os.path.exists(base_dir):
        print(f"Error: Directory not found: {base_dir}")
        return

    # Get all subdirectories
    try:
        items = os.listdir(base_dir)
    except Exception as e:
        print(f"Error listing directory: {e}")
        return

    dirs = [d for d in items if os.path.isdir(os.path.join(base_dir, d))]

    for d in dirs:
        zip_filename = f"{d}.zip"
        zip_path = os.path.join(base_dir, zip_filename)
        dir_path = os.path.join(base_dir, d)

        if os.path.exists(zip_path):
            print(f"Skipping '{d}' - '{zip_filename}' already exists.")
        else:
            print(f"Zipping '{d}' to '{zip_filename}'...")
            try:
                # shutil.make_archive adds the extension automatically, so we pass the base name without extension
                # But wait, shutil.make_archive(base_name, format, root_dir)
                # base_name is the name of the file to create, including the path, minus any format-specific extension.
                # format is "zip"
                # root_dir is the directory that will be the root directory of the archive.
                
                output_filename = os.path.join(base_dir, d) # shutil will add .zip
                shutil.make_archive(output_filename, 'zip', dir_path)
                print(f"Successfully zipped '{d}'.")
            except Exception as e:
                print(f"Failed to zip '{d}': {e}")

if __name__ == "__main__":
    zip_folders()
