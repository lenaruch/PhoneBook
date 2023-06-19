from view import menu, show_contacts, print_message, input_contact, input_return
import model
from view import text


def start():
    while True:
        choice = menu()
        match choice:
            case 1:  # Открыть файл
                model.open_file()
                print_message(text.open_succesful)
            case 2:  # Сохранить файл
                pass
            case 3:  # Показать все контакты
                show_contacts(model.phone_book)
                print_message(text.show_succesful)
            case 4:  # Создать новый контакт
                new = input_contact(text.input_new)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:  # Найти контакт
                word = input_return(text.search_word)
                result = model.saerch(word)
                show_contacts(result)
            case 6:  # Изменить контакт
                word = input_return(text.search_word)
                result = model.saerch(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index)-1].get('name')
                print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))
            case 7:  # Удалить контакт
                pass
            case 8:  # Выход
                break  # Выход из цикла while True через функцию break
