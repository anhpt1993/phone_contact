def get_item(contact_list):
    while True:
        try:
            key = int(input("Enter the serial number: "))
            if check_key(contact_list, key):
                return key
                break
            else:
                print(f"\nS/N {key} is not in contact list\n")
        except ValueError:
            print("\nInvalid Input. Try Again!!!\n")
            
def check_key(contact_list, key):
    if key in contact_list.keys():
        return True
    else:
        return False

if __name__ == '__main__':
    contact_list = {
        1: {'name': 'The Anh', 'phones': ['0123456789'], 'emails': ['anhpt@xxx'], 'address': 'Vung Tau', 'note': '',
            'tags': ['1', '2', '3']},
        2: {'name': 'Le Thi Nga', 'phones': ['0123456987'], 'emails': ['ngalt@xxx'], 'address': 'Vung Tau', 'note': '',
            'tags': ['1', '2']}
    }

    print("\nWhich contact do you want to delete?".upper())
    del contact_list[get_item(contact_list)]
    print(f"New contact list: \n{contact_list}")
