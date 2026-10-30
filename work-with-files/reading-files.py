with open('input.txt') as file:
    result = file.read()
    print(result)

print ('\n Using readline to print the next one in line....\n')

with open('input.txt') as file:
    result = file.readline()
    print(result)

    result = file.readline()
    print(result)


print('\n all text in each line using loop')

with open('input.txt') as file:
    for line in file:
        print(line)