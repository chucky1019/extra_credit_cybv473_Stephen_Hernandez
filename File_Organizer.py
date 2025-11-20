import os

def File_orginizer():
    files = ["report.docx", "photo.jpg", "notes.txt", "image.png", "scripts.py"]

    # FIXED: use splitext, not split.text
    extensions = [os.path.splitext(f)[1] for f in files]

    organized = {
        ext: [f for f in files if os.path.splitext(f)[1] == ext]
        for ext in set(extensions)
    }

    print("Organizing files:")
    for i, (ext, grouped_files) in enumerate(organized.items(), start=1):
        print(f"{i}. {ext} -> {len(grouped_files)} files: {grouped_files}")


File_orginizer()
