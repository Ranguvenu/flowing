import sys
sys.path.append('/var/www/html/myproject/')  
from smartConnect import SmartConnect 
import threading
import pyotp, time
from config import *

obj = SmartConnect(api_key=apikey)

data = obj.generateSession('V280771', 4562, pyotp.TOTP(token).now())
AUTH_TOKEN = data['data']['jwtToken']
refreshToken = data['data']['refreshToken']
FEED_TOKEN=obj.getfeedToken()
res = obj.getProfile(refreshToken)


"""
    Created on Monday Feb 2 2022

    @author: Nishant Jain

    :copyright: (c) 2022 by Angel One Limited
"""

from SmartApi.smartWebSocketV2 import SmartWebSocketV2

AUTH_TOKEN = 'Bearer eyJhbGciOiJIUzU-w'
API_KEY = 'qwert'
CLIENT_CODE = 'X123456'
FEED_TOKEN = '00998877'

correlation_id = "nishant_123_qwerty"
action = 0
mode = 3

token_list = [{"exchangeType": 1, "token":["2885"]}]

sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))


def on_open(wsapp):
    print("on open")
    sws.subscribe(correlation_id, mode, token_list)


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()


