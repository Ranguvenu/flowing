def order_testing(obj, order_details, transaction_type):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": order_details['optionname'],
            "symboltoken": order_details['token'],
            "transactiontype": transaction_type,
            "exchange": "NFO",
            "ordertype": "LIMIT",
            "producttype": "CARRYFORWARD",
            "duration": "DAY",
            "price": "0",
            "squareoff": 0,
            "stoploss": 0,
            "quantity": 15
            }
        # Method 1: Place an order and return the order ID
        orderid = obj.placeOrder(orderparams)

        orderid = obj.placeOrder(orderparams)
        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
    except Exception as e:
        print('error'+ e)