class PhoneBook:
    def __init__(self, path: str = 'phones.txt'):
        self.phone_book = {}
        self.path = path


    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for i, contact in enumerate(data, 1):
            contact = contact.strip().split(';')
            self.phone_book[i] = contact

    
    def save_file(self):
        contacts = []
        for contact in self.phone_book.values():
            contact = ';'.join(contact)
            contacts.append(contact)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(contacts))


    def new_id(self):
        return max(self.phone_book) + 1


    def new_contact(self, contact: list[str]):
        self.phone_book[self.new_id()] = contact


    def search(self, word: str) -> dict[int, list[str]]:
        result = {}
        for u_id, contact in self.phone_book.items():
            if word.lower() in ' '.join(contact).lower():
                result[u_id] = contact
        return result


    def edit(self, u_id: int, contact: list[str]) -> str:
        original_contact = self.phone_book.get(u_id)
        for i in range(len(contact)):
            contact[i] = contact[i] if contact[i] else original_contact[i]
        self.phone_book[u_id] = contact
        return contact[0]


    def delete(self, u_id: int)-> str:
        return self.phone_book.pop(u_id)[0]