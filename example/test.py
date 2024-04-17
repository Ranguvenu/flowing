# from Strategy import *
# test = SupportResistance(42241, 49000)

import time, timedelta
from datetime import datetime


def spell_integer(n):
    if n < 20:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n]
    if n < 100:
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10-2] + ('_' + spell_integer(n%10) if n % 10 else '')
    if n < 1000:
        return spell_integer(n//100) + '_hundred_' + spell_integer(n%100) if n % 100 else ''
    for i, j in enumerate(('thousand', 'million', 'billion', 'trillion'), 1):
        if n < 1000 ** (i + 1):
            return spell_integer(n // 1000 ** i) + '_' + j + '_' + spell_integer(n % 1000 ** i) if n % 1000 ** i else ''
    return ''

# Example usage
# number = 25
# print(spell_integer(number))

data = [
    ['2024-04-15T11:15:00+05:30', 48028.6, 48045.75, 47998.95, 48031.6, 0],
    ['2024-04-15T11:20:00+05:30', 48028.35, 48057.15, 48009.7, 48050.9, 0],
    ['2024-04-15T11:25:00+05:30', 48055.9, 48058.0, 48028.1, 48049.1, 0]
]

# reversed_data = list(reversed(data))
# print(reversed_data)


# local_time = time.localtime()
# time = time.strftime("%Y-%m-%d %H:%M", local_time)
# print(time)

# def recent_historion_time(interval = False):
#     # Get current local time
    
#     local_time = time.localtime()
#     current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
#     current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")


#     # If current minute is a multiple of 5
#     if current_time.minute % interval == 0:
#         startime_readble = current_time.strftime("%Y-%m-%d %H:%M")
#     else:
#         # Find the closest past multiple of 5
#         minutes_diff = current_time.minute % interval

#         unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
#         time_correction = time.mktime(unix) - minutes_diff*60
#         startime_readble = datetime.fromtimestamp(time_correction)
#         startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
#     return startime_readble


# print(recent_historion_time(5))

# print(22 % 5)
def recent_historion_timeline(interval = False, into_past=False):
    # Get current local time
    
    local_time = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")


    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        startime_readble = current_time.strftime("%Y-%m-%d %H:%M")
    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval

        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = time.mktime(unix) - minutes_diff*60
        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")

    return {'startime_from' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

# test = recent_historion_timeline(5, 50*60)

# print(test)

# fruits = ["apple", "banana", "cherry", 'sss']
# for i, fruit in enumerate(fruits, start=1):
#     exec(f"fruit_{i} = '{fruit}'")

# # Now you have variables fruit_1, fruit_2, etc.
# print(fruit_1)
# print(fruit_2)
# print(fruit_3)
