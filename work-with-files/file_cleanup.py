import os

folder_original = '../../PythonCourse/getting-started'
folder_destination = '../../PythonCourse/CleanedUp'

os.mkdir(folder_destination)

entries = os.scandir(folder_original)

for entry in entries:
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)















# for entry in entries:
#     if os.path.isfile(entry):
#         print('File:', entry.name)
#     elif os.path.isdir(entry):
#         print('Directory:', entry.name)

