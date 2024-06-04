import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

def greenery_recording(ltp, time, confirmation=False, flow_type=False):
    timeto_inix = datetime.strptime(time, "%Y-%m-%d %H:%M")
    day = timeto_inix.strftime("%A")  # Get the day from the datetime

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Venu@5599',
        'database': 'mydb'
    }

    try:
        dbconnection = mysql.connector.connect(**db_config)
        cursor = dbconnection.cursor()
        insert_query = "INSERT INTO greenery_second (datetime, day, confirmation, flow_type, ltp, unix_time) VALUES (%s, %s, %s, %s, %s, %s)"
        data_to_insert = [time, day, confirmation, flow_type, ltp, timeto_inix]
        cursor.execute(insert_query, data_to_insert)
        dbconnection.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            # Duplicate entry, so just skip insertion
            print("Duplicate entry found. Skipping insertion.")
        else:
            # Another MySQL error occurred, print error
            print("MySQL Error:", err)
    finally:
        # Close the database connection
        cursor.close()
        dbconnection.close()
