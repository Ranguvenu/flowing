from lib import *
import time

option_ltplist = [{'37053': 55.3}, {'37297': 15.45}, {'37012': 321.0}, {'36882': 964.0}, {'36804': 2200.0}, {'36806': 2025.35}, {'37059': 46.0}, {'36884': 876.1}, {'37017': 272.1}, {'36963': 639.95}, {'36920': 716.7}]
token_names = {'39607': 'BANKNIFTY31JUL2454900CE', '39603': 'BANKNIFTY31JUL2454800CE', '38473': 'BANKNIFTY31JUL2454700CE', '38470': 'BANKNIFTY31JUL2454600CE', '38036': 'BANKNIFTY31JUL2454500CE', '38017': 'BANKNIFTY31JUL2454400CE', '37984': 'BANKNIFTY31JUL2454300CE', '37967': 'BANKNIFTY31JUL2454200CE', '37862': 'BANKNIFTY31JUL2454100CE', '37858': 'BANKNIFTY31JUL2454000CE', '37297': 'BANKNIFTY31JUL2453900CE', '37274': 'BANKNIFTY31JUL2453800CE', '37087': 'BANKNIFTY31JUL2453700CE', '37081': 'BANKNIFTY31JUL2453600CE', '37064': 'BANKNIFTY31JUL2453500CE', '37059': 'BANKNIFTY31JUL2453400CE', '37053': 'BANKNIFTY31JUL2453300CE', '37044': 'BANKNIFTY31JUL2453200CE', '37042': 'BANKNIFTY31JUL2453100CE', '37040': 'BANKNIFTY31JUL2453000CE', '37038': 'BANKNIFTY31JUL2452900CE', '37032': 'BANKNIFTY31JUL2452800CE', '37030': 'BANKNIFTY31JUL2452700CE', '37027': 'BANKNIFTY31JUL2452600CE', '37017': 'BANKNIFTY31JUL2452500CE', '37012': 'BANKNIFTY31JUL2452400CE', '36995': 'BANKNIFTY31JUL2452300CE', '36990': 'BANKNIFTY31JUL2452200CE', '36985': 'BANKNIFTY31JUL2452100CE', '36970': 'BANKNIFTY31JUL2452000CE', '36963': 'BANKNIFTY31JUL2451900CE', '36920': 'BANKNIFTY31JUL2451800CE', '36906': 'BANKNIFTY31JUL2451700CE', '36884': 'BANKNIFTY31JUL2451600CE', '36882': 'BANKNIFTY31JUL2451500CE', '36863': 'BANKNIFTY31JUL2451400CE', '36857': 'BANKNIFTY31JUL2451300CE', '36852': 'BANKNIFTY31JUL2451200CE', '36838': 'BANKNIFTY31JUL2451100CE', '36836': 'BANKNIFTY31JUL2451000CE', '36832': 'BANKNIFTY31JUL2450900CE', '36830': 'BANKNIFTY31JUL2450800CE', '36826': 'BANKNIFTY31JUL2450700CE', '36824': 'BANKNIFTY31JUL2450600CE', '36820': 'BANKNIFTY31JUL2450500CE', '36818': 'BANKNIFTY31JUL2450400CE', '36806': 'BANKNIFTY31JUL2450300CE', '36804': 'BANKNIFTY31JUL2450200CE', '36796': 'BANKNIFTY31JUL2450100CE', '36792': 'BANKNIFTY31JUL2450000CE', '36790': 'BANKNIFTY31JUL2449900CE', '36788': 'BANKNIFTY31JUL2449800CE'}

def best_option_fromlive(response_data, forname=False):
    closest_key = None
    closest_value = None
    closest_shareprice = None

    target_value = 2700

    for item in response_data:
        for key, value in item.items():
            multiplied_value = value * 15
            if multiplied_value <= target_value:
                if closest_value is None or multiplied_value > closest_value:
                    closest_key = key
                    closest_value = multiplied_value
                    closest_shareprice = value
    if closest_key is not None:
        return {'token': closest_key, 'price': closest_value, 'symbol': forname[closest_key], 'shareprice': closest_shareprice}
    else:
        return None

# hi = best_option_fromlive(option_ltplist, token_names)

# print(hi)

# import time

# def timer(seconds):
#     for remaining in range(seconds, 0, -1):
#         print(f"Time left: {remaining} seconds", end='\r')
#         time.sleep(1)
#     print("Time's up!")

# # Set the timer for a specific number of seconds
# # timer(10)

def next_fivemloop_inseconds():
    # Get the current time
    now = datetime(2024, 7, 18, 11, 25.355555)
    # print(type(now))

    # Calculate the next multiple of 5 minutes
    if now.minute % 5 != 0:
        next_minute = (now.minute // 5 + 1) * 5
    else:
        next_minute = now.minute

    # Handle the case where next_minute is 60
    if next_minute == 60:
        next_minute = 0
        next_time = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        next_time = now.replace(minute=next_minute, second=0, microsecond=0)

    # Calculate the time difference in seconds
    next_loop_inseconds = (next_time - now).total_seconds()

    return int(next_loop_inseconds)


# print(next_fivemloop_inseconds())


bounds = [51884.68, 52229.11, 52589.62, 53023.84]