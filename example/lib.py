#Operational Functions
import sys
sys.path.append('/var/www/html/myproject/')  
from smartapi import SmartConnect
from config import *
import pyotp, time
import mysql.connector

#The Connection

def StreamLTP(Exchange, Symbol, SymbolCode, Intervel, connection):


    # Example: Execute a SELECT query
    # cursor.execute("SELECT * FROM ltp_data")
    # result = cursor.fetchall()

    # Example: Insert data into the table


    sample = "sample"
    i = 0
    while True:
        Ltp = connection.ltpData("NSE", "SBIN-EQ", 3045)
        # print('sfdsjfsdf')
        print(Ltp)
        print('goodthings take time')
        # exit()
        Ltp_insertion(i, Ltp)
        current_time_struct = time.localtime()

        # if i == 0:
        #     PriceA = Ltp
        # if PriceA < Ltp and i > 0:
        #     print("Buy")

        # elif PriceA > Ltp and i == 1:
        #     PriceB = Ltp
        # else
        # # print(Ltp)
        # # exit()

        print("Last Trading Price: ", Ltp['data']['ltp'], "@",  time.strftime("%H:%M:%S", current_time_struct))
        time.sleep(Intervel)  # Sleep for "Intervel" seconds before running again
        i += 1


    return sample

def Ltp_insertion(i, Ltp):

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Venu@5599',
        'database': 'mydb'
    }
    dbconnection = mysql.connector.connect(**db_config)
    print(dbconnection)
    cursor = dbconnection.cursor()
    insert_query = "INSERT INTO streamed_data (symbol, price, Exchange) VALUES (%s, %s, %s)"
    print(Ltp)
    # exit()
    data_to_insert = [Ltp['data']['tradingsymbol'], Ltp['data']['ltp'], Ltp['data']['exchange']]
    cursor.execute(insert_query, data_to_insert)

    # Commit the changes to the database
    dbconnection.commit()

def get_records(Table, NumberOfRecentRecords):

    DbConnection = Db_Connection()
    cusrsor = DbConnection.cursor()

    SelectQuery = "SELECT * FROM " + Table + " ORDER BY id DESC LIMIT " + str(NumberOfRecentRecords)
    print(SelectQuery)
    Records = cusrsor.execute(SelectQuery)

    return Records



def Db_Connection():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Venu@5599',
        'database': 'mydb'
    }
    return mysql.connector.connect(**db_config)