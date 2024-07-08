from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = current_date - input_date
        return delta.days
    except ValueError:
        # Handle the exception for incorrect input format
        return "Invalid date format. Please use 'YYYY-MM-DD'."


input_date_str = '2025-10-09'
result = get_days_from_today(input_date_str)
print(f"Number of days between {input_date_str} and today: {result}")
