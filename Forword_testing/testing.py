# from optionslib import *
ss = {'token': '37095', 'price': 2790.0, 'optionname': 'BANKNIFTY12JUN2450700CE', 'shareprice': 186.0}

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


try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "BANKNIFTY12JUN2450700CE",
        "symboltoken": "37095",
        "transactiontype": "BUY",
        "exchange": "NFO",
        "ordertype": "MARKET",
        "producttype": "CARRYFORWARD",
        "duration": "DAY",
        "price": "0",
        "squareoff": 0,
        "stoploss": 0,
        "quantity": 45
        }
    # Method 1: Place an order and return the order ID
    orderid = obj.placeOrder(orderparams)

    orderid = obj.placeOrder(orderparams)
    logger.info(f"PlaceOrder : {orderid}")
    # Method 2: Place an order and return the full response
    response = obj.placeOrderFullResponse(orderparams)
    logger.info(f"PlaceOrder : {response}")
except Exception as e:
    logger.exception(f"Order placement failed: {e}")