from db import *
import sys

def main_menu():
    menu_list = ('\tMENU', 'Dodaj nowy wpis', 'Pokaz wszystkie wpisy', 'Szukaj wpisu', 'zakończ',)
    while True:
        for index, item in enumerate(menu_list):
            if index == 0:
                print(item)
                continue
            print(f'{index}) - {item}.')
        print('#'*30)
        user_choice = int(input('Wybierz opcję wpisując numer z powyższej listy:'))
        if type(user_choice) is int and (0 < user_choice <= len(menu_list)):
            break
    if user_choice == 1:
        add_service()
    if user_choice == 2:
        [print(x) for x in show_all_records()]
    if user_choice == 3:
        search_service()
    if user_choice == 4:
        sys.exit()


def search_service()->None:
    web_site = input('Wpisz serwis który chcesz wyszukac:')
    user_login = input('Wpisz login który chcesz wyszukać:')
    show_selected_record(web_site, user_login)


def add_service() -> None:
    while True:
        print('Wpisz serwis : ')
        web_site = \
            input()
        if web_site == '':
            continue
        else:
            break

    while True:
        print(f'Wpisz login wykorzystywany w {web_site}: ')
        user_login = input()
        if user_login == '':
            continue
        else:
            break

    while True:
        print(f'Wpisz haslo dla {user_login}: ')
        user_pass = input()
        if user_pass == '':
            continue
        else:
            break

    insert_record(web_site, user_login, user_pass)


if __name__ == '__main__':
    main_menu()