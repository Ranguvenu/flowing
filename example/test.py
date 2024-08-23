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


# print("lower_bound:", lower_bound)
# print("lower_bound:", upper_bound)
# print(range(4, 7))
def find_upper_bound(numbers, given_number, margin):
    try:
        for i in range(len(numbers) - 1):
            if numbers[i] < given_number < numbers[i + 1]:
                if (numbers[i + 1] - given_number) >= margin:
                    return numbers[i + 1]
                else:
                    # If the difference is less than the margin, continue checking subsequent numbers
                    for j in range(i + 2, len(numbers)):
                        if (numbers[j] - given_number) >= margin:
                            return numbers[j]
                return None  # No suitable upper_bound found within the margin

        return None  # In case given_number is outside the range of the numbers
    except Exception as e:
        print(f"Error with finding upper bound: {e}")

# Example usage:
bounds = [50595.88, 50831.11, 51033.42, 51349.26, 51769.07, 52066.61]

print(find_upper_bound(bounds, 50555, 55))  # Expected output: 50831.11

