def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False
    
    try:
        with open("acronym.txt") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print("The acronym was not found")


def add_acronym():
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")
    with open("input.txt", "a") as file:
        file.write(acronym + " - " + definition + "\n")


def main():
    choice = input('Do you want to find (F) or add (A) an acroynm?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()