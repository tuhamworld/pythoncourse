import zipfile

to_zip = ['files/01_file.csv',
          'files/02_file.csv',
          'files/subfolder/01_file_test.csv'
]


def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)


create_zip('work-with-files/files.zip', to_zip, 'w')