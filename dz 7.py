from datetime import datetime, timedelta

# Класи для валідації даних
class Field:
    pass

class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

# Клас запису контакту
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

# Клас адресної книги
class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def find(self, name):
        for record in self.records:
            if record.name == name:
                return record
        return None

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now()
        for record in self.records:
            if record.birthday is not None:
                if record.birthday.value.month == today.month:
                    if record.birthday.value.day >= today.day:
                        days_until_birthday = (record.birthday.value - today).days
                        if days_until_birthday <= 7:
                            upcoming_birthdays.append((record.name, days_until_birthday))
                elif record.birthday.value.month == (today.month % 12) + 1:  # Check for the next month
                    days_until_birthday = (record.birthday.value - today).days
                    if days_until_birthday <= 7:
                        upcoming_birthdays.append((record.name, days_until_birthday))
        return upcoming_birthdays

def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


def change_phone(args, book):
    name, new_phone = args
    record = book.find(name)
    if record:
        if record.phones:
            record.phones.pop()  # Змінюємо тільки перший номер
        record.add_phone(new_phone)
        return "Phone number changed."
    else:
        return "Contact not found."


def show_phone(args, book):
    name, = args
    record = book.find(name)
    if record:
        if record.phones:
            return record.phones[0]  # Повертаємо тільки перший номер
        else:
            return "Phone number not found."
    else:
        return "Contact not found."


def show_all_contacts(book):
    if book.records:
        return "\n".join([record.name for record in book.records])
    else:
        return "Address book is empty."

def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."


def show_birthday(args, book):
    name, = args
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday.value.strftime('%d.%m.%Y')
        else:
            return "Birthday not found."
    else:
        return "Contact not found."


def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        message = "Upcoming birthdays:\n"
        for name, days_until_birthday in upcoming_birthdays:
            message += f"{name}: {days_until_birthday} days\n"
        return message
    else:
        return "No upcoming birthdays."

# Функція парсингу введених команд
def parse_input(user_input):
    return user_input.split()

# Головна функція програми
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
