import sys
sys.path.append('/var/www/html/myproject/')
from SmartApi import SmartConnect
import pyotp, time
from datetime import datetime
from SmartApi.smartWebSocketV2 import SmartWebSocketV2

from logzero import logger
from config import *
from lib import *


connecting_object = SmartConnect(api_key="yWjMIfbo")
data = connecting_object.generateSession('V280771', 4562, pyotp.TOTP(token).now())
history_date = "2024-06-03 11:25:00"
current_date = "2024-06-03 11:30:00"
dates = forword_testing(connecting_object, current_date, history_date)
