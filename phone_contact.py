from module_add_contact import *
from module_delete import *
from module_update import *

def choose_option():
    while True:
        try:
            option = int(input("""
            Choose one of the following options:
            1. Add contact
            2. Delete contact
            3. Update contact
            4. Show all contacts
            5. Show all contacts same tags
            6. Quit
            
            => Your choice: """))

            if 1 <= option <= 6:
                return option
                break
            else:
                print("\nInvalid Value. Try again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try again!!!\n")

def try_again(text):
    answer = input(text)
    if answer == "Y" or answer == "YES":
        return True
    else:
        return False

if __name__ == '__main__':
    # contact_list = {
    #     1: {'name': 'Pham The Anh', 'phones': ['0123456789'], 'emails': ['anhpt@xxx'], 'address': 'Vung Tau',
    #         'note': '', 'tags': ['1', '2', '3']},
    #     2: {'name': 'Le Thi Nga', 'phones': ['0123456987'], 'emails': ['ngalt@xxx'], 'address': 'Vung Tau', 'note': '',
    #         'tags': ['1', '2']},
    #     3: {'name': 'Le Duc Manh', 'phones': ['0969996669'], 'emails': ['le.dm@xyz'], 'address': 'Binh Duong',
    #         'note': 'brother in law', 'tags': ['1', '3']},
    #     4: {'name': 'Nguyen Van B', 'phones': ['0669969996'], 'emails': ['b.nguyen@yahoo'], 'address': 'Ha Nam',
    #         'note': 'University', 'tags': ['1']}
    # }

    contact_list = {}
    while True:
        option = choose_option()
        if option == 1:
            if bool(contact_list):
                contact_list.update({max(contact_list.keys()) + 1: add_personal_information()})
            else:
                contact_list.update({1: add_personal_information()})
        elif option == 2:
            if bool(contact_list):
                print("\nWhich contact do you want to delete?".upper())
                del contact_list[get_item(contact_list)]
            else:
                print("\nNothing to delete!!!\n".upper())
        elif option == 3:
            if bool(contact_list):
                print("\nWhich contact do you want to update?".upper())
                key = get_item(contact_list)
                choice_list = list(contact_list[key].keys())
                choice = choose_info_to_revise(choice_list)
                if choice == "phones" or choice == "emails" or choice == "tags":
                    print(f"New values of {choice}: ", end=" ")
                    new_value = add_value_to_list()
                    contact_list[key][choice] = new_value
                else:
                    new_value = input(f"New value of {choice}: ")
                    contact_list[key][choice] = new_value
            else:
                print("\nNothing to change!!!\n".upper())
        elif option == 4:
            print("\nYour contact list:".upper())
            if bool(contact_list):
                for key, val in contact_list.items():
                    print(f"{key} : {val}")
            else:
                print("\nYou have to add contact first\n".upper())
        elif option == 5:
            pass
        else:
            exit()

