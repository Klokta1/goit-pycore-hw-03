from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # today = datetime.today().date()
    today = datetime.strptime("2024.01.22", "%Y.%m.%d").date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=today.year)

        # Check next year if birthday is already passed
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days
        if days_until_birthday <= 7:
            if birthday.weekday() == 5:  # saturday
                days_until_birthday += 2
            if birthday.weekday() == 6:  # sunday
                days_until_birthday += 1
            congratulation_date = today + timedelta(days=days_until_birthday)
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Upcoming birthdays:", upcoming_birthdays)
