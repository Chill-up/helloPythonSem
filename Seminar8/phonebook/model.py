
path = "d:/Learn/GB/Разработчик/Python/Seminar/Seminar8/phonebook/base.txt"
contacts = []
added = 0

def read_file():
    global contacts
    with open(path, "r", encoding="UTF-8") as file:
        contacts = [i.strip().split(';') for i in file.readlines()]

def get_contacts():
    global contacts
    return contacts

def save_file():
    global contacts
    #contacts = "".join(map(str,contacts))

    return

def add_contacts():
    global contacts
    global added
    id = input(f'Введите id: ')
    name = input(f'Введите name: ')
    phone = input(f'Введите phone: ')
    comment = input(f'Введите comment: ')
    contacts.append(";".join([id,name,phone,comment]))
    added = added + 1