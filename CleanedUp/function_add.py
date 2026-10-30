def addition(a, b):
    return a + b

def main():
    num1 = int(input('Enter your 1st number: \n'))
    num2 = int(input('Enter your 2nd number: \n'))

    # Calling the function

    result = addition(num1, num2)
    print('The addition of', num1, 'and', num2, 'is', result)

main();