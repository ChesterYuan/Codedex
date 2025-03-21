# Define menu items once, at the global level
MENU_ITEMS = {
    1: 'Cheeseburger',
    2: 'Fries',
    3: 'Soda',
    4: 'Ice Cream',
    5: 'Cookie'
}

def get_item(i):
    return MENU_ITEMS.get(i, 'invalid input')

def display_menu():
    print('Here is our menu:')
    for number, item in MENU_ITEMS.items():
        print(f'{number}. {item}')

def main():
    display_menu()
    try:
        option = int(input('What would you like to order? '))
        output = get_item(option)
        if output != 'invalid input':
            print(f'We will have {output} for you shortly')
        else:
            print('Sorry, that is not a valid menu option')
    except ValueError:
        print('Please enter a number')

# Run the program
main()
