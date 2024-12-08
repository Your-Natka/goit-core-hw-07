import sys
from pathlib import Path

# Додати шлях до папки `models`
sys.path.append(str(Path(__file__).parent / "models"))
from commands import COMMANDS
from modul7.address_book import AddressBook 

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = user_input.split()
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in COMMANDS:
            print(COMMANDS[command](args, book))
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
