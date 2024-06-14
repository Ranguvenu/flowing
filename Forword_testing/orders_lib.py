def option_order(obj, order_details, transaction_type="BUY"):
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
        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
    except Exception as e:
        print('error'+ e)




def sell_at(current_index_at = 48555):
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


def option_order_record(obj, order_details, transaction_type="BUY", current_index=49515):
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
        # Method 2: Place an order and return the full response
        response = obj.placeOrderFullResponse(orderparams)
        logger.info(f"PlaceOrder : {response['data']['script']}")

        sell_index = sell_at(current_index)
        # DB table name is order_records
        # response['data']['script'] is symbol
        # response['data']['orderid'] is orderid
        # sell_index is sell_index
        # current_index is nse_index
        # symbol, orderid, sell_index, nse_index are db table fields
        # there will be bought_at and lot_price extra columns, need to pass None
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Venu@5599',
            'database': 'mydb'
        }

        insert_data = (
            response['data']['script'],
            response['data']['orderid'],
            sell_index,
            current_index,
            15,  # bought_at
            15   # lot_price
        )

        # Insert the data into the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO order_records (symbol, orderid, sell_index, nse_index, bought_at, lot_price)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, insert_data)
        conn.commit()
        cursor.close()
        conn.close()
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        print('error:', e)
