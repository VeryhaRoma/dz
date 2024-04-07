import pickle

class AddressBook:
    def __init__(self):
        self.contacts = []

    # Додати функціонал для додавання, зміни, видалення контактів та ін.

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    print("Welcome to the Address Book App!")

    while True:
        command = input("Enter a command (add, remove, show, save, exit): ")

        if command == "add":
            # Додати контакт
            pass
        elif command == "remove":
            # Видалити контакт
            pass
        elif command == "show":
            # Показати всі контакти
            pass
        elif command == "save":
            save_data(book)
            print("Data saved successfully!")
        elif command == "exit":
            save_data(book)
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
