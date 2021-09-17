# Contacts:
#    - name
#    - phones (nhiều số điện thoại)
#    - emails (nhiều email)
#    - address
#    - note
#    - tags (nhiều tag --> dùng để phân nhóm: bạn bè, gia đình, công việc,..)

fields = [
    {
        "name": "name",
        "loop": False,
        "display_text": "+) Name: "
    },
    {
        "name": "phones",
        "loop": True,
        "display_text": "+) Phone number (Enter nothing to break): "
    },
    {
        "name": "emails",
        "loop": True,
        "display_text": "+) Email (Enter nothing to break): "
    },
    {
        "name": "address",
        "loop": False,
        "display_text": "+) Address: "
    },
    {
        "name": "note",
        "loop": False,
        "display_text": "+) Note: "
    },
    {
        "name": "tags",
        "loop": True,
        "display_text": "+) Tags (Choose one of the following options, enter nothing to break): "
    }
]
def add_personal_information():
    contact = {}
    for field in fields:
        if field["loop"]:
            value_list = []
            print(field["display_text"])
            while True:
                value = input()
                if value == "":
                    break
                value_list.append(value)
            contact.update({field["name"]: value_list})
        else:
            value = input(field["display_text"])
            contact.update({ field["name"]: value })
    return contact
def input_text(text):
    return input(text)

if __name__ == '__main__':
    print(add_personal_information())