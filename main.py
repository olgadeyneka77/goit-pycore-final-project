import json
from models import AddressBook, NoteBook
from handlers import (
    parse_input, 
    add_contact, 
    change_contact,  
    show_phone,     
    add_birthday, 
    show_birthday, 
    birthdays,
    show_all_contacts,  
    add_note,           # Нові імпорти
    find_notes_by_tag,
    delete_contact,
    delete_note,
    edit_note,
    smart_search 
)

# --- Функції серіалізації даних ---

def save_data(address_book, note_book, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"contacts": address_book.to_dict(), "notes": note_book.to_dict()}, f, ensure_ascii=False, indent=2)

def load_data(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return AddressBook.from_dict(data["contacts"]), NoteBook.from_dict(data["notes"])
    except (FileNotFoundError, KeyError, ValueError):
        return AddressBook(), NoteBook()

# --- Головна функція ---

def main():
    book, notes = load_data()
    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                continue

            command, *args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break

                case "hello":
                    print("How can I help you?")

                case "add":
                    print(add_contact(args, book))

                case "change":
                    print(change_contact(args, book))

                case "phone":
                    print(show_phone(args, book))

                case "add-birthday":
                    print(add_birthday(args, book))

                case "show-birthday":
                    print(show_birthday(args, book))

                case "birthdays":
                    print(birthdays(args, book))

                case "all":
                    print(show_all_contacts(book))

                case "add-note":
                    print(add_note(args, notes))

                case "find-notes":
                    print(find_notes_by_tag(args, notes))

                case "delete-contact":
                    print(delete_contact(args, book))

                case "edit-note":
                    print(edit_note(args, notes))

                case "delete-note":
                    print(delete_note(args, notes))

                case cmd if cmd.startswith("#"):
                    print(smart_search(cmd, book, notes))

                case _:
                    print("Invalid command.")
    finally:
        save_data(book, notes)

if __name__ == "__main__":
    main()