# Далее импортируем текст из файла .text в виде переменных для сокращения кода
from .text import *

# Функция по выводу меню с контролем ввода цифры от 1 до 8
def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 10:
            return int(choice)
        print(input_error)

# Украшательство месседжа
def print_message(message: str):
    print('\n' + '='*len(message) )
    print(message)

def show_contacts(book: list[dict[str,str]]):
    if book:
        for contact in book:
            print()
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{uid:>3}. {name:<20} {phone:<20} {comment:<20}')
    else:
        print(book_error)

def input_contact(message: str) -> dict[str,str]:
    print(message)
    name = input(new_conatct[0])
    phone = input(new_conatct[1])
    comment = input(new_conatct[2])
    return {'name': name, 'phone': phone, 'comment': comment}

def input_return(message: str) -> str:
    return input(message)

