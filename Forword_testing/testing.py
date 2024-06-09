# from optionslib import *
ss = {'token': '37095', 'price': 2790.0, 'optionname': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}

def sell_at(current_index_at):
    support_resistances = [50055.05, 49918.73, 49593.87, 49257.89, 48951.64]
    next_greater = None
    second_next_greater = None

    for resistance in support_resistances:
        if resistance > current_index_at:
            if next_greater is None:
                next_greater = resistance
            else:
                second_next_greater = resistance
                break
    if next_greater is not None and abs(next_greater - current_index_at) <= 55:
        return second_next_greater

    return next_greater

# Example usage:
current_index_at = 424
print(sell_at(current_index_at))  # Output: 155 (since 66 is within 55 points
