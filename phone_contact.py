from module_add_contact import *
from module_delete import *
from module_update import *
from module_show_contact_by_tag import *
from module_search_by_name import *

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
            6. Search by name
            7. Quit
            
            => Your choice: """))

            if 1 <= option <= 7:
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
    contact_list = {
        1: {'name': 'Pham The Anh', 'phones': ['0123456789'], 'emails': ['anhpt@xxx'], 'address': 'Vung Tau',
            'note': '', 'tags': ["friend", "family", "co-worker"]},
        2: {'name': 'Le Thi Nga', 'phones': ['0123456987'], 'emails': ['ngalt@xxx'], 'address': 'Vung Tau', 'note': '',
            'tags': ["friend", "family"]},
        3: {'name': 'Le Duc Manh', 'phones': ['0969996669'], 'emails': ['le.dm@xyz'], 'address': 'Binh Duong',
            'note': 'brother in law', 'tags': ["friend", "co-worker"]},
        4: {'name': 'Nguyen Van B', 'phones': ['0669969996'], 'emails': ['b.nguyen@yahoo'], 'address': 'Ha Nam',
            'note': 'University', 'tags': ["others"]}
    }

    # contact_list = {}
    while True:
        option = choose_option()
        if option == 1:
            if bool(contact_list):
                contact_list.update({max(contact_list.keys()) + 1: add_personal_information()})
            else:
                contact_list.update({1: add_personal_information()})
        elif option == 7:
            exit()
        else:
            if bool(contact_list) == False:
                print("\nEmpty contact. You have to add contact first\n".upper())
            else:
                if option == 2:
                    print("\nWhich contact do you want to delete?".upper())
                    print("Enter serial number to delete: \t")
                    del contact_list[get_item(contact_list)]
                elif option == 3:
                    print("\nWhich contact do you want to update?".upper())
                    print("Enter serial number to update: \t")
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
                elif option == 4:
                    print("\nYour contact list:".upper())
                    for key, val in contact_list.items():
                        print(f"{key} : {val}")
                elif option == 5:
                    print("Choose one tag of the following options:")
                    for key, val in tag_ID.items():
                        print(f"\t{key} : {val}")
                    print("Enter serial number corresponding to tag: \t")
                    item = get_item(tag_ID)
                    print(f"\nAll contact with tag '{tag_ID[item]}':")
                    for key, val in contact_list.items():
                        if tag_ID[item] in contact_list[key]["tags"]:
                            print(f"{key} : {val}")
                elif option == 6:
                    name = input("Which name do you want to find out: ")
                    print(f"\nAl contact with word '{name.strip()}' inside:\n")
                    count = 0
                    for key, val in contact_list.items():
                        if is_name_in_contact(val, name):
                            count += 1
                            print(f'{key}: {val}')
                    if count == 0:
                        print("Nil")