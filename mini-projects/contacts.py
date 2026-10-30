contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
        {'name': 'Abdulhamid Sanusi', 'email': 'tuham@example.com'},
        {'name': 'Hermione Granger', 'email': 'hermione@example.com'},
        {'name': 'Ron Weasley', 'email': 'ron@example.com'}
    ]
}

print('Student emails')

for student in contacts['students']:
    print(student['email'])