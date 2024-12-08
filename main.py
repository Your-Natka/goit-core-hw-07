from modul7.address_book import AddressBook
from modul7.record import Record
from utility import input_error
from datetime import datetime, timedelta

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
    if not book.records:  # Перевіряємо, чи є контакти в книзі
        return "No contacts in the address book."
    
    result = []  # Збираємо інформацію про всі контакти
    for record in book.records.values():  # Використовуємо self.records, а не self.data
        phones = ", ".join(phone.value for phone in record.phones)
        birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "No birthday"
        result.append(f"{record.name.value}: Phones: {phones}, Birthday: {birthday}")
    
    return "\n".join(result)

@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        return "Error: You must provide a contact name."

    name = args[0]

    # Знаходимо контакт
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."

    # Отримуємо телефони
    phones = ", ".join(phone.value for phone in record.phones)
    return f"{name}: Phones: {phones}" if phones else f"{name} has no phones."

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
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    result = []

    # Якщо вказано ім'я, шукаємо лише для конкретного контакту
    if args:
        name = args[0]
        record = book.find(name)
        if not record:
            return f"Contact {name} not found."
        records = [record]
    else:
        # Інакше перевіряємо всі записи
        records = book.records.values()

    for record in records:
        if record.birthday:
            # Отримуємо дату народження як рядок
            day, month, year = map(int, record.birthday.value.split("."))
            birthday_this_year = datetime(year=today.year, month=month, day=day).date()

            # Якщо день народження виходить на вихідні, переносимо на понеділок
            if birthday_this_year.weekday() == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                birthday_this_year += timedelta(days=1)

            # Перевіряємо, чи день народження в межах наступного тижня
            if today <= birthday_this_year <= next_week:
                result.append(f"{record.name.value} - {birthday_this_year.strftime('%d.%m.%Y')}")

    return "\n".join(result) if result else "No birthdays in the next week."

def birthdays(_, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join([f"{entry['name']} - {entry['birthday']}" for entry in upcoming])

def parse_input(user_input):
    parts = user_input.strip().split(" ")
    return parts[0], parts[1:]

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args

    # Знаходимо контакт
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."

    # Шукаємо старий телефон
    for phone in record.phones:
        if phone.value == old_phone:
            phone.value = new_phone  # Змінюємо телефон
            return f"Phone number for {name} updated from {old_phone} to {new_phone}."
    
    return f"Phone number {old_phone} not found for contact {name}."

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    commands = {
        "add": add_contact,
        "change": change_contact,
        "all": show_all,
        "phone": show_phone,
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