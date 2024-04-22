import sys
sys.path.append('/var/www/html/myproject/')  
# package import statement
from smartapi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
from config import *
import pyotp, time
from Symbols import *
from datetime import datetime

def recent_number_of_histories_params(exchange=False, symboltoken=False, interval=False, histories_count=False, candle_timeframe=False, history_date=False):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Redirect standard output to a variable
    # output = sys.stdout
    captured_output = sys.stdout = sys.stderr = open('data.txt', 'a')

    print("sample text")

    # Reset standard output
    # sys.stdout = sys.stderr = output

    # into_past = candle_timeframe * histories_count*60
    # times = recent_historion_timeline(candle_timeframe, into_past, history_date)
    # print(times['startime_from_readable'])
    # exit()
    history_params = {'exchange': 'NSE', 'symboltoken': '99926009', 'interval': 'FIVE_MINUTE', 'fromdate': '2024-04-16 15:20', 'todate': '2024-04-16 15:20'}
    
    # Return both the history_params and the captured_output
    return history_params, captured_output

# def save_data(data):
#     with open('data.txt', 'a') as f:  # 'a' to append data to the file
#         f.write(data + '\n')

# Get data from recent_number_of_histories_params() function
data, captured_output = recent_number_of_histories_params()

# Save the data to a file
# save_data(str(data))
