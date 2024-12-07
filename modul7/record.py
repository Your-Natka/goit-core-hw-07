from modul7.fields import Name, Phone, Birthday

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone: str, new_phone: str):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Phone not found")

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)
