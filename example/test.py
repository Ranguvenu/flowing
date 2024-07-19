from datetime import datetime, timedelta
import time

def next_fivemloop_inseconds():
    # Get the current time
    now = datetime.now()

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

# Example usage
# print(next_fivemloop_inseconds())
import time

def timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds:.1f} seconds", end='\r')
        time.sleep(0.1)
        seconds -= 0.1
    print("Time's up!                             ")


# print(timer(5.55555555555555555555555))
# exit()
from mysql.connector import Error
from logzero import logger
import mysql.connector

update_data = ('240719100534771', 52284.8, 15, 15, 'Achieved', '48730', 'SELL', 'BANKNIFTY24JUL2451500PE', 'CE')
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Venu@5599',
    'database': 'mydb'
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Update query
    update_query = """
    UPDATE order_records
    SET sell_orderid = %s, nse_index = %s, bought_at = %s, lot_price = %s, status = %s, token = %s, type = %s
    WHERE symbol = %s AND sell_orderid IS NULL AND option_type = %s
    """

    # Log the query and data
    logger.info(f"Executing query: {update_query}")
    logger.info(f"With data: {update_data}")

    # Execute the update query
    cursor.execute(update_query, update_data)

    # Commit the changes
    conn.commit()

    logger.info("Update successful")

except Error as e:
    logger.error(f"Error: {e}")
    if conn.is_connected():
        conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
