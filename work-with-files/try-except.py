# Try except helps to keep your program running without causing a crash 

acronyms = {
    'LOL': 'laugh out loud',
    'IDK': "i don't know"
}

# definition = acronyns['TBH'] -- # This will crash the code 
# print(definition) -- # This will crash the code


try:
    definition = acronyms['LOL'] 
    print('The definition is', definition)
except:
    print('This key does not exist')
finally:
    for acronym in acronyms:
        print(acronym)

print('The program keeps going..')