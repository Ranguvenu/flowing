from logzero import logger


def order_testing(obj, order_details, transaction_type="BUY"):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": order_details['optionname'],
            "symboltoken": order_details['token'],
            "transactiontype": transaction_type,
            "exchange": "NFO",
            "ordertype": "MARKET",
            "producttype": "CARRYFORWARD",
            "duration": "DAY",
            "price": "0",
            "squareoff": 0,
            "stoploss": 0,
            "quantity": 15
            }

        orderid = obj.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
        logger.info(f"PlaceOrder : {response}")
    except Exception as e:
        print('error'+ e)



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