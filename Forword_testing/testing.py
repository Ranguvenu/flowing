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

# upper_bound = find_upper_bound(numbers, given_number, margin)
# print(upper_bound)
# if upper_bound is not None:
#     print(f"The upper bound for {given_number} with a margin of {margin} is {upper_bound}.")
# else:
#     print(f"There is no upper bound for {given_number} in the list with the given margin.")



def best_option_fromlive(response_data, forname=False):
    closest_key = None
    closest_value = None

    target_value = 2500

    for item in response_data:
        for key, value in item.items():
            multiplied_value = value * 15
            if (multiplied_value <= target_value) and closest_value is None:
                closest_key = key
                closest_value = multiplied_value
            elif closest_value is not None and (multiplied_value < closest_value):
                closest_key = key
                closest_value = multiplied_value
    return {'token': closest_key, 'price': closest_value, 'symbol': forname[closest_key], 'shareprice': closest_value/15}


token_and_symbolname = {'53778': 'BANKNIFTY03JUL2453200CE', '53776': 'BANKNIFTY03JUL2453100CE', '53774': 'BANKNIFTY03JUL2453000CE', '53772': 'BANKNIFTY03JUL2452900CE', '53770': 'BANKNIFTY03JUL2452800CE', '53768': 'BANKNIFTY03JUL2452700CE', '53766': 'BANKNIFTY03JUL2452600CE', '53764': 'BANKNIFTY03JUL2452500CE', '53762': 'BANKNIFTY03JUL2452400CE', '53760': 'BANKNIFTY03JUL2452300CE', '53758': 'BANKNIFTY03JUL2452200CE', '53756': 'BANKNIFTY03JUL2452100CE'}
token_and_price = [{'53770': 224.0}, {'53760': 440.0}, {'53774': 172.15}, {'53764': 340.85}, {'53772': 194.15}, {'53762': 392.85}, {'53778': 129.85}, {'53756': 567.3}, {'53768': 260.0}, {'53776': 147.95}, {'53766': 300.0}]

# test = best_option_fromlive(token_and_price, token_and_symbolname)


def spell_integer_two(n):
    if n < 20:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n]
    if n < 100:
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10-2] + ('_' + spell_integer_two(n%10) if n % 10 else '')
    if n < 1000:
        return spell_integer_two(n//100) + '_hundred_' + spell_integer_two(n%100) if n % 100 else ''
    for i, j in enumerate(('thousand', 'million', 'billion', 'trillion'), 1):
        if n < 1000 ** (i + 1):
            return spell_integer_two(n // 1000 ** i) + '_' + j + '_' + spell_integer_two(n % 1000 ** i) if n % 1000 ** i else ''
    return ''

# print(test)

def ranger_options(obj):

    banknifty_ltp = obj.ltpData("NSE", "BANKNIFTY", 99926009)
    rounded_ltp = banknifty_ltp['data']['ltp'] % 100
    rounded_ltp = round(banknifty_ltp['data']['ltp'] - rounded_ltp)


    i = 0
    range_starts = rounded_ltp - 200
    options_inrange = {}

    while i <= 11:
        symbol_name = "BANKNIFTY"
        validate = "03JUL24"
        type = 'CE'

        options_inrange["option_" + spell_integer_two(i)] = symbol_name + validate + str(range_starts) + type
        range_starts += 100
        i += 1
    options_inrange['current_ltp'] = banknifty_ltp['data']['ltp']
    return options_inrange



import mysql.connector

# Replace with your MySQL database connection details

# Data from the JSON structure
data = {
    "35164": "BANKNIFTY03JUL2454900CE",
    "35792": "BANKNIFTY03JUL2454800CE",
    "35681": "BANKNIFTY03JUL2454700CE",
    "35661": "BANKNIFTY03JUL2454600CE",
    "53798": "BANKNIFTY03JUL2454500CE",
    "35578": "BANKNIFTY03JUL2454400CE",
    "35457": "BANKNIFTY03JUL2454300CE",
    "35453": "BANKNIFTY03JUL2454200CE",
    "35450": "BANKNIFTY03JUL2454100CE",
    "53796": "BANKNIFTY03JUL2454000CE",
    "35393": "BANKNIFTY03JUL2453900CE",
    "53794": "BANKNIFTY03JUL2453800CE",
    "53792": "BANKNIFTY03JUL2453700CE",
    "53790": "BANKNIFTY03JUL2453600CE",
    "53788": "BANKNIFTY03JUL2453500CE",
    "53785": "BANKNIFTY03JUL2453400CE",
    "53782": "BANKNIFTY03JUL2453300CE",
    "53778": "BANKNIFTY03JUL2453200CE",
    "53776": "BANKNIFTY03JUL2453100CE",
    "53774": "BANKNIFTY03JUL2453000CE",
    "53772": "BANKNIFTY03JUL2452900CE",
    "53770": "BANKNIFTY03JUL2452800CE",
    "53768": "BANKNIFTY03JUL2452700CE",
    "53766": "BANKNIFTY03JUL2452600CE",
    "53764": "BANKNIFTY03JUL2452500CE",
    "53762": "BANKNIFTY03JUL2452400CE",
    "53760": "BANKNIFTY03JUL2452300CE",
    "53758": "BANKNIFTY03JUL2452200CE",
    "53756": "BANKNIFTY03JUL2452100CE",
    "53754": "BANKNIFTY03JUL2452000CE",
    "53752": "BANKNIFTY03JUL2451900CE",
    "53750": "BANKNIFTY03JUL2451800CE",
    "53748": "BANKNIFTY03JUL2451700CE",
    "53746": "BANKNIFTY03JUL2451600CE",
    "53744": "BANKNIFTY03JUL2451500CE",
    "53742": "BANKNIFTY03JUL2451400CE",
    "53740": "BANKNIFTY03JUL2451300CE",
    "53736": "BANKNIFTY03JUL2451200CE",
    "53732": "BANKNIFTY03JUL2451100CE",
    "53728": "BANKNIFTY03JUL2451000CE",
    "53726": "BANKNIFTY03JUL2450900CE",
    "53722": "BANKNIFTY03JUL2450800CE",
    "53720": "BANKNIFTY03JUL2450700CE",
    "53718": "BANKNIFTY03JUL2450600CE",
    "53716": "BANKNIFTY03JUL2450500CE",
    "53714": "BANKNIFTY03JUL2450400CE",
    "53712": "BANKNIFTY03JUL2450300CE",
    "53710": "BANKNIFTY03JUL2450200CE",
    "53708": "BANKNIFTY03JUL2450100CE",
    "53705": "BANKNIFTY03JUL2450000CE",
    "53702": "BANKNIFTY03JUL2449900CE",
    "53700": "BANKNIFTY03JUL2449800CE"
}

# Additional value to be inserted in all rows
validate_value = '16JUL24'

def option_seeding(data, validate_value):
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Venu@5599',
        'database': 'mydb'
    }
    # Connect to MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare SQL query
        sql = "INSERT INTO inrange_options (symbol, token, validate) VALUES (%s, %s, %s)"

        # Iterate through data and execute the query
        for token, symbol in data.items():
            cursor.execute(sql, (symbol, token, validate_value))

        # Commit changes
        conn.commit()
        print(cursor.rowcount, "record(s) inserted successfully into inrange_options")

    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def get_valid_options():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Venu@5599',
        'database': 'mydb'
    }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare SQL query
        sql = "SELECT token, symbol FROM inrange_options WHERE validate = %s"
        validate_value = '03JUL24'
        cursor.execute(sql, (validate_value,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Convert rows to dictionary format
        result_dict = {token: symbol for token, symbol in rows}

        # Print or use the result dictionary
        print("Result Dictionary:")
        print(result_dict)

    except mysql.connector.Error as error:
        print("Error retrieving data from MySQL table:", error)

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySQL connection is closed")



import mysql.connector

def get_valid_options():
    # Replace with your MySQL database connection details
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Venu@5599',
        'database': 'mydb'
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare SQL query to retrieve data
        sql_select = "SELECT token, symbol FROM inrange_options WHERE validate = %s"
        validate_value = '03JUL24'
        cursor.execute(sql_select, (validate_value,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Create dictionary and list
        result_dict = {token: symbol for token, symbol in rows}
        token_list = [token for token, _ in rows]

        return result_dict, token_list

    except mysql.connector.Error as error:
        print("Error retrieving data from MySQL table:", error)
        return {}, []

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# # Example usage:
# result_dict, token_list = valid_options()
# print("Result Dictionary:")
# print(result_dict)
# print("Token List:")
# print(token_list)

import smtplib

from email.mime.text import MIMEText

def send_email(subject, body):

    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Gmail's TLS port
    sender_email = 'venucharyrangu@gmail.com'
    receiver_email = 'venu.chary@moodle.com'
    smtp_username = 'venucharyrangu@gmail.com'
    smtp_password = 'dbvb zwju zuvr hgjv'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()


print(send_email('HIHIII', 'hihiihiihi'))