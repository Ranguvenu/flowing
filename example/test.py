from datetime import datetime, timedelta
import time

def find_bounds(numbers, given_number, margin):
    lower_bound = None
    upper_bound = None

    for i in range(len(numbers) - 1):
        if numbers[i] < given_number < numbers[i + 1]:

            for j in range(i + 1, len(numbers)):
                if (numbers[j] - given_number) > margin:
                    return numbers[i], numbers[j]
            return numbers[i], None  # In case no suitable upper_bound is found
    return upper_bound

bounds = [51884.68, 52229.11, 52589.62, 53023.84]
lower_bound, upper_bound = find_bounds(bounds, 52307.05, margin = 51)


print("lower_bound:", lower_bound)
print("lower_bound:", upper_bound)
# print(range(4, 7))
