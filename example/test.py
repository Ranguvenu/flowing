import sys
sys.path.append('/var/www/html/myproject/')  
# package import statement
from smartapi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
from config import *
import pyotp, time, timedelta
from Symbols import *
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



fruits = {"fruit_one": "apple", "fruit_two": "banana", "fruit_three": "cherry", "fruit": "sss"}

# Creating dynamic variables from dictionary
for key, value in fruits.items():
    globals()[key] = value

# Accessing dynamic variables
# print(fruit_one)    # Output: apple
# print(fruit_two)    # Output: banana
# print(fruit_three)  # Output: cherry
# print(fruit)        # Output: sss
def times_giving(begins=False, interval=False):
    begins = "2024-04-16 09:15"
    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M")
    begins_unix = int(begins_dt_format.timestamp())
    begins_timeonly = begins_dt_format.time()
    # while 

    then_giventime = begins_timeonly.replace(hour=15, minute=30)
    # print(then_giventime)
    # exit()



    begins_timeonly = datetime.strptime(begins_timeonly.strftime("%H:%M:%S"), "%H:%M:%S").time()

    # Extract hour and minute parts
    hour = begins_timeonly.hour
    minute = begins_timeonly.minute


    if (hour < 9 and hour != 3 and hour != 2 and hour != 1) or (hour == 9 and minute < 15):
        giventime = "2024-04-16 09:14"
        begins_unix = begins_unix - 86400

    # then_giventime_bacames = make yesterdays 3:30pm

    print("Hour:", hour)
    print("Minute:", minute)

    return begins_timeonly





# begins = "2024-04-16 09:15"
# new_time = "15:30"

# # concatination or replacing time
# new_begins = (datetime.strptime(begins, "%Y-%m-%d %H:%M").replace(hour=int(new_time[:2]), minute=int(new_time[3:]))).strftime("%Y-%m-%d %H:%M")

# print(times_giving())


# from datetime import datetime

# def next_times_giving(begins="2024-04-16 09:35"):
#     begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M")
#     begins_unix = int(begins_dt_format.timestamp())
#     reduced_unix = begins_unix - 5 * 60
#     reduced_time = datetime.fromtimestamp(reduced_unix)
#     formatted_date = reduced_time.strftime("%Y-%m-%d %H:%M")

#     print(formatted_date)
#     return formatted_date

# Example usage:
# times_giving_two()



# my_dict = {}

# # Method 1: Using the `not` operator
# if not my_dict:
#     print("Dictionary is empty")

# # Method 2: Comparing its length to zero
# if len(my_dict) == 0:
#     print("Dictionary is empty")

# # Method 3: Directly check if it's empty
# if my_dict == {}:
#     print("Dictionary is empty")


# def next_five():
#     current_time = time.localtime()
#     current_time = current_time.strptime()

#     print(current_time)

# next_five()

def next_fivemloop_inseconds():
    local_time = time.localtime()
    current_time = int(time.strftime("%M", local_time))
    # print(time.strftime("%M", local_time))
    # exit()
    # Sample next_time
    next_time = time.strftime("%Y-%m-%d %H:%M", local_time)

    if current_time % 5 != 0:
        current_time = (current_time // 5 + 1) * 5

    # Split next_time into date and time components
    date_part, time_part = next_time.split()

    # Replace the minute part with current_time
    new_time = time_part[:3] + str(current_time)

    # Reconstruct the modified next_time
    modified_next_time = date_part + ' ' + new_time
    modified_next_time = datetime.strptime(modified_next_time, "%Y-%m-%d %H:%M")
    modified_next_time = int(modified_next_time.timestamp())
    now_the_time = int(time.time())
    next_loop_inseconds = modified_next_time - now_the_time
    return next_loop_inseconds


# def test():

#     return {'history_date':'history_date', 'current_date':'current_date'}
# testsse = test()
# print(testsse['history_date'])

import sys
sys.path.append('/var/www/html/myproject/')  
from smartapi import SmartConnect
from config import *
import pyotp
from datetime import datetime, timedelta
from datetime import datetime, time, timedelta

def into_the_yesterday(begins="2024-04-15 09:15:00"):
    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")
    
    # Extract time component from begins_dt_format
    time_component = begins_dt_format.time()

    # Define the target times for comparison
    target_time_1 = time(9, 15, 0)
    target_time_2 = time(9, 10, 0)
    target_time_1 = datetime.strptime("09:15:00", "%H:%M:%S")
    target_time_1 = target_time_1.time()
    target_time_2 = datetime.strptime("09:10:00", "%H:%M:%S")
    target_time_2 = target_time_2.time()
    # print(target_time_1.time())
    # exit()

    # If time is exactly 9:15, return yesterday's 15:35
    if time_component == target_time_1:
        # Calculate yesterday's date by subtracting 1 day
        yesterday = begins_dt_format - timedelta(days=1)
        # Create a new datetime object for yesterday's 15:35
        return datetime(year=yesterday.year, month=yesterday.month, day=yesterday.day, hour=15, minute=35, second=0)
    # If time is exactly 9:10, return yesterday's 15:30
    elif time_component == target_time_2:
        # Calculate yesterday's date by subtracting 1 day
        yesterday = begins_dt_format - timedelta(days=1)
        # Create a new datetime object for yesterday's 15:30
        return datetime(year=yesterday.year, month=yesterday.month, day=yesterday.day, hour=15, minute=30, second=0)
    else:
        return begins  # Return False if neither condition is met
# print(next_times_giving())