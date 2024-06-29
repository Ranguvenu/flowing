import sys
sys.path.append('/var/www/html/myproject/')
from SmartApi import SmartConnect
import pyotp, time
from datetime import datetime
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
from config import *
from lib import *




connecting_object = SmartConnect(api_key="yWjMIfbo")
# data = connecting_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
history_date = "2024-06-25 11:40:00"
current_date = "2024-06-25 11:45:00"
# dates =
connection_data = connecting_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
#------------------------------------------------------------------------------------

# banknifty_index = connecting_object.ltpData("NSE", "BANKNIFTY","99926009")
# order_details = {'token': '37095', 'price': 2790.0, 'symbol': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}


# orderparams = {
#     "variety": "NORMAL",
#     "tradingsymbol": "BANKNIFTY03JUL2453700CE",
#     "symboltoken": 53792,
#     "transactiontype": "SELL",
#     "exchange": "NFO",
#     "ordertype": "MARKET",
#     "producttype": "CARRYFORWARD",
#     "duration": "DAY",
#     "price": "0",
#     "squareoff": 0,
#     "stoploss": 0,
#     "quantity": 15
# }
# orderid = connecting_object.placeOrder(orderparams)
# response = connecting_object.placeOrderFullResponse(orderparams)
# print(response)
# exit()

# ltp = connecting_object.ltpData("NSE", "BANKNIFTY", "99926009")['data']['ltp']
#-------------------------------------------------------------------------------------
forword_testing(connecting_object, current_date, history_date, connection_data)
exit()
try:
    dates = forword_testing(connecting_object, current_date, history_date, connection_data)
    history_date = dates['history_date']
    current_date = dates['current_date']
    forword_testing(connecting_object, current_date, history_date, connection_data)
except Exception as e:
    while True:
        print('Power nap++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        time.sleep(5)
        try:
            dates = forword_testing(connecting_object, current_date, history_date, connection_data)

        except Exception as e:
            time.sleep(5)
            print(f"An error occurred: {e}")
            print("Attempting to reconnect...")
            # Reconnect and continue the loop

            obj = SmartConnect(api_key="yWjMIfbo")
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())

            continue

