age = int(input("How old are you? \n"))
decades = age//10       #the double slashes gives whole number
years = age % 10        #module gives the remainder
print("You are " + str(decades) + " decades and " + str(years) + " years old.")