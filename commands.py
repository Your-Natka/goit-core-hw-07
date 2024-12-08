from decorators import input_error

@input_error
def add_contact(args, book):
    name, phone = args[0], args[1]
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
def change_contact(args, book):
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found.")
    record.change_phone(old_phone, new_phone)
    return "Phone number updated."

@input_error
def show_phones(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    phones = ", ".join(phone.value for phone in record.phones)
    return f"Phones for {name}: {phones}"

@input_error
def add_birthday(args, book):
    name, birthday = args[0], args[1]
    record = book.find(name)
    if not record:
        raise ValueError("Contact not found.")
    record.add_birthday(birthday)
    return f"Birthday {birthday} added for {name}."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        return "Contact or birthday not found."
    return f"Birthday for {name}: {record.birthday.value.strftime('%d.%m.%Y')}"

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    result = "Upcoming birthdays:\n"
    for entry in upcoming:
        result += f"{entry['name']}: {entry['birthday']}\n"
    return result.strip()

@input_error
def show_all(args, book):
    result = "All contacts:\n"
    for name, record in book.records.items():
        phones = ", ".join(phone.value for phone in record.phones)
        birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "Not set"
        result += f"{name}: Phones: {phones}, Birthday: {birthday}\n"
    return result.strip()

COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phones,
    "all": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
}
