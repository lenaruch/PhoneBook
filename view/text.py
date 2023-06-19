''' Для перевода на другой язык, достаточно перевести значения в данном файле'''

main_menu = '''Главное меню 
1. Открыть файл  | 2. Сохранить файл  | 3. Показать все контакты  | 4. Создать новый контакт  | 5. Найти контакт  | 6. Изменить контакт  | 7. Удалить контакт  | 8. Выход'''
menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод. Введите число от 1 до 8: '
book_error = 'Телефонная книга пуста или файл не открыт'
open_succesful = 'Телефонная книга открыта. Что с ней будем делать дальше?'
show_succesful = 'Вот все контакты. Что будем делать дальше?'
input_new = 'Введите данные нового контакта'
# input_change = 'Введите данные изменяемого контакта'
new_conatct = ['Введите имя контакта: ', 'Введите номер телефона: ', 'Введите комментарий: ']
search_word = 'Введите искомы элемент: '
input_index = 'Введиете индекс изменяемого контакта: '
input_change_contact = 'Введите данные изменяемого контакта или Enter? чтобы оставть без изменений: '

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранен'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'