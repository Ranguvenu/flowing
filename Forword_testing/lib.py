from datetime import datetime, timedelta
import pyotp, time, timedelta
from SmartApi import SmartConnect

from config import *
from Flower_filter import *
from orders_lib import *
def forword_testing(connection_object, current_time, history_time):
    connection_data = connection_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())

    i = 0
    while True:
        time.sleep(1)  # Sleep for "Intervel" seconds before running again

        history_time = next_times_giving(history_time)

        current_time = next_times_giving(current_time)

        try:

            params = recent_number_of_forwording_histories_params("NSE", "99926009", "FIVE_MINUTE", 6, 5, history_time)
            current_params = recent_number_of_forwording_histories_params("NSE", "99926009", "FIVE_MINUTE", 0, 5, current_time)

            history = connection_object.getCandleData(params)

            current_history = connection_object.getCandleData(current_params)


            try:
                current_history = connection_object.getCandleData(current_params)
            except Exception as e:
                print("In exeption: ")
                print('cjdnfjdfj2')

                connection_object=SmartConnect(api_key="yWjMIfbo")
                #login api callconnection_object
                data = connection_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
                # refreshToken= data['data']['refreshToken']
                print('pramsasansns:', current_params)
                print('object_object',connection_object.getCandleData(current_params))
                current_history = connection_object.getCandleData(current_params)
                print('current_history::::::', current_history)
                # continue

            Historion = recent_history_forflowing(history)

            try:
                current = current_flowing(current_history)
            except Exception as e:
                print('the error is:', e)

            if not current:
                print("this is current params:", current_params)
                print("this is current:", current)


            Historion.update(current)

            flowfilterv = flowfilter(Historion, current_params['todate'], connection_data, connection_object)
            flow_twov = flow_two(Historion, current_params['todate'], connection_data, connection_object)

            fourth_flowv = fourth_flow(Historion, current_params['todate'], connection_data, connection_object)
            high_fiveflowv = high_fiveflow(Historion, current_params['todate'], connection_data, connection_object)

            holdings = False
            # if flowfilterv or flow_twov or fourth_flowv or high_fiveflowv or holdings:
            sleep_time = next_fivemloop_inseconds()

            if sleep_time != 0:
                sell_atv = sell_at()
                start_time = time.time()
                while (time.time() - start_time) < sleep_time:
                    ltp_target_checking(connection_object, sell_atv)
                    time.sleep(5)
            elif sleep_time <= 0:
                sell_atv = sell_at()
                start_time = time.time()
                while (time.time() - start_time) < 300:
                    ltp_target_checking(connection_object, sell_atv)
                    time.sleep(5)



            i += 1
            print("after flow"+str(i))


            # Place your main function logic here that runs after the sleep period.
            print("Main loop is running.")
        except Exception as e:
            return {'history_date': history_time, 'current_date': current_time}
    return {'history_date':history_date, 'current_date':current_date}



def next_fivemloop_inseconds():
    local_time = time.localtime()
    current_time = int(time.strftime("%M", local_time))
    # print(time.strftime("%M", local_time))

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



def next_times_giving(begins="2024-04-15 15:25"):

    begins_dt_format = datetime.strptime(begins, "%Y-%m-%d %H:%M:%S")

    begins_unix = int(begins_dt_format.timestamp())
    reduced_unix = begins_unix + 5 * 60
    reduced_time = datetime.fromtimestamp(reduced_unix)
    formatted_date = reduced_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date



def recent_number_of_forwording_histories_params(exchange, symboltoken, interval, histories_count, candle_timeframe, history_time=False):
    local_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    into_past = candle_timeframe * histories_count*60
    times = recent_historion_timeline_forlive(candle_timeframe, into_past, history_time)


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




def recent_historion_timeline_forlive(interval = False, into_past=False, current_time=False, forlive_history=False):
    # Get current local time
    # uncomment for live

    # current_time = "2024-04-23 15:30:00"

    current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

    # If current minute is a multiple of 5
    if current_time.minute % interval == 0:

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




def recent_history_forflowing(response_data):
    formatted_data = {}

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


def current_flowing(response_data):
    formatted_data = {}
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




def ltp_target_checking(obj, sell_index_point = 48555):
    banknifty_ltp = obj.ltpData(Exchange= "NSE", Symbol= "BANKNIFTY", SymbolCode= "99926009")

    # if sell_index_point <= banknifty_ltp or (sell_index_point - banknifty_ltp) <= 15:
