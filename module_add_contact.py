# Contacts:
#    - name
#    - phones (nhiều số điện thoại)
#    - emails (nhiều email)
#    - address
#    - note
#    - tags (nhiều tag --> dùng để phân nhóm: bạn bè, gia đình, công việc,..)

from module_delete import get_item

fields = [
    {
        "name": "name",
        "loop": False,
        "display_text": "+) Name: ",
        "data_validation": None
    },
    {
        "name": "phones",
        "loop": True,
        "display_text": "+) Phone number (Enter nothing to break): ",
        "data_validation": None
    },
    {
        "name": "emails",
        "loop": True,
        "display_text": "+) Email (Enter nothing to break): ",
        "data_validation": None
    },
    {
        "name": "address",
        "loop": False,
        "display_text": "+) Address: ",
        "data_validation": None
    },
    {
        "name": "note",
        "loop": False,
        "display_text": "+) Note: ",
        "data_validation": None
    },
    {
        "name": "tags",
        "loop": True,
        "display_text": "+) Tags (Enter nothing to break): ",
        "data_validation": {1: "friend", 2: "family", 3: "co-worker", 4: "others", 5: "press '5' to exit"}
    }
]
def add_personal_information():
    contact = {}
    for field in fields:
        if field["loop"]:
            value_list = []
            print(field["display_text"])
            if field["data_validation"] == None:
                while True:
                    value = input()
                    if value == "":
                        break
                    value_list.append(value)
            else:
                show_data_validation(field["data_validation"])
                print("Your choice: \t")
                while True:
                    value = get_item(field["data_validation"])
                    if value == 5:
                        break
                    value_list.append(field["data_validation"][value])

            contact.update({field["name"]: value_list})
        else:
            value = input(field["display_text"])
            contact.update({field["name"]: value})
    return contact

def show_data_validation(data_validation):
    print("Choose one of the followings:")
    for key, val in data_validation.items():
        print(f"{key}: {val}")

if __name__ == '__main__':
    print(add_personal_information())