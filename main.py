import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from modul7.address_book import AddressBook
from modul7.record import Record
from utils import input_error

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return f"Contact {name} added/updated."

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday for {name} added."
    else:
        return f"Contact {name} not found."

@input_error
def show_birthday(args, book):
    name, = args
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}."
    return f"Birthday for {name} not found."

@input_error
def birthdays(_, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    return "\n".join([f"{entry['name']}: {entry['birthday']}" for entry in upcoming])

def parse_input(user_input):
    parts = user_input.split()
    return parts[0], parts[1:]

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    commands = {
        "add": add_contact,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    }

    while True:
        user_input = input("Enter a command: ")
        print(f"You entered: {user_input}") 
        command, args = parse_input(user_input)
        print(f"Command: {command}, Args: {args}")

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        handler = commands.get(command)
        if handler:
            print(handler(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()        
