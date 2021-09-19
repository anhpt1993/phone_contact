def is_name_in_contact(contact, name):
    if name.lower().strip() in contact["name"].lower().strip():
        return True
    else:
        return False

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
    name = input("Which name do you want to find out: ")
    print(f"\nAl contact with word '{name.strip()}' inside:\n")
    count = 0
    for key, val in contact_list.items():
        if is_name_in_contact(val, name):
            count += 1
            print(f'{key}: {val}')
    if count == 0:
        print("Nil")