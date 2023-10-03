import text

def main_menu() -> str:
    print(text.main_menu[0])
    for i, item in enumerate(text.main_menu[1:], 1):
        print(f'\t{i}. {item}')
    while True:
        choice = input(text.user_coice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return choice
        print(text.user_choice_error)


def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) +'\n')


def show_contacts(book: dict, msg: str):
    if book:
        print('\n' + '=' * 68)
        for u_id, contact in book.items():
            print(f'{u_id:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
        print('=' * 68 +'\n')
    else:
        print_message(msg)


def input_new_contact(msg: list) -> list[str]:
    contact = []
    for in_text in msg:
        contact.append(input(in_text))
    return contact


def input_info(msg: str) -> str:
    return input(msg)