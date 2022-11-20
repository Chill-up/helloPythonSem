


def show_menu():
    menu_text = '\nВведите необходимую команду:\n1 - Показать все контакты\
        \n2 - Открыть файл с контактами\
        \n3 - Записать файл с контактами\
        \n4 - Добавить контакт\
        \n5 - Изменить контакт\
        \n6 - Удалить контакт\
        \n7 - Поиск по контактам\
        \n0 - Выход\
        \n:'
    choice = input(menu_text)
    return choice

def show_contacts(contacts: list):
    if len(contacts) == 0:
        print("Нет контактов")
    else:
        [print(contact) for contact in contacts]
