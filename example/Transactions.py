import sys
sys.path.append('/var/www/html/myproject/')
# package import statement
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
from config import *
import pyotp, time
from lib import *
# from live_stream import *
from Symbols import *
from Strategy import *
from datetime import datetime
from mysql.connector import Error

from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from orders_lib import *
# import schedule

obj=SmartConnect(api_key="yWjMIfbo")

#login api call

data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
# refreshToken = data['data']['refreshToken']

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

live_history_params = {'exchange': 'NSE', 'symboltoken': '99926009', 'interval': 'FIVE_MINUTE', 'fromdate': '2024-05-23 08:10', 'todate': '2024-05-23 09:10'}
# history_date = "2024-05-08 15:25:00"
# current_date = "2024-05-08 15:30:00"

try:
    dates = stream_into_flow(obj,data)
except Exception as e:
    while True:
        print('Power nap++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        time.sleep(5)
        try:
            dates = stream_into_flow(obj, data)

        except Exception as e:
            time.sleep(5)
            print(f"An error occurred: {e}")
            print("Attempting to reconnect...")
            # Reconnect and continue the loop

            obj = SmartConnect(api_key="yWjMIfbo")
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())

            send_email('Flow update', "Please check the flow.. Connection might interupted.")

            continue