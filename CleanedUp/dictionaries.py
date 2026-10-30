acronyms = {
    'LOL': 'laugh out loud',
    'IDK': 'i dont know',
    'TBH': 'to be honest'
}

acronyms['SMH'] = 'shaking my head'

print('Original list: ', acronyms)

# Updating a value
acronyms['LOL'] = 'laughing out loud'

print('Printing updated values', acronyms)

# Deleting a value

del acronyms['LOL']

print('Deleted LOL from the list: ', acronyms)

# Getting a key thats not there by accessing directly would crash the program. best way to do it is using get

definition = acronyms.get('WDYM') # if NOT exist, means false

if (definition):
    print(definition)
else:
    print('Key does not exist')



sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence: ', sentence)
print('translation: ', translation)