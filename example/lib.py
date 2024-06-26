#Operational Functions
import sys
sys.path.append('/var/www/html/myproject/')  
from smartapi import SmartConnect
from config import *
import pyotp, time, timedelta
import mysql.connector
from datetime import datetime, timedelta
from Strategy import *

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
    cursor = dbconnection.cursor()
    insert_query = "INSERT INTO streamed_data (symbol, price, Exchange) VALUES (%s, %s, %s)"
    # print(Ltp)
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
def round_up_to_nearest_five(x):
    return 5 * ((x + 4) // 5)
    
def StreamLTP_two(Exchange, Symbol, SymbolCode, Intervel, connection):
    i = 0
    while True:
        Ltp = connection.ltpData(Exchange, Symbol, SymbolCode)
        print(Ltp)
        print('goodthings take time')
        Ltp_insertion(i, Ltp)
        current_time_struct = time.localtime()
        print("Last Trading Price: ", Ltp['data']['ltp'], "@",  time.strftime("%H:%M:%S", current_time_struct))
        
        # Calculate the time until the next multiple of five minutes
        current_minute = current_time_struct.tm_min
        next_iteration_minute = round_up_to_nearest_five(current_minute)
        minutes_to_sleep = (next_iteration_minute - current_minute) % 60
        if minutes_to_sleep == 0:
            minutes_to_sleep = 5
        print(minutes_to_sleep) 
        time.sleep(minutes_to_sleep * 60)  # Sleep until the next multiple of five minutes
        i += 1
def StreamLTP_twotwo(Exchange, Symbol, SymbolCode, Intervel, connection):
    i = 0
    while True:
        Ltp = connection.ltpData(Exchange, Symbol, SymbolCode)
        print(Ltp)
        print('goodthings take time')
        Ltp_insertion(i, Ltp)
        current_time_struct = time.localtime()
        print("Last Trading Price: ", Ltp['data']['ltp'], "@",  time.strftime("%H:%M:%S", current_time_struct))
        
        # Calculate the time until the next multiple of five minutes
        current_minute = current_time_struct.tm_min
        next_iteration_minute = round_up_to_nearest_five(current_minute)
        minutes_to_sleep = (next_iteration_minute - current_minute) % 60
        if minutes_to_sleep == 0:
            minutes_to_sleep = 5
        print(minutes_to_sleep) 
        time.sleep(minutes_to_sleep * 60)  # Sleep until the next multiple of five minutes
        i += 1


def recent_history_forflowing(response_data):
    formatted_data = {}

    print(response_data['data'])

    response_data['data'] = list(reversed(response_data['data']))

    i = 1
    for item in response_data['data']:

        timestamp = item[0]
        opening_price = item[1]
        highest_price = item[2]
        lowest_price = item[3]
        closing_price = item[4]
        volume = item[5]  # Assuming this is the volume
        spell = spell_integer(i)

        formatted_data[f'timestamp_{spell}'] = timestamp
        formatted_data[f'opening_price_{spell}'] = opening_price
        formatted_data[f'highest_price_{spell}'] = highest_price
        formatted_data[f'lowest_price_{spell}'] = lowest_price
        formatted_data[f'closing_price_{spell}'] = closing_price
        formatted_data[f'volume_{spell}'] = volume
        formatted_data[f'a_{spell}_green'] = True if closing_price > opening_price else False
        formatted_data[f'a_{spell}_wread'] = True if closing_price < opening_price else False
        formatted_data[f'a_{spell}_opens'] = opening_price
        formatted_data[f'a_{spell}_open'] = opening_price
        formatted_data[f'a_{spell}_opening'] = opening_price
        formatted_data[f'a_{spell}_closes'] = closing_price
        formatted_data[f'a_{spell}_closing'] = closing_price
        formatted_data[f'a_{spell}'] = closing_price
        i += 1
        

    return formatted_data
        # Display the formatted data
        # for data_point in formatted_data:
        #     print(data_point)

def current_flowing(response_data):
    formatted_data = {}

    print("response_data:", response_data['data'])
    response_data['data'] = list(reversed(response_data['data']))

    i = 1
    for item in response_data['data']:

        timestamp = item[0]
        opening_price = item[1]
        highest_price = item[2]
        lowest_price = item[3]
        closing_price = item[4]
        volume = item[5]  # Assuming this is the volume

        formatted_data['timestamp_current'] = timestamp
        formatted_data['opening_price_current'] = opening_price
        formatted_data['highest_price_current'] = highest_price
        formatted_data['lowest_price_current'] = lowest_price
        formatted_data['closing_price_current'] = closing_price
        formatted_data['volume_current'] = volume
        formatted_data['current_green'] = True if closing_price > opening_price else False
        formatted_data['current_wread'] = True if closing_price < opening_price else False
        formatted_data['current_opens'] = opening_price
        formatted_data['current_opening'] = opening_price
        formatted_data['current_closes'] = closing_price
        formatted_data['current_closing'] = closing_price
        formatted_data['current'] = closing_price
        i += 1
        

    return formatted_data
        # Display the formatted data
        # for data_point in formatted_data:
        #     print(data_point)




#spell integer
def spell_integer(n):
    if n < 20:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n]
    if n < 100:
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10-2] + ('_' + spell_integer(n%10) if n % 10 else '')
    if n < 1000:
        return spell_integer(n//100) + '_hundred_' + spell_integer(n%100) if n % 100 else ''
    for i, j in enumerate(('thousand', 'million', 'billion', 'trillion'), 1):
        if n < 1000 ** (i + 1):
            return spell_integer(n // 1000 ** i) + '_' + j + '_' + spell_integer(n % 1000 ** i) if n % 1000 ** i else ''
    return ''


def recent_number_of_histories_params(exchange, symboltoken, interval, histories_count, candle_timeframe, history_date=False, forlive = False):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    into_past = candle_timeframe * histories_count*60
    if forlive:
        times = recent_historion_timeline(candle_timeframe, into_past, history_date)
    else:
        times = recent_historion_timeline_forlive(candle_timeframe, into_past, history_date)


    # print(times['startime_from_readable'])
    # exit()
    history_params = {
        "exchange": f"{exchange}",
        "symboltoken": f"{symboltoken}",
        "interval": f"{interval}",
        # "fromdate": "2024-04-15 11:15",
        "fromdate": times['startime_to_readable'],
        "todate":times['startime_from_readable']
        # "todate": "2024-04-15 11:25"
    }
    return history_params

def recent_number_of_histories_params_forlive(exchange, symboltoken, interval, histories_count, candle_timeframe, history_date=False, live_history = False):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    # history_date = False
    into_past = candle_timeframe * histories_count*60
    times = recent_historion_timeline(candle_timeframe, into_past, history_date, live_history)
    # print(times)
    # exit()
    # if live_history:
    #     print(times)
    #     exit()

    history_params = {
        "exchange": f"{exchange}",
        "symboltoken": f"{symboltoken}",
        "interval": f"{interval}",
        # "fromdate": "2024-04-15 11:15",
        "fromdate": times['startime_to_readable'],
        "todate":times['startime_from_readable']
        # "todate": "2024-04-15 11:25"
    }
    return history_params
def recent_number_of_histories_params_two(exchange, symboltoken, interval, histories_count, candle_timeframe):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    into_past = candle_timeframe * histories_count*60
    times = recent_historion_timeline(candle_timeframe, into_past)
    # print(times['startime_from_readable'])
    # exit()
    history_params = {
        "exchange": f"{exchange}",
        "symboltoken": f"{symboltoken}",
        "interval": f"{interval}",
        # "fromdate": "2024-04-15 11:15",
        "fromdate": times['startime_to_readable'],
        "todate":times['startime_from_readable']
        # "todate": "2024-04-15 11:25"
    }
    return history_params


def recent_historion_timeline_forlive(interval = False, into_past=False, current_time=False, forlive_history = False):
    # Get current local time
    # uncomment for live

    # current_time = "2024-04-23 15:30:00"
    if current_time == False:
        local_time = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    # current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

    #the below two lines code is only for last holidays
    # print(current_time)
    # exit()
    # current_time = "2024-04-16 11:25:00"
    # print('datatime doesnt match', current_time)
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    # print('dsssssssssssssss:', current_time)
    # exit()
    # print(type(current_time))
    # exit()
    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        # print(type(current_time))
        # exit()
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60)

        past_time_starts_unix = time_correction - into_past
        time_correction = datetime.fromtimestamp(time_correction)

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")

        
        startime_readble = time_correction.strftime("%Y-%m-%d %H:%M")


        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')

        time_correction = (time.mktime(unix) - minutes_diff*60 - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60)

        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


    # return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}





def recent_historion_timeline(interval = False, into_past=False, current_time=False, forlive_history = False):
    # Get current local time
    # uncomment for live

    # current_time = "2024-04-23 15:30:00"
    if current_time == False:
        local_time = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    # current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

    #the below two lines code is only for last holidays
    # print(current_time)
    # exit()
    # current_time = "2024-04-16 11:25:00"
    # print('datatime doesnt match', current_time)
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    # print('dsssssssssssssss:', current_time)
    # exit()
    # print(type(current_time))
    # exit()
    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        # print(type(current_time))
        # exit()
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60 -600)

        past_time_starts_unix = time_correction - into_past
        time_correction = datetime.fromtimestamp(time_correction)

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")

        
        startime_readble = time_correction.strftime("%Y-%m-%d %H:%M")


        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')

        time_correction = (time.mktime(unix) - minutes_diff*60 - interval*60) if forlive_history else (time.mktime(unix) - minutes_diff*60 -600)

        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


    # return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


def recent_historion_timeline_two_for_currentpricess(interval = False, into_past=False):
    # Get current local time
    
    local_time = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M", local_time)
    # current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")

    #the below two lines code is only for last holidays
    # current_time = "2024-04-16 11:25:00"
    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")


    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - minutes_diff*60)
        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")



        startime_readble = current_time.strftime("%Y-%m-%d %H:%M")

        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}

    else:
        # Find the closest past multiple of 5
        minutes_diff = current_time.minute % interval
        unix = time.strptime(str(current_time), '%Y-%m-%d %H:%M:%S')
        time_correction = (time.mktime(unix) - minutes_diff*60)
        past_time_starts_unix = time_correction - into_past

        past_time_starts_unix_readable = datetime.fromtimestamp(past_time_starts_unix)
        past_time_starts_unix_readable = past_time_starts_unix_readable.strftime("%Y-%m-%d %H:%M")
        startime_readble = datetime.fromtimestamp(time_correction)

        startime_readble = startime_readble.strftime("%Y-%m-%d %H:%M")
        return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}


    # return {'startime_from_readable' : startime_readble, 'startime_from_unix': time_correction, 'startime_to_unix': past_time_starts_unix, 'startime_to_readable': past_time_starts_unix_readable}



def next_times_giving(begins="2024-04-15 15:25"):
    print("inttitiuti:", begins)
    begins = into_the_yesterday(begins)
    beginsstrinhg = type(begins)
    if beginsstrinhg != str:
        print('chnaged ormat:',begins)
        print('nd its type:', type(begins))
        # exit()
    else:
        print('chnaged ormat:',begins)
        print('nd its type:', type(begins))
        # exit()
    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")
    # print(begins_dt_format)
    # exit()
    begins_unix = int(begins_dt_format.timestamp())
    reduced_unix = begins_unix - 5 * 60
    reduced_time = datetime.fromtimestamp(reduced_unix)
    formatted_date = reduced_time.strftime("%Y-%m-%d %H:%M:%S")

    print(formatted_date)
    return formatted_date   

# To save the result data in file
def save_data(data):
    if data is not None:
        with open('data_two.txt', 'a') as f:  # 'a' to append data to the file
            f.write(str(data) + '\n')
    else:
        print("Data is None, cannot save to file.")



def flowing_through_history(obj, current_date=False, history_starts=False):

    history_date = "2024-04-16 15:20:00"
    current_date = "2024-04-16 15:25:00"
    i = 0
    while True:
        time.sleep(2)  # Sleep for "Intervel" seconds before running again

        history_date = next_times_giving(history_date)

        current_date = next_times_giving(current_date)
        # print("timegiver H:", history_date)
        # print("timegiver C:", current_date)
        # exit()
        params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 10, 5, history_date)
        print("params:",params)
        current_params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_date)
        print("params2:",current_params)
        # obj=SmartConnect(api_key="yWjMIfbo")

        history = obj.getCandleData(params)
        print("historyyyyyyyyy:", history)

        # current_history = obj.getCandleData(current_params)
        try:
            current_history = obj.getCandleData(current_params)
            if current_history['errorCode'] == 'AG8001':
                obj=SmartConnect(api_key="yWjMIfbo")
                #login api call
                data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
                # refreshToken= data['data']['refreshToken']
                current_history = obj.getCandleData(current_params)

        except Exception as e:
            obj=SmartConnect(api_key="yWjMIfbo")
            #login api call
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
            # refreshToken= data['data']['refreshToken']
            current_history = obj.getCandleData(current_params)

        print("the seee---")
        # while True:
        #     times_forhistory = 
        Historion = recent_history_forflowing(history)

        current = current_flowing(current_history)

        if not current:
            print("this is current params:", current_params)
            print("this is current:", current)
            print("current_raw:", current_history['errorCode'])


        Historion.update(current)
        flowfilter(Historion)

        save_tofile = flowfilter(Historion)
        # print("type of response:", type(Historion))
        # exit()
        save_data(save_tofile)
        i += 1
        print("after flow"+str(i))
        time.sleep(2)  # Sleep for "Intervel" seconds before running again

def flowing_through_history_two(obj, current_date=False, history_date=False):


    i = 0
    while True:
        time.sleep(2)  # Sleep for "Intervel" seconds before running again

        history_date = next_times_giving(history_date)

        current_date = next_times_giving(current_date)

        params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 10, 5, history_date)
        print("params:",params)
        current_params = recent_number_of_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_date)
        print("params2:",current_params)

        history = obj.getCandleData(params)
        print("historyyyyyyyyy:", history)

        try:
            current_history = obj.getCandleData(current_params)


        except Exception as e:
            obj=SmartConnect(api_key="yWjMIfbo")
            #login api call
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
            # refreshToken= data['data']['refreshToken']
            current_history = obj.getCandleData(current_params)

        print("the seee---")


        Historion = recent_history_forflowing(history)


        try:
            current = current_flowing(current_history)
        except Exception as e:
            print('the error is:', e)



        if not current:
            print("this is current params:", current_params)
            print("this is current:", current)


        Historion.update(current)
        print("current history at:", current_params['todate'])
        flowfilter(Historion, current_params['todate'])
        save_tofile = flow_two(Historion, current_params['todate'])

        print("type of response:", Historion)
        save_data(save_tofile)
        i += 1
        print("after flow"+str(i))
        time.sleep(2)  # Sleep for "Intervel" seconds before running again
    return {'history_date':history_date, 'current_date':current_date}



def stream_into_flow(obj):
    i = 0
    while True:
        # captured_outputs = sys.stdout = sys.stderr = open('data.txt', 'a')



        # time.sleep(2)  # Sleep for "Intervel" seconds before running again
        live_history_params = recent_number_of_histories_params_forlive("NSE", "99926009", "FIVE_MINUTE", 12, 5, False, False)
        print("live_history_params:",live_history_params)

        current_params = recent_number_of_histories_params_forlive("NSE", "99926009", "FIVE_MINUTE", 0, 5, False, True)

        history = obj.getCandleData(live_history_params)
        print("historyyyyyyyyy:", history)

        # current_history = obj.getCandleData(current_params)
        try:
            current_history = obj.getCandleData(current_params)
            print("at issue:", current_history)
        except Exception as e:
            obj=SmartConnect(api_key="yWjMIfbo")
            #login api call
            data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
            current_history = obj.getCandleData(current_params)

        print("the seee---")

        Historion = recent_history_forflowing(history)
        # print(current_history)
        # exit()
        current = current_flowing(current_history)
        print("current data:",current_flowing)
        if not current:
            print("this is current params:", current_params)
            print("this is current:", current)


        Historion.update(current)
        # print("Total live text:",Historion)
        # exit()
        flowfilter(Historion, current_params['todate'])
        flow_two(Historion, current_params['fromdate'])



        save_tofile = flow_two(Historion)
        # next_fivemloop_insecondss = next_fivemloop_inseconds()
        save_data(save_tofile)
        i += 1
        print("after flow"+str(i))

        # time.sleep(next_fivemloop_inseconds())  # Sleep for "Intervel" seconds before running again
        if next_fivemloop_inseconds() != 0:
            time.sleep(next_fivemloop_inseconds())  # Sleep for "Intervel" seconds before running again
        elif next_fivemloop_inseconds() <= 0:
            time.sleep(300)




def next_fivemloop_inseconds():
    local_time = time.localtime()
    current_time = int(time.strftime("%M", local_time))
    # print(time.strftime("%M", local_time))
    # exit()
    # Sample next_time
    next_time = time.strftime("%Y-%m-%d %H:%M", local_time)

    if current_time % 5 != 0:
        current_time = (current_time // 5 + 1) * 5

    # Split next_time into date and time components
    date_part, time_part = next_time.split()

    # Replace the minute part with current_time
    new_time = time_part[:3] + str(current_time)

    # Reconstruct the modified next_time
    modified_next_time = date_part + ' ' + new_time
    print("Next History time:", modified_next_time)
    modified_next_time = datetime.strptime(modified_next_time, "%Y-%m-%d %H:%M")
    modified_next_time = int(modified_next_time.timestamp())
    now_the_time = time.time()
    now_the_time = int(now_the_time - (now_the_time % 60))
    next_loop_inseconds = modified_next_time - now_the_time
    if next_loop_inseconds <= 0:
        return 0
    return next_loop_inseconds



def into_the_yesterday(begins="2024-04-15 09:15:00"):
    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")
    
    # Extract time component from begins_dt_format
    time_component = begins_dt_format.time()

    # Define the target times for comparison
    # target_time_1 = time(9, 15, 0)
    # target_time_2 = time(9, 10, 0)
    target_time_1 = datetime.strptime("09:15:00", "%H:%M:%S")
    target_time_1 = target_time_1.time()
    target_time_2 = datetime.strptime("09:10:00", "%H:%M:%S")
    target_time_2 = target_time_2.time()
    # print(target_time_1.time())
    # exit()

    # If time is exactly 9:15, return yesterday's 15:35
    if time_component == target_time_1:
        # Calculate yesterday's date by subtracting 1 day
        yesterday = begins_dt_format - timedelta(days=1)
        # Create a new datetime object for yesterday's 15:35
        yesterday = datetime(year=yesterday.year, month=yesterday.month, day=yesterday.day, hour=15, minute=35, second=0)

        yesterday = datetime.strftime(yesterday, "%Y-%m-%d %H:%M:%S")
        return yesterday
    # If time is exactly 9:10, return yesterday's 15:30
    elif time_component == target_time_2:
        # Calculate yesterday's date by subtracting 1 day
        yesterday = begins_dt_format - timedelta(days=1)
        # Create a new datetime object for yesterday's 15:30
        yesterday = datetime(year=yesterday.year, month=yesterday.month, day=yesterday.day, hour=15, minute=30, second=0)
        yesterday = datetime.strftime(yesterday, "%Y-%m-%d %H:%M:%S")

        return yesterday
    else:
        return begins  # Return False if neither condition is met
