import random


def get_numbers_ticket(min, max, quantity):
    try:
        if quantity > (max - min + 1):
            raise ValueError("Number of elements requested exceeds the range.")
        if min > max:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        if quantity <= 0 or min <= 0 or max <= 0:
            raise ValueError("All input parameters must be a positive integer.")

        numbers_set = random.sample(range(min, max + 1), quantity)
        return sorted(numbers_set)
    except ValueError as e:
        print(f"Error: {e}")


min = 1
max = 49
quantity = 6
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Lottery numbers: ", lottery_numbers)
