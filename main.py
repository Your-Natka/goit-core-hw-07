from modul7.address_book import AddressBook
from modul7.record import Record
from utility import input_error

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message

@input_error
def show_all(_, book: AddressBook):
    if not book.data:
        return "No contacts in the address book."
    result = []
    for record in book.data.values():
        phones = ", ".join(phone.value for phone in record.phones)
        birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "No birthday"
        result.append(f"{record.name.value}: Phones: {phones}, Birthday: {birthday}")
    return "\n".join(result)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        raise KeyError("Birthday not found.")
    return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}."

@input_error
def birthdays(_, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join([f"{entry['name']} - {entry['birthday']}" for entry in upcoming])

def parse_input(user_input):
    parts = user_input.strip().split(" ")
    return parts[0], parts[1:]

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    commands = {
        "add": add_contact,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    }
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in commands:
            print(commands[command](args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()