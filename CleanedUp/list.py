# Creating lists and appending an item

acronyms = []
acronyms.append("LOL")
acronyms.append("IDK")
# print(acronyms)


# Removing item from a list

new_acronyms = ['LOL', 'IDK', 'SMH', 'TBH', 'LMAO']
new_acronyms.append('IMHO')
print('printing original new acronyms list.. \n')
print(new_acronyms)
print('removing LMAO.. \n')
new_acronyms.remove('LMAO') #removing value
print(new_acronyms)
print('removing SMH.. \n')
del new_acronyms [2] # alternati
print('printing updated new acronyms list..')
print(new_acronyms)

# Checking if an item exists in a list

word = 'TBH'
if word in new_acronyms:
    print(word + ' is in the list \n')
else:
    print(word + ' is NOT in the list \n')


# Looping in list

print('printing each acronym per line..')
for acronym in new_acronyms:
    print(acronym)