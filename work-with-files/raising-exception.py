def remainder_division(a, b):
    if b == 0:
        raise Exception('Divisor cannot be by 0')
    result = a // b
    remainder = a % b
    print(a, '/', b, 'is', result,
          ':remainder', remainder)

        
# Main program
remainder_division(10, 0)