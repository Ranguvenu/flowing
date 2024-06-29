from datetime import datetime, timedelta

def add_five_minutes(current_time):
    return (datetime.strptime(current_time, "%Y-%m-%d %H:%M") + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M")

# Example usage
current_time = "2024-05-14 09:55"

# new_time = add_five_minutes(current_time)
# print("New Time:", new_time)
# Initialize index_targets list
# index_targets = []
# def test():
#     print('sdsd')
# sample = test()

# # List of variables to check
# variables = [15, 155, -55, sample]
# # Initialize index_targets list
# index_targets = []
# for var in variables:
#     if var is not None:
#         if var > 0:
#             if var not in index_targets:
#                 index_targets.append(var)
#         elif var < 0:
#             if -var in index_targets:
#                 index_targets.remove(-var)

# print(index_targets)

import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Venu@5599',
    'database': 'mydb'
}

# Data to update, including the new 'type' field
update_data = ['240620001239381', None, 51150, 15, 15, 'pending', '56100', 'SELL', 'BANKNIFTY26JUN2452000CE']

# Establish a database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Update query, including the new 'type' field
update_query = """
UPDATE order_records
SET orderid = %s, sell_index = %s, nse_index = %s, bought_at = %s, lot_price = %s, status = %s, symboltoken = %s, type = %s
WHERE symbol = %s
"""

# Execute the update query
cursor.execute(update_query, update_data)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

exit()

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Venu@5599',
    'database': 'mydb'
}
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()
# sell_index = "500155"
# select_query = """
# SELECT *
# FROM order_records
# WHERE status NOT LIKE 'completed' AND sell_index =
# """ + sell_index
# cursor.execute(select_query)
# rows = cursor.fetchall()


def options_to_sell(sell_index):
    db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Venu@5599',
    'database': 'mydb'
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    select_query = """
    SELECT *
    FROM order_records
    WHERE status NOT LIKE 'completed' AND sell_index =
    """ + sell_index
    cursor.execute(select_query)
    rows = cursor.fetchall()

# print(rows)