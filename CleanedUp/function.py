# Creating function using local scope


def greeting(name):
    print("Hello", name)


input_name = input("Enter your name for welcome message: \n")
greeting(input_name)


# Creating function using global scope


def sayBye():
    print("Goodbye", yourname)


yourname = input("Enter your name to receive bye: \n")
sayBye()
