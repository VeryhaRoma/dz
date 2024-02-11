#завдання 1
def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                
                surname, salary = line.strip().split(',')
                
                total_salary += int(salary)
                num_developers += 1
        average_salary = total_salary / num_developers if num_developers > 0 else 0

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except ValueError:
        print("Неправильний формат даних у файлі.")
        return None, None

total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




#завдання 2
import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000 and 1 <= quantity <= maximum - minimum + 1):
        return []

    random_numbers = random.sample(range(minimum, maximum + 1), quantity)

    return sorted(random_numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)





#завдання 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def show_phone(contacts, args):
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return "Contact not found."

def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    return "Contact added."

def change_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts saved."

def main():
    contacts = {}
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
            if len(args) == 2:
                print(add_contact(contacts, args[0], args[1]))
            else:
                print("Invalid command.")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(contacts, args[0], args[1]))
            else:
                print("Invalid command.")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(contacts, args[0]))
            else:
                print("Invalid command.")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


