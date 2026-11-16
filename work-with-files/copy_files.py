import shutil

def copy_files(src, dst):
    shutil.copy(src, dst)
    print(f'Files copied from {src} to {dst}')

def copy_folder(src, dst):
    shutil.copytree(src, dst)
    print(f'Folder copied from {src} to dst')


# copy_files('./files/02_file.txt', './files/subfolder')
copy_folder('./files', './files/new_folder')