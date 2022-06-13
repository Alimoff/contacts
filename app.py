import main

MENU_PROMPT = """_-_-_- WELCOME -_-_-_
Choose an option:

1) Add contact.
2) Show all contacts.
3) Delete contact.
4) Update existing contact..
5) Exit.


Your select:"""


def menu():
    while (user_input := int(input(MENU_PROMPT))) != 5:
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input")
            continue
        if user_input == 1:
            main.add_contact()
        elif user_input == 2:
            main.show_all()
        elif user_input == 3:
            main.delete_contact()
        elif user_input == 4:
            main.update_contacts()
        else:
            print("Invalid input!")


menu()
