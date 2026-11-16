import os, fnmatch

def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)


# match('./files', '*.csv')
# match('./files', '*.txt')
# match('./files', '*_file.csv')
# match('./files', '*1*_file.csv')
# match('./files', '*2*_file.csv')
# match('./files', '*2*_test.csv')
match('./files', '*2*.t*')