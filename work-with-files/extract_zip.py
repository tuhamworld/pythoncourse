import zipfile

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)


# extract_file('work-with-files/files.zip', 'files/01_file.csv', 'work-with-files/extracted')
extract_all('work-with-files/files.zip', 'work-with-files/extracted')