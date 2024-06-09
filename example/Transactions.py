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

from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger

# import schedule

obj=SmartConnect(api_key="yWjMIfbo")

#login api call

data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
# refreshToken = data['data']['refreshToken']

#-----------------------------------------------------------------------------

{'variety': 'NORMAL',
'tradingsymbol': 'ICICIBANK27MAY21600CE',
'symboltoken': '88488',
'transactiontype': 'SELL',
'exchange': 'NFO',
'ordertype': 'MARKET',
'producttype': 'CARRYFORWARD',
'duration': 'DAY',
'price': '0',
'squareoff': 0,
'stoploss': 0,
'quantity': 1375}



ss = {'token': '37095', 'price': 2790.0, 'optionname': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}


try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "BANKNIFTY12JUN2450700CE",
        "symboltoken": "37095",
        "transactiontype": "BUY",
        "exchange": "NFO",
        "ordertype": "MARKET",
        "producttype": "CARRYFORWARD",
        "duration": "DAY",
        "price": "0",
        "squareoff": 0,
        "stoploss": 0,
        "quantity": 45
        }
    # Method 1: Place an order and return the order ID
    orderid = obj.placeOrder(orderparams)

    orderid = obj.placeOrder(orderparams)
    logger.info(f"PlaceOrder : {orderid}")
    # Method 2: Place an order and return the full response
    response = obj.placeOrderFullResponse(orderparams)
    logger.info(f"PlaceOrder : {response}")
except Exception as e:
    logger.exception(f"Order placement failed: {e}")

exit()




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