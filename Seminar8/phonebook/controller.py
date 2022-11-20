import view as v
import model as m

def start():
    while True:
        command = v.show_menu()
        match command:
            case "1":
                v.show_contacts(m.get_contacts())
            case "2":
                m.read_file()
            case "3":
                m.save_file()
            case "4":
                m.add_contacts()
            case "0":
                break
