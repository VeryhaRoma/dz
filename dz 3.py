#завдання 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))  




#завдання 2
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'  
    for match in re.finditer(pattern, text):
        yield float(match.group()) 

def sum_profit(text: str, func: Callable):
    total = sum(func(text)) 
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



#завдання 4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide name and phone."
        except IndexError:
            return "Invalid input. Please provide name and phone."

    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def show_all_contacts():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def handle_command(command):
    parts = command.split()
    if parts[0] == "add":
        result = add_contact(parts[1:])
    elif parts[0] == "phone":
        result = show_phone(parts[1:])
    elif parts[0] == "all":
        result = show_all_contacts()
    else:
        result = "Invalid command."
    return result

while True:
    command = input("Enter a command: ")
    print(handle_command(command))
