import zipfile

to_zip = [
    'files/02_test_file.csv',
    'files/subfolder/01_test_file.txt'
]

def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist()
            if not f in lst:
                archive.write(f)
            else:
                print(f'File already exists in zip: {f}')

add_to_zip('work-with-files/files.zip', to_zip, 'a')