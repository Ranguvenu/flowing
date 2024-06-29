# from optionslib import *
ss = {'token': '37095', 'price': 2790.0, 'symbol': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}

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


# try:
#     orderparams = {
#         "variety": "NORMAL",
#         "tradingsymbol": "BANKNIFTY12JUN2450700CE",
#         "symboltoken": "37095",
#         "transactiontype": "BUY",
#         "exchange": "NFO",
#         "ordertype": "MARKET",
#         "producttype": "CARRYFORWARD",
#         "duration": "DAY",
#         "price": "0",
#         "squareoff": 0,
#         "stoploss": 0,
#         "quantity": 45
#         }
#     # Method 1: Place an order and return the order ID
#     orderid = obj.placeOrder(orderparams)

#     orderid = obj.placeOrder(orderparams)
#     logger.info(f"PlaceOrder : {orderid}")
#     # Method 2: Place an order and return the full response
#     response = obj.placeOrderFullResponse(orderparams)
#     logger.info(f"PlaceOrder : {response}")
# except Exception as e:
#     logger.exception(f"Order placement failed: {e}")

import time
from datetime import datetime, timedelta
import pytz

def wait_until_next_5_minute_mark():
    # Define the timezone for Asia/Kolkata
    kolkata_timezone = pytz.timezone('Asia/Kolkata')

    while True:
        # Get the current time in Asia/Kolkata timezone
        now = datetime.now(kolkata_timezone)
        # Calculate the next 5-minute mark
        next_minute = (now.minute // 5 + 1) * 5 % 60
        next_hour = now.hour + (1 if next_minute == 0 else 0)
        next_time = now.replace(hour=next_hour % 24, minute=next_minute, second=0, microsecond=0)
        # Calculate the time to sleep
        time_to_sleep = (next_time - now).total_seconds()
        # Wait until the next 5-minute mark
        time.sleep(time_to_sleep)
        # Perform the task
        print(f"Task executed at {datetime.now(kolkata_timezone).strftime('%Y-%m-%d %H:%M:%S')}")
        # Add your task logic here

# if __name__ == "__main__":
#     wait_until_next_5_minute_mark()
import mysql.connector

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Venu@5599',
    'database': 'mydb'
}

def get_entered_options():
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Define the query to fetch records with status "Entered"
        query = "SELECT * FROM order_records WHERE status = 'Entereds'"
        # Execute the query
        cursor.execute(query)

        # Fetch all the records
        records = cursor.fetchall()
        # Print the fetched records
        return records
        for record in records:
            print(record)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# print(get_entered_options())
import time
from datetime import datetime, timedelta
import pytz

def loop_until_next_5_minute_markaa():
    # Define the timezone for Asia/Kolkata
    kolkata_timezone = pytz.timezone('Asia/Kolkata')

    # Get the current time in Asia/Kolkata timezone
    now = datetime.now(kolkata_timezone)

    # Calculate the next multiple of 5 seconds
    next_second = (now.second // 5 + 1) * 5
    if next_second >= 60:
        next_second = 0
        now += timedelta(minutes=1)
    next_time = now.replace(second=next_second, microsecond=0)

    # Wait until the next multiple of 5 seconds
    time_to_sleep = (next_time - datetime.now(kolkata_timezone)).total_seconds()
    time.sleep(time_to_sleep)

    while True:
        # Get the current time in Asia/Kolkata timezone
        now = datetime.now(kolkata_timezone)



        # if now % 5 == 0:
        #     first_multiple_of_five  = now.minute

        # print(now.minute)
        # exit()
        # Check if the current time is at a 5-minute mark
        if now.minute % 5 == 0 and now.second == 0:
            break

        try:
            first_multiple_of_five
        except:
            if now.minute % 5 == 0:
                first_multiple_of_five = now.minute
                print('hihi')
                break



        # Perform the task
        print(f"Task executed at {now.strftime('%Y-%m-%d %H:%M:%S')}")
        # Add your task logic here

        # Wait for the next 5-second interval
        time.sleep(5 - now.second % 5)


# if __name__ == "__main__":
#     loop_until_next_5_minute_mark()
import time
from datetime import datetime, timedelta
import pytz

def loop_until_next_5_minute_mark():
    # Define the timezone for Asia/Kolkata
    kolkata_timezone = pytz.timezone('Asia/Kolkata')

    # Perform the initial task here
    # Example initial task


    # Get the current time in Asia/Kolkata timezone
    now = datetime.now(kolkata_timezone)

    # Calculate the next multiple of 5 seconds
    next_second = (now.second // 5 + 1) * 5
    if next_second >= 60:
        next_second = 0
        now += timedelta(minutes=1)
    next_time = now.replace(second=next_second, microsecond=0)

    # Wait until the next multiple of 5 seconds
    time_to_sleep = (next_time - datetime.now(kolkata_timezone)).total_seconds()
    time.sleep(time_to_sleep)

    while True:
        # Get the current time in Asia/Kolkata timezone

        start_time = time.time()
        #Schenarios comes here
        # initial_task()
        end_time = time.time()
        time_defferance = int(end_time - start_time)
        now = datetime.now(kolkata_timezone)
        if time_defferance > 0:
            seconds_time = now.second - time_defferance

        # initial_task()

        # Check if the current time is at a 5-minute mark
        if now.minute % 5 == 0 and seconds_time % 5 == 0:
            #check the time record
            #if exist  continue
            #else insert the current time record and exit/break
            break
        # Perform the task
        print(f"Task executed at {now.strftime('%Y-%m-%d %H:%M:%S')}")
        # Add your task logic here

        # Wait for the next 5-second interval
        next_second = (now.second // 5 + 1) * 5
        if next_second >= 60:
            next_second = 0
            now += timedelta(minutes=1)
        next_time = now.replace(second=next_second, microsecond=0)


        time_to_sleep = (next_time - datetime.now(kolkata_timezone)).total_seconds()
        time.sleep(time_to_sleep)

def initial_task():
    # Example initial task that might take a few seconds
    print("Initial task started")
    time.sleep(2.9)  # Simulate task taking 3 seconds
    print("Initial task completed")

# if __name__ == "__main__":
#     loop_until_next_5_minute_mark()
# import time

# def initial_task():
#     # Your code goes here
#     time.sleep(5)
#     return 'hihihih'
# # Measure execution time
# start_time = time.time()
# result = initial_task()
# end_time = time.time()

# # Calculate elapsed time
# elapsed_time = end_time - start_time
# print(f"Execution time: {elapsed_time} seconds")
# print(f"Result: {result}")
import pytz
from datetime import datetime

# Define the Kolkata timezone
kolkata_timezone = pytz.timezone('Asia/Kolkata')

# # Get the current time in Asia/Kolkata timezone
# now = datetime.now(kolkata_timezone)

# # Remove seconds and microseconds
# readable_now_without_seconds = now.replace(second=0, microsecond=0)

# # Convert to Unix timestamp
# unix_timestamp_without_seconds = int(now_without_seconds.timestamp())

# print("Current time in Kolkata (with seconds):", now)
# print("Unix timestamp in Kolkata (with seconds):", int(now.timestamp()))

# print("\nCurrent time in Kolkata (without seconds):", now_without_seconds)
# print("Unix timestamp in Kolkata (without seconds):", unix_timestamp_without_seconds)
test = {'id': 15, 'symbol': 'BANKNIFTY03JUL2453700CE', 'bought_at': 15, 'sell_index': 52615, 'lot_price': 15, 'nse_index': '51782.75', 'orderid': '240622000000399', 'status': 'Entered', 'symboltoken': '53792', 'type': 'BUY', 'sell_orderid': None}
# print(test['symbol'])

{'id': 15, 'symbol': 'BANKNIFTY03JUL2453700CE', 'bought_at': 15, 'sell_index': 52615, 'lot_price': 15, 'nse_index': '51782.75', 'orderid': '240622000000399', 'status': 'Entered', 'symboltoken': '53792', 'type': 'BUY', 'sell_orderid': None}

        # orderparams = {
        #     "variety": "NORMAL",
        #     "tradingsymbol": "order_details['symbol']",
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
from logzero import logger
def option_order_record(obj, order_details={}, transaction_type="BUY", current_index=51150):
    # print(order_details)
    # exit()
    order_details = {
        'symbol' : "BANKNIFTY03JUL2452800CE",
        'token' : 53770
    }
    # order_details['symbol'] = "BANKNIFTY03JUL2452800CE"
    # order_details['token'] = 53770
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": order_details['symbol'],
            "symboltoken":  order_details['token'],
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
        if transaction_type == "SELL":

            # Update records with reference "symbol"

            db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'Venu@5599',
                'database': 'mydb'
            }

            update_data = (
                response['data']['orderid'],
                sell_at(current_index),  # Assuming sell_at is a defined function
                current_index,
                15,  # bought_at
                15,  # lot_price
                'Achieved',
                order_details['token'],
                transaction_type,
                order_details['symbol']
            )

            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()

                # Update query
                update_query = """
                UPDATE order_records
                SET sell_orderid = %s, sell_index = %s, nse_index = %s, bought_at = %s, lot_price = %s, status = %s, token = %s, type = %s
                WHERE symbol = %s AND sell_orderid IS NULL
                """

                # Example update_data, make sure this matches your actual data
                # update_data should be a tuple with the values in the correct order
                # Execute the update query
                cursor.execute(update_query, update_data)

                # Commit the changes
                conn.commit()

            except Exception as e:
                logger.error(f"Error: {e}")
                print('error:', e)
        else:
            sell_index = sell_at(current_index)
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
                15,  # lot_price
                'Entered',
                order_details['token'],
                transaction_type
            )

            # Insert the data into the database
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO order_records (symbol, orderid, sell_index, nse_index, bought_at, lot_price, status, token, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, insert_data)
            conn.commit()
            cursor.close()
            conn.close()
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        print('error:', e)


bounds = [51966.51, 52186.93, 52460.21, 52701.59, 52998.74, 53182.99]
given_number = 52097.45
margin = 51

def find_bounds(numbers, given_number, margin):
    lower_bound = None
    upper_bound = None

    for i in range(len(numbers) - 1):
        if numbers[i] < given_number < numbers[i + 1]:
            if (numbers[i + 1] - given_number) > margin:
                return numbers[i], numbers[i + 1]
            else:
                for j in range(i + 2, len(numbers)):
                    if (numbers[j] - given_number) > margin:
                        return numbers[i], numbers[j]
                return numbers[i], None  # In case no suitable upper_bound is found

    return upper_bound

# print(find_bounds(bounds, given_number, margin))
numbers = [5, 10, 15, 20, 25]
given_number = 6
margin = 3

def find_upper_bound(numbers, given_number, margin):
    for i in range(len(numbers) - 1):
        if numbers[i] < given_number < numbers[i + 1]:
            if (numbers[i + 1] - given_number) > margin:
                return numbers[i + 1]
            else:
                for j in range(i + 2, len(numbers)):
                    if (numbers[j] - given_number) > margin:
                        return numbers[j]
                return None  # In case no suitable upper_bound is found

    return None

upper_bound = find_upper_bound(numbers, given_number, margin)
print(upper_bound)
# if upper_bound is not None:
#     print(f"The upper bound for {given_number} with a margin of {margin} is {upper_bound}.")
# else:
#     print(f"There is no upper bound for {given_number} in the list with the given margin.")
