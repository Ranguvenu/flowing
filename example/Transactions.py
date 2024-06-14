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
from orders_lib import *
# import schedule

obj=SmartConnect(api_key="yWjMIfbo")

#login api call

data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
# refreshToken = data['data']['refreshToken']

#-----------------------------------------------------------------------------
# banknifty_index = obj.ltpData("NSE", "BANKNIFTY","99926009")
# print(banknifty_index)
# exit()
# # portfolio = obj.allholding()
import mysql.connector
from mysql.connector import errorcode
order_params = {'token': '37095', 'price': 2790.0, 'optionname': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}
order_details = {'token': '37095', 'price': 2790.0, 'optionname': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}


def order_testing(obj, order_details, transaction_type="BUY", current_index=49515):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": order_details['optionname'],
            "symboltoken": order_details['token'],
            "transactiontype": transaction_type,
            "exchange": "NFO",
            "ordertype": "MARKET",
            "producttype": "CARRYFORWARD",
            "duration": "DAY",
            "price": "0",
            "squareoff": 0,
            "stoploss": 0,
            "quantity": 15
        }

        orderid = obj.placeOrder(orderparams)
        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
        logger.info(f"PlaceOrder : {response['data']['script']}")

        sell_index = sell_at(current_index)

        # DB table name is order_records
        # response['data']['script'] is symbol
        # response['data']['orderid'] is orderid
        # sell_index is sell_index
        # current_index is nse_index
        # symbol, orderid, sell_index, nse_index are db table fields
        # there will be bought_at and lot_price extra columns, need to pass None
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Venu@5599',
            'database': 'mydb'
        }

        insert_data = (
            response['data']['script'],
            response['data']['orderid'],
            sell_index,
            current_index,
            15,  # bought_at
            15   # lot_price
        )

        # Insert the data into the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO order_records (symbol, orderid, sell_index, nse_index, bought_at, lot_price)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, insert_data)
        conn.commit()
        cursor.close()
        conn.close()

        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        print('error:', e)



# order_testing(obj, order_params, "BUY", )




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
