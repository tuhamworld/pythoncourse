
import os
import shutil
from pathlib import Path

# Get the current user's Desktop directory
DESKTOP = Path.home() / "Desktop"
print('This is the desktop path', DESKTOP)

# Define file categories and their extensions
FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".svg", ".webp", ".ico", ".tiff"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".rtf", ".odt", ".xls", ".xlsx",
        ".ppt", ".pptx", ".csv"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2"
    ],

    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi",
        ".wmv", ".flv", ".webm"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac", ".ogg",
        ".flac", ".m4a"
    ],

    "Programs": [
        ".exe", ".msi", ".bat", ".cmd",
        ".py", ".js", ".jar", ".apk"
    ],

    "Code": [
        ".html", ".css", ".json", ".xml",
        ".php", ".jsx", ".tsx", ".ts",
        ".sql", ".java", ".cpp", ".c"
    ]
}


def get_category(extension):
    """Find the category for a file extension."""

    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category

    return "Others"


def organize_desktop():
    """Organize Desktop files into categorized folders."""

    if not DESKTOP.exists():
        print("Desktop folder was not found.")
        return

    moved_count = 0

    print("\nStarting Desktop organization...\n")

    # Only process files directly on the Desktop
    for file in DESKTOP.iterdir():

        if not file.is_file():
            continue

        category = get_category(file.suffix)

        # Create the destination folder
        destination_folder = DESKTOP / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file.name

        # Avoid overwriting files with the same name
        if destination.exists():
            name = file.stem
            extension = file.suffix
            counter = 1

            while destination.exists():
                destination = destination_folder / (
                    f"{name}_{counter}{extension}"
                )
                counter += 1

        try:
            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {category}/")
            moved_count += 1

        except Exception as error:
            print(f"Could not move {file.name}: {error}")

    print("\nOrganization completed!")
    print(f"Total files moved: {moved_count}")


if __name__ == "__main__":
    print("=" * 40)
    print("       DESKTOP FILE ORGANIZER")
    print("=" * 40)

    confirmation = input(
        "\nThis will organize files on your Desktop."
        "\nContinue? (y/n): "
    )

    if confirmation.lower() == "y":
        organize_desktop()
    else:
        print("Operation cancelled.")

    input("\nPress Enter to exit...")
