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
history_date = "2024-06-05 11:45:00"
current_date = "2024-06-05 11:50:00"
# dates =

#------------------------------------------------------------------------------------

# banknifty_index = connecting_object.ltpData("NSE", "BANKNIFTY","99926009")
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
            None,  # bought_at
            None   # lot_price
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

order_testing(obj, order_details)
exit()
#-------------------------------------------------------------------------------------

try:
    dates = forword_testing(connecting_object, current_date, history_date)
    history_date = dates['history_date']
    current_date = dates['current_date']
    forword_testing(connecting_object, current_date, history_date)
except Exception as e:
    while True:
        print('Power nap++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        time.sleep(5)
        try:
            dates = forword_testing(connecting_object, current_date, history_date)

        except Exception as e:
            time.sleep(5)
            print(f"An error occurred: {e}")
            print("Attempting to reconnect...")
            # Reconnect and continue the loop

            obj = SmartConnect(api_key="yWjMIfbo")
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())

            continue

