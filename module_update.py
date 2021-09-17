from module_delete import get_item

def choose_info_to_revise(array):
    while True:
        try:
            print("Choose one of the following options: ")
            for i in range(len(array)):
                print(f"{i+1} : {array[i]}")
            option = int(input("\n=> Your choice: """))
            if 1 <= option <= len(array):
                return array[option-1]
                break
            else:
                print("\nInvalid Value. Try Again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")

def add_value_to_list():
        lst = []
        while True:
            value = input()
            if value == "":
                return lst
                break
            else:
                lst.append(value)

if __name__ == '__main__':
    contact_list = {
        1: {'name': 'Pham The Anh', 'phones': ['0123456789'], 'emails': ['anhpt@xxx'], 'address': 'Vung Tau',
            'note': '', 'tags': ['1', '2', '3']},
        2: {'name': 'Le Thi Nga', 'phones': ['0123456987'], 'emails': ['ngalt@xxx'], 'address': 'Vung Tau', 'note': '',
            'tags': ['1', '2']},
        3: {'name': 'Le Duc Manh', 'phones': ['0969996669'], 'emails': ['le.dm@xyz'], 'address': 'Binh Duong',
            'note': 'brother in law', 'tags': ['1', '3']},
        4: {'name': 'Nguyen Van B', 'phones': ['0669969996'], 'emails': ['b.nguyen@yahoo'], 'address': 'Ha Nam',
            'note': 'University', 'tags': ['1']}
    }
    print("\nWhich contact do you want to update?".upper())
    key = get_item(contact_list)
    choice_list = list(contact_list[key].keys())
    choice = choose_info_to_revise(choice_list)
    if choice == "phones" or choice == "emails" or choice == "tags":
        print(f"New values of {choice}: ", end = " ")
        new_value = add_value_to_list()
        contact_list[key][choice] = new_value
    else:
        new_value = input(f"New value of {choice}: ")
        contact_list[key][choice] = new_value

    print(contact_list)

