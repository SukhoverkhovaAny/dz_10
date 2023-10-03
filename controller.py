import text
import view
from model import PhoneBook



def search_contact(book: PhoneBook, msg: str) -> dict[int, list[str]]:
    word = view.input_info(msg)
    result = book.search(word)
    view.show_contacts(result, text.search_word_error(word))
    return result


def start():
    pb = PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
            case '1':
                pb.open_file()
                view.print_message(text.open_successfull)
            case '2':
                pb.save_file()
                view.print_message(text.save_successfull)

            case '3':
                view.show_contacts(pb.phone_book, text.empty_phone_book_error)
            case '4':
                new_contact = view.input_new_contact(text.input_new_contact)
                pb.new_contact(new_contact)
                view.print_message(text.contact_info(new_contact[0], 0))
            case '5':
                search_contact(pb, text.input_search_word)
            case '6':
                if search_contact(pb, text.input_search_word_edit):
                    u_id = view.input_info(text.input_id_edit)
                    edit_contact = view.input_new_contact(text.input_edit_contact)
                    name = pb.edit(int(u_id), edit_contact)
                    view.print_message(text.contact_info(name, 1))
            case '7':
                if search_contact(pb, text.input_search_word_delete):
                    u_id = view.input_info(text.input_id_delete)
                    name = pb.delete(int(u_id))
                    view.print_message(text.contact_info(name, 2))
            case '8':
                view.print_message(text.good_bay)
                break