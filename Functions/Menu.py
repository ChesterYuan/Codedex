def get_item(i):
    menu_items = {
        1: 'Cheeseburger',
        2: 'Fries',
        3: 'Soda',
        4: 'Ice Cream',
        5: 'Cookie'
    }
    return menu_items.get(i, 'invalid input')

def display_menu():
    print('Here is our menu:')
    menu_items = [
        '1. Cheeseburger',
        '2. Fries',
        '3. Soda',
        '4. Ice Cream',
        '5. Cookie'
    ]
    for item in menu_items:
        print(item)

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
