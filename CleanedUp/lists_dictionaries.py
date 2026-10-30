menus = {
    'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
    'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
    'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']
}


# for menu in menus:
#     print(menu)


for name, menu in menus.items():
    print(name, ':', menu)