import pandas as pd
import sys

#x1 is Least recent closing price and x5 is most recent closing price and y1 current price
def strategy(x1, x2, x3, x4, x5, y1):
    if x1 > x2 > x3 < x4 < x1 < x5 and y1 > x1:
        print('ample text: Bull')




def check_buy_signal(current_price, recent_closing_prices, support_resistance_price):
    """
    Checks if the current price generates a buy signal based on the described strategy.

    Parameters:
    - current_price: Current price of the stock.
    - recent_closing_prices: List of the most recent 10 closing prices of the stock.
    - support_resistance_price: Static support/resistance price for the stock.

    Returns:
    - True if a buy signal is generated, False otherwise.
    """

    # Ensure we have at least 10 closing prices
    if len(recent_closing_prices) < 10:
        print("Need Least 10 Closing Prices")
        return False

    # Identify green candles (closing price higher than the open price)
    green_candles = [price for price in recent_closing_prices if price > 0]

    # Check if there are at least 2 green candles
    if len(green_candles) < 2:
        return False

    # Create a DataFrame with 'close' column using only green candles
    data = pd.DataFrame({'close': green_candles})

    # Initialize variables
    window_size = 2  # Number of candles to check for sideways movement
    fluctuation_threshold = 0.002  # 0.2% fluctuation threshold
    move_down_threshold = 0.002  # 0.2% move down threshold

    # Extract relevant window of data
    window_data = data.head(window_size)

    # Calculate price fluctuations in the window
    price_fluctuations = window_data['close'].pct_change()

    # Check if the stock moves sideways with fluctuation under 0.2%
    if all(abs(fluctuation) < fluctuation_threshold for fluctuation in price_fluctuations):
        # Check if the stock comes down about 0.4%
        if price_fluctuations.sum() < -move_down_threshold:
            # Find the highest closing price in the window
            highest_closing_price = window_data['close'].max()

            # Check if the stock comes back and crosses the highest closing price near the support/resistance level
            if current_price > highest_closing_price and current_price > support_resistance_price:
                # Buy signal identified
                return True

    return False


def SupportResistance(BeginsAt, EndsAt):
    records = []

    SupportResistance = BeginsAt

    while SupportResistance <= EndsAt:
        records.append(round(SupportResistance, 3))
        #Support/Resistance for every 0.5% of priveous support/Resistance
        SupportResistance = SupportResistance * 1.005
    return records


# def checkcolor():
    # save the record in db with "status" is green or wread
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


def flow_two(payload):
    captured_output = sys.stdout = sys.stderr = open('data.txt', 'a')


    # # flow_one -stage_one

    if payload['current_green'] and payload['a_one_green'] and payload['a_two_wread'] and payload['a_two_opens'] > payload['a_one_closing'] and payload['a_two_opens'] < payload['current_closing']:

        print("flow_two -stage_one")
        # flow_two_one --stage-two-start

        if payload['a_three_wread'] and payload['a_three_opens'] < payload['current_closing']:
            print("flow_two_one --stage_two")
        # flow_two_two --stage_two
        if payload['a_three_wread'] and payload['a_three_opens'] > payload['current_closing']:
            print("flow_two_two --stage_two falsy")
        # flow_two_three --stage_two

        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three")
        # flow_two_four --stage_two
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four")
        # flow_two_five --stage_two
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_two")

        # flow_two_one ---stage_three-starts
        if payload['a_three_wread'] and payload['a_three_opens'] < payload['current_closing']:
            print("flow_two_one --stage_two -copied")
            # flow_two_one_one ---stage_three-starts

            #                  approx
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_one_one ---stage_three")
            # flow_two_one_two ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_two_one_two ---stage_three")
            # flow_two_one_three ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_one_three ---stage_three")
            # flow_two_one_four ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] == payload['a_two_closing']:
                print("flow_two_one_four ---stage_three")
            # flow_two_one_five ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_one_five ---stage_three")
            # flow_two_one_six ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_two_one_six ---stage_three")

        # flow_two_three ---stage_three -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_three_starts -copied")
            # flow_two_three_one ---stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_two_closing']:
                print("flow_two_three_one ---stage_three")
            # flow_two_three_two ---stage_three
            if payload['a_one_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_three_two ---stage_three")
            # flow_two_three_three ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_three_three ---stage_three")
            # flow_two_three_four ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_three_four ---stage_three")

        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_four_one --stage_three")
            # flow_two_four_two --stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_four_two --stage_three")
            # flow_two_four_three --stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_four_three --stage_three")
            # flow_two_four_four --stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_four_four --stage_three")

        # flow_two_five --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_five --stage_three_starts -copied")

            # flow_two_five_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_five_one --stage_three_starts")
            # flow_two_five_two --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_five_two --stage_three")
            # flow_two_five_three --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_five_three --stage_three")
            # flow_two_five_four --stage_three
            if payload['a_four_green'] and payload['a_four_opens'] < payload['current_closing'] and payload['a_four_opens'] > payload['a_three_closing']:
                print("flow_two_five_four --stage_three")
            # flow_two_five_five --stage_three
            if payload['a_four_green'] and payload['a_four_opens'] > payload['current_closing']:
                print("flow_two_five_five --stage_three")
        
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_three_starts_for_four --copied2")
            # flow_two_three_one ---stage_three_for_four -copied
            print("flow_two_three_one ---stage_four_starts -copied ")
            # flow_two_three_one_one ----stage_four starts
            if payload['a_five_green']:
                print("flow_two_three_one_one ----stage_four started")
            # flow_two_three_one_two ----stage_four
            if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing']:
                print("flow_two_three_one_two ----stage_four")
            # flow_two_three_one_three ----stage_four
            if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                print("flow_two_three_one_three ----stage_four")
            # flow_two_three_one_four ----stage_four
            if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                print("flow_two_three_one_four ----stage_four")
            # flow_two_three_one_five ----stage_four
            if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                print("flow_two_three_one_five ----stage_four")
            # flow_two_three_one_six ----stage_four
            if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                print("flow_two_three_one_six ----stage_four")
            # flow_two_three_one_seven ----stage_four
            if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                print("flow_two_three_one_seven ----stage_four")


    #flow_two_one_one series going to come here -------------------------------------------"""




                # flow_two_three_one_one stage_four_starts

        # flow_two_three_two ----stage_four_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_four_starts -copied")
            # flow_two_three_two ---stage_three
            if payload['a_one_green'] and payload['a_four_opens'] < payload['a_two_closing']:
                print("flow_two_three_two ---stage_four_starts")

                # flow_two_three_two_one ---stage_four_starts -copied
                if payload['a_five_green']:
                    print("flow_two_three_two_one _starts_started")
                # flow_two_three_two_two
                if payload['a_five_wread'] and payload['a_five_wread'] == payload['a_four_closing']:
                    print("flow_two_three_two_two ---stage_four")
                # flow_two_three_two_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_three_two_three ---stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_three_two_four ---stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_two_five ---stage_four")
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_three_two_six ---stage_four")

        # flow_two_three_two ----stage_four_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_four_starts -copied")
            # flow_two_three_three ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] == payload['a_three_closing']:
                print("flow_two_three_three ---stage_four_starts - copied")
                # flow_two_three_three_one ------stage_four_starts
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_three_three_one ---stage_four_started")
                # flow_two_three_three_two ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_three_closing']:
                    print("flow_two_three_three_two ---stage_four")
                # flow_two_three_three_three ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_three_three_three ---stage_four")
                # flow_two_three_three_four ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_two_three_three_four ---stage_four")
                # flow_two_three_three_five ---stage_four
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_two_closing'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_three_three_five ---stage_four")
                # flow_two_three_three_six ---stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_three_six ---stage_four")
                # flow_two_three_three_seven ---stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_three_three_seven ---stage_four")

        # flow_two_three_two ----stage_four_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] > payload['a_two_closing']:
            print("flow_two_three ---stage_four_starts -copied")
            # flow_two_three_four ---stage_three
            if payload['a_four_wread'] and payload['a_four_opens'] > payload['a_three_closing'] and payload['a_four_opens'] < payload['current_closing']:
                print("flow_two_three_four ---stage_three")
                # flow_two_three_four_one ---stage_four_starts
                if payload['a_five_green'] and payload['a_five_opens'] > payload['a_four_closing']:
                    print("flow_two_three_four_one ---stage_four_started")
                # flow_two_three_four_two ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_three_four_two ---stage_three")
                # flow_two_three_four_three ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_two_closing']:
                    print("flow_two_three_four_three ---stage_three")
                # flow_two_three_four_four ---stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_three_four_four ---stage_three")
                # flow_two_three_four_five ---stage_three
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_two_closing']:
                    print("flow_two_three_four_five ---stage_three")





        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_one --stage_three_starts
            if payload['a_four_green']:
                print("flow_two_four_one --stage_three -copied")
                # flow_two_four_one_one ----stage_four_starts
                if payload['a_five_green']:
                    print("#flow_two_four_one_one ----stage_four_started")
                # flow_two_four_one_two ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_one_two ----stage_four")
                # flow_two_four_one_three ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_one_three ----stage_four")
                # flow_two_four_one_four ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['a_three_closing']:
                    print("flow_two_four_one_four ----stage_four")
                # flow_two_four_one_five ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_three_closing']:
                    print("flow_two_four_one_five ----stage_four")
                # flow_two_four_one_six ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_three_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_four_one_six ----stage_four")
                # flow_two_four_one_seven ----stage_four
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_four_one_seven ----stage_four")

        # flow_two_four --stage_three_starts -copied
        if payload['a_three_green'] and payload['a_three_opens'] < payload['a_two_closing']:
            print("flow_two_four --stage_three_starts -copied")

            # flow_two_four_two --stage_three_starts
            if payload['a_four_wread'] and payload['a_four_opens'] < payload['a_three_closing']:
                print("flow_two_four_two --stage_three_starts_for_four - copied")
                # flow_two_four_two_one --stage_four
                if payload['a_five_green'] and payload['a_two_opens'] < payload['a_four_closing']:
                    print("flow_two_four_two_one --stage_three_started")
                # flow_two_four_two_two --stage_three
                if payload['a_five_green'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_two_two --stage_three")
                # flow_two_four_three --stage_three
                if payload['a_five_green'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_three --stage_three")
                # flow_two_four_two_four --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] < payload['a_four_closing']:
                    print("flow_two_four_two_four --stage_three")
                # flow_two_four_two_five --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] == payload['a_four_closing']:
                    print("flow_two_four_two_five --stage_three")
                # flow_two_four_two_six --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['a_four_closing'] and payload['a_five_opens'] < payload['current_closing']:
                    print("flow_two_four_two_six --stage_three")
                # flow_two_four_two_seven --stage_three
                if payload['a_five_wread'] and payload['a_five_opens'] > payload['current_closing']:
                    print("flow_two_four_two_seven --stage_three")
        
    else:
        print("It's out of second flow")
