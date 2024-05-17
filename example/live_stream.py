import sys
sys.path.append('/var/www/html/myproject/')  
# package import statement
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
from config import *
import pyotp, time
from lib import *
from Symbols import *
from Strategy import *
from datetime import datetime

from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger

# Define a global variable to store the response
response_data = None
tokens = []
option_ltp = []
i = 0
best_option = None
tokens_withnames = None
def pickup_fromstream(obj=False,data=False):
    global tokens_withnames
    if obj== False or data==False:
        obj=SmartConnect(api_key="yWjMIfbo")
        #login api call
        data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
    # refreshToken= data['data']['refreshToken']

    AUTH_TOKEN = data['data']['jwtToken']
    API_KEY = "yWjMIfbo"
    CLIENT_CODE = "V280771"
    FEED_TOKEN = data['data']['feedToken']
    correlation_id = "abc123"
    action = 1
    mode = 1
    ranger_options =  ranger_options_tokens(obj)
    tokens_withnames = ranger_options[1]
    token_collection =ranger_options[0]

    #retry_strategy=0 for simple retry mechanism
    sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN,max_retry_attempt=0, retry_strategy=0, retry_delay=10, retry_duration=30)
    

    # Initialize tokens and option_ltp outside the function

    def on_data(wsapp, message):
        global response_data
        global received_tokens
        global tokens
        global option_ltp
        global i
        global best_option

        logger.info("Ticks: {}".format(message))

        response_data = message

        token = response_data['token']  # Assuming the key for token is 'token'
        last_traded_price = response_data['last_traded_price']  # Assuming the key for last traded price is 'last_traded_price'
        if response_data['token'] not in tokens:
            print("in appending:")
            tokens.append(token)
            option_ltp.append({token: last_traded_price/100})
            i+=1
            if i >= 11:
                print('option_ltplist:', option_ltp)
                close_connection()
                # print("best option",best_option_fromlive(option_ltp))
                print('token names:', tokens_withnames)
                best_option =  best_option_fromlive(option_ltp, tokens_withnames)
        elif(response_data['token'] == 41615):
            # If token repeats, close the connection
            print("in appending:elseing")

            close_connection()
            print("best option",best_option_fromlive(option_ltp))
            return best_option_fromlive(option_ltp)



    # Initialize received_tokens as an empty set

    def on_control_message(wsapp, message):
        logger.info(f"Control Message: {message}")
        # print('LTPLTP:',message['message'])


    def on_open(wsapp):
        logger.info("on open")
        some_error_condition = False
        if some_error_condition:
            error_message = "Simulated error"
            if hasattr(wsapp, 'on_error'):
                wsapp.on_error("Custom Error Type", error_message)
        else:
            sws.subscribe(correlation_id, mode, token_collection)

    def on_error(wsapp, error):
        logger.error(error)

    def on_close(wsapp):
        logger.info("Close")

    def close_connection():
        sws.close_connection()

    # Assign the callbacks.
    sws.on_open = on_open
    sws.on_data = on_data
    sws.on_error = on_error
    sws.on_close = on_close
    sws.on_control_message = on_control_message

    sws.connect()
    close_connection()

    return best_option

# Add your remaining code here


# print("from live:",pickup_fromstream())