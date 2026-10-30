import os
import shutil

# Path of the desktop folder
desktop_path = os.path.expanduser("~/Desktop")

# Dictionary containing the folder names and their corresponding file extension
folders =  {
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
    "Shortcut": [
        ".lnk"
    ],

    "Code": [
        ".html", ".css", ".json", ".xml",
        ".php", ".jsx", ".tsx", ".ts",
        ".sql", ".java", ".cpp", ".c"
    ]
}

# Create the subfolders if they dont exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(original_file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(original_file_path, destination_folder)
