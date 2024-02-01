#завдання 1
from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        date_difference = current_date - input_date
        return date_difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

today = datetime.today().strftime("%Y-%m-%d")
result = get_days_from_today("2021-10-09")

print(f"Сьогодні {today}, різниця у днях: {result}")



#завдання 2
import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000 and 1 <= quantity <= maximum - minimum + 1):
        return []

    random_numbers = random.sample(range(minimum, maximum + 1), quantity)

    return sorted(random_numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)





#завдання 3
import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number.lstrip('38')

    return cleaned_number

phone_number1 = "    +38(050)123-32-34"
phone_number2 = "     0503451234"
phone_number3 = "(050)8889900"
phone_number4 = "38050-111-22-22"
phone_number5 = "38050 111 22 11   "

normalized_number1 = normalize_phone(phone_number1)
normalized_number2 = normalize_phone(phone_number2)
normalized_number3 = normalize_phone(phone_number3)
normalized_number4 = normalize_phone(phone_number4)
normalized_number5 = normalize_phone(phone_number5)

print("Нормалізовані номери:")
print(normalized_number1)
print(normalized_number2)
print(normalized_number3)
print(normalized_number4)
print(normalized_number5)

#завдання 4


from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days
        if days_until_birthday <= 7 and days_until_birthday >= 0:
            if birthday.weekday() == 5:  # Субота
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:  
                birthday += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John", "birthday": "1990.02.15"},
    {"name": "Alice", "birthday": "1992.01.05"},
    {"name": "Bob", "birthday": "1985.12.31"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Прийдешні дні народження для привітань:")
for birthday in upcoming_birthdays:
    print(f"{birthday['name']} - {birthday['congratulation_date']}")
