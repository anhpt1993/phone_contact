from module_delete import get_item
tag_ID = {
    1: "friend",
    2: "family",
    3: "co-worker",
    4: "others"
}

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

    print("Choose one or more tags of the following options:")
    for key, val in tag_ID.items():
        print(f"\t{key} : {val}")
    print("Your choice: ")
    item = get_item (tag_ID)
    print(f"\nAll contact with tag '{tag_ID[item]}':")
    for key, val in contact_list.items():
        if tag_ID[item] in contact_list[key]["tags"]:
            print(f"{key} : {val}")