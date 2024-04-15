import pandas as pd

#x1 is Least recent closing price and x5 is most recent closing price and y1 current price
def strategy(x1, x2, x3, x4, x5, y1):
    if x1 > x2 > x3 < x4 < x1 < x5 and y1 > x1:
        print('ample text: Bull')



# if x1 > x2 > x3 < x4 < x1 < x5 and y1 > x1:
#     print('ample text: Bull')
        


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

# Example usage within a while loop:
# current_price = ...  # Get current price
# recent_closing_prices = [...]  # Get most recent 10 closing prices
# sr_price = ...  # Provide static support/resistance price

# Check for buy signal
# if check_buy_signal(current_price, recent_closing_prices, sr_price):
#     print("Buy Signal Detected!")
# else:
#     print("No Buy Signal.")


def SupportResistance(BeginsAt, EndsAt):
    records = []

    SupportResistance = BeginsAt

    while SupportResistance <= EndsAt:
        records.append(round(SupportResistance, 3))
        #Support/Resistance for every 0.5% of priveous support/Resistance
        SupportResistance = SupportResistance * 1.005
    return records

# def TestStrategy():
#     Current = 'Current'
#     Green = "Green"
#     Red = "Red"
#     FirstRecent = ''
#     SecondRecent = ''
#     ThirdRecent = ''
#     #need to add "If current is green" Condition
#     if Current  > FirstRecent and not FirstRecent > Current:
#         if SecondRecent == Green and ThirdRecent == Red and 

# def checkcolor():
    # save the record in db with "status" is green or wread

def flowfilter():
    current_closing = "Current price"
    # "a" is a past prices, a1 is most recent price

    a_one = 'most recent'
    a_one_green = True
    a_two = 'Second Recent'
    a_two_green = True
    a_three = 'Third Recent'
    a_three_open = 'three'
    a_four = 'Fourth Recent'
    a_three_wread = True
    a_three_opens = True
    a_three_green = True
    a_two_open = True
    current_green = True
    a_two_closes = True
    a_three_closes  = True
    #Begins at top
    if current_green and current_closing > a_one and a_one_green and a_one > a_two and a_two_green:

        #flow_one-stage-one
        if a_three_wread and a_three_opens > a_two and a_three_open < a_one:
            print("flow_one_one")
        
        if a_three_wread and a_three_opens > current_closing:
            print("flow_one_two")
        
        if  a_three_wread and a_three_opens > a_one and a_three_opens < current_closing and a_three_opens > a_one_closes:
            print("flow_one_three")
        if a_three_green and a_three_opens < a_two_open and a_three_closes < a_two_closes:
            print("flow_one_four")

        if a_three_wread and a_three_opens < a_two_closes:
            print("flow_one_five")

        #---------------------------------------------------------------------------
            
             #flow_one_four    --stage_two
        a_four_wread = True
        a_four_opens = True 
        a_one_closes = True
        a_four_green  = True
        a_four_closing = True
        if a_three_green and a_three_opens < a_two_open and a_three_closes < a_two_closes:
            print("flow_one_four copied")
            if a_four_wread and a_four_opens > current_closing:
                print("flow_one_four_one")
            if a_four_wread and a_four_opens < a_three_closes:
                print("flow_one_four_two")
            if a_four_wread and a_four_opens < a_two_closes and a_four_opens > a_three_closes:
                print("flow_one_four_three")
            if a_four_wread and a_four_opens < a_one_closes and a_four_opens > a_two_closes:
                print("flow_one_four_four")

            if a_four_wread and a_four_opens > a_one_closes and a_four_opens < current_closing:
                print("flow_one_four_five  --------- signal might come from here")    

            if a_four_green and a_four_opens < a_three_opens and a_four_closing < a_three_closes:
                print("flow_one_four_six")



        #---------------------------------------------------------------------------
                
                #flow_one_three   --stage_two

        if  a_three_wread and a_three_opens > a_one and a_three_opens < current_closing and a_three_opens > a_one_closes:
            print("flow_one_three ------copied")
            #in pratice it not possible to "a_four_opens == a_three_closes", make it aprox
            if a_four_green and a_four_opens == a_three_closes:
                print("flow_one_three_one")

            if a_four_wread and a_four_opens > current_closing:
                print("flow_one_three_two")
            if a_four_green and a_four_opens < a_three_closes:
                print("flow_one_three_three")
            if a_four_green and a_four_opens > a_three_closes:
                print("flow_one_three_four")
            if a_four_wread and a_four_opens < current_closing:
                print("flow_one_three_five")

        #--------------------------------------------------------------------------------------------

            #flow_one_three_one   --stage_three
           
           
           #in pratice it not possible to "a_four_opens == a_three_closes", make it aprox
            if a_four_green and a_four_opens == a_three_closes:
                print("flow_one_three_one ---copied")
                a_five_green = True
                a_five_wread = True
                a_five_opens = True
                if a_five_green:
                    print("flow_one_three_one_one  --signal is here (2nd degree)")
                if a_five_wread and a_five_opens < a_four_closing:
                    print("flow_one_three_one_two --signal is here (2nd degree)")
                    #In practice it is almost not possible, Please make it approx
                if a_five_wread and a_five_opens == a_four_closing:
                    print("flow_one_three_one_three -- might become the signal(3rd degree)")
                if a_five_wread and a_five_opens > a_four_closing:
                    print("flow_one_three_one_four")


        #------------------------------------------------------------------------------------------------

            #flow_one_three_three   --stage_three
            if a_four_green and a_four_opens < a_three_closes:
                print("flow_one_three_three --copied")

                if a_five_green and a_five_opens < a_four_opens:
                    print("flow_one_three_three_one")
                if a_five_wread and a_five_opens < a_four_closing:
                    print("flow_one_three_three_two")
                #in pratice it not possible to "a_five_opens == a_four_closing", make it aprox
                if a_five_wread and a_five_opens == a_four_closing:
                    print("flow_one_three_three_three")
                if a_five_wread and a_five_opens > a_four_closing and a_five_opens < current_closing:
                    print("flow_one_three_three_four")
                if a_five_wread and a_five_opens > a_four_closing and a_five_opens > current_closing:
                    print("flow_one_three_three_five")

        #---------------------------------------------------------------------------------------------------------------

            #flow_one_three_four   --stage_three
                    
                if a_four_green and a_four_opens > a_three_closes:
                    print("flow_one_three_four  ---copied")

                    if a_five_green and a_five_opens < a_three_closes:
                        print("flow_one_three_four_one")
                    if a_five_green and a_five_opens > a_three_closes: 
                        print("flow_one_three_four_two")
                    if a_five_wread and a_five_opens < a_four_closing:
                        print("flow_one_three_four_three")
                    #in pratice it not possible to "a_five_opens == a_four_closing", make it aprox
                    if a_five_wread and a_five_opens == a_four_closing:
                        print("flow_one_three_four_four")
                    if a_five_wread and a_five_opens > a_four_closing and a_five_opens < current_closing:
                        print("flow_one_three_four_five")
                    if a_five_wread and a_five_opens > a_four_closing and a_five_opens > current_closing:
                        print("flow_one_three_four_six")
        #----------------------------------------------------------------------------------------------------------------
                
            #flow_one_three_five  --stage_three
                        
            if a_four_wread and a_four_opens < current_closing:
                print("flow_one_three_five ---copied")

                if a_five_green and a_five_opens > a_four_closing:
                    print("flow_one_three_five_one")
                if a_five_green and a_five_opens < a_four_closing and a_five_opens > a_three_closes:
                    print("flow_one_three_five_two")
                if a_five_green and a_five_opens < a_four_closing and a_five_opens < a_three_closes:
                    print("flow_one_three_five_three")
                if a_five_wread and a_five_opens > a_five_opens and a_five_opens < current_closing:
                    print("flow_one_three_five_four")
                if a_five_wread and a_five_opens > current_closing:
                    print("flow_one_three_five_five ")
            







def flow_two():

    current_closing = True

    #flow_one -stage_one
    current_green = True
    a_one_green = True
    a_two_wread = True
    a_two_opens = True
    a_one_closing = True
    if current_green and a_one_green and a_two_wread and a_two_opens > a_one_closing and a_two_opens < current_closing:

        print("flow_two -stage_one")





        # flow_two_one --stage-two-start
        a_three_wread = True
        a_three_opens = True
        if a_three_wread and a_three_opens < current_closing:
            print("flow_two_one --stage_two")
        #flow_two_two --stage_two
        if a_three_wread and a_three_opens > current_closing:
            print("flow_two_two --stage_two falsy")
        #flow_two_three --stage_two
        a_two_closing = True
        a_three_green = True
        if a_three_green and a_three_opens > a_two_closing:
            print("flow_two_three")
        #flow_two_four --stage_two
        if a_three_green and a_three_opens < a_two_closing:
            print("flow_two_four")
        #flow_two_five --stage_two
        if a_three_green and a_three_opens < a_two_closing:
            print("flow_two_five --stage_two")





        #flow_two_one ---stage_three-starts
        if a_three_wread and a_three_opens < current_closing:
            print("flow_two_one --stage_two -copied")
            #flow_two_one_one ---stage_three-starts
            a_four_opens = True
            a_four_green = True
            a_three_closing = True
            #                  approx
            if a_four_green and a_four_opens == a_three_closing:
                print("flow_two_one_one ---stage_three")
            #flow_two_one_two ---stage_three
            if a_four_green and a_four_opens > a_three_closing:
                print("flow_two_one_two ---stage_three")
            #flow_two_one_three ---stage_three
            if a_four_green and a_four_opens > a_three_closing and a_four_opens < a_two_closing:
                print("flow_two_one_three ---stage_three")
            #flow_two_one_four ---stage_three 
            if a_four_green and a_four_opens == a_two_closing:
                print("flow_two_one_four ---stage_three")
            #flow_two_one_five ---stage_three
            if a_four_green and a_four_opens < a_two_closing:
                print("flow_two_one_five ---stage_three")
            #flow_two_one_six ---stage_three
            a_four_wread = True
            if a_four_wread and a_four_opens > current_closing:
                print("flow_two_one_six ---stage_three")


        #flow_two_three ---stage_three -copied
        if a_three_green and a_three_opens > a_two_closing:
            print("flow_two_three ---stage_three_starts -copied")
            #flow_two_three_one ---stage_three
            if a_four_green and a_four_opens > a_two_closing:
                print("flow_two_three_one ---stage_three")
            #flow_two_three_two ---stage_three
            if a_one_green and a_four_opens < a_two_closing:
                print("flow_two_three_two ---stage_three")
            #flow_two_three_three ---stage_three
            if a_four_wread and a_four_opens == a_three_closing:
                print("flow_two_three_three ---stage_three")
            #flow_two_three_four ---stage_three
            if a_four_wread and a_four_opens > a_three_closing and a_four_opens < current_closing:
                print("flow_two_three_four ---stage_three")
        


        #flow_two_four --stage_three_starts -copied
        if a_three_green and a_three_opens < a_two_closing:
            print("flow_two_four --stage_three_starts -copied")

            #flow_two_four_one --stage_three_starts
            if a_four_green:
                print("flow_two_four_one --stage_three")
            #flow_two_four_two --stage_three
            if a_four_wread and a_four_opens < a_three_closing:
                print("flow_two_four_two --stage_three")
            #flow_two_four_three --stage_three
            if a_four_wread and a_four_opens == a_three_closing:
                print("flow_two_four_three --stage_three")
            #flow_two_four_four --stage_three
            if a_four_green and a_four_opens > a_three_closing and a_four_opens < current_closing:
                print("flow_two_four_four --stage_three")

        


        #flow_two_five --stage_three_starts -copied
        if a_three_green and a_three_opens < a_two_closing:
            print("flow_two_five --stage_three_starts -copied")
            
            #flow_two_five_one --stage_three_starts
            if a_four_green:
                print("flow_two_five_one --stage_three_starts")
            #flow_two_five_two --stage_three_starts
            if a_four_wread and a_four_opens < a_three_closing:
                print("flow_two_five_two --stage_three")
            #flow_two_five_three --stage_three_starts
            if a_four_wread and a_four_opens == a_three_closing:
                print("flow_two_five_three --stage_three")
            #flow_two_five_four --stage_three
            if a_four_green and a_four_opens < current_closing and a_four_opens > a_three_closing:
                print("flow_two_five_four --stage_three")
            #flow_two_five_five --stage_three
            if a_four_green and a_four_opens > current_closing:
                print("flow_two_five_five --stage_three")




        """ flow_two_one_one series going to come here -------------------------------------------"""








                

        #flow_two_three_one_one stage_four_starts
        if a_three_green and a_three_opens > a_two_closing:
            print("flow_two_three ---stage_three_starts_for_four --copied2")
            #flow_two_three_one ---stage_three_for_four -copied
            if a_four_green and a_four_opens > a_two_closing:
                print("flow_two_three_one ---stage_four_starts -copied ")
                #flow_two_three_one_one ----stage_four starts
                a_five_green = True
                if a_five_green:
                    print("flow_two_three_one_one ----stage_four started")
                #flow_two_three_one_two ----stage_four
                a_five_opens = True
                if a_five_green and a_five_opens > a_two_closing:
                    print("flow_two_three_one_two ----stage_four")
                #flow_two_three_one_three ----stage_four
                a_four_closing = True
                a_five_wread = True
                if a_five_wread and a_five_opens == a_four_closing:
                    print("flow_two_three_one_three ----stage_four")
                #flow_two_three_one_four ----stage_four
                if a_five_wread and a_five_opens > a_four_closing and a_five_opens < a_three_closing:
                    print("flow_two_three_one_four ----stage_four")
                #flow_two_three_one_five ----stage_four
                if a_five_wread and a_five_opens == a_three_closing:
                    print("flow_two_three_one_five ----stage_four")
                #flow_two_three_one_six ----stage_four
                if a_five_wread and a_five_opens > a_three_closing and a_five_opens < current_closing:
                    print("flow_two_three_one_six ----stage_four")
                #flow_two_three_one_seven ----stage_four
                if a_five_wread and a_five_opens > current_closing:
                    print("flow_two_three_one_seven ----stage_four")
                    
            


        #flow_two_three_two ----stage_four_starts -copied
        if a_three_green and a_three_opens > a_two_closing:
            print("flow_two_three ---stage_four_starts -copied")
            #flow_two_three_two ---stage_three
            if a_one_green and a_four_opens < a_two_closing:
                print("flow_two_three_two ---stage_four_starts")

                #flow_two_three_two_one ---stage_four_starts -copied
                if a_five_green:
                    print("flow_two_three_two_one _starts_started")
                #flow_two_three_two_two
                if a_five_wread and a_five_wread == a_four_closing:
                    print("flow_two_three_two_two ---stage_four")
                #flow_two_three_two_three
                if a_five_wread and a_five_opens > a_three_closing and a_five_opens < a_three_closing:
                    print("flow_two_three_two_three ---stage_four")
                if a_five_wread and a_five_opens == a_three_closing:
                    print("flow_two_three_two_four ---stage_four")
                if a_five_wread and a_five_opens > a_three_closing and a_five_opens < current_closing:
                    print("flow_two_three_two_five ---stage_four")
                if a_five_wread and a_five_opens > current_closing:
                    print("flow_two_three_two_six ---stage_four")
                
                





        
        
        #flow_two_three_two ----stage_four_starts -copied
        if a_three_green and a_three_opens > a_two_closing:
            print("flow_two_three ---stage_four_starts -copied")
            #flow_two_three_three ---stage_three
            if a_four_wread and a_four_opens == a_three_closing:
                print("flow_two_three_three ---stage_four_starts - copied")
                #flow_two_three_three_one ------stage_four_starts
                if a_five_green and a_five_opens == a_three_closing:
                    print("flow_two_three_three_one ---stage_four_started")
                #flow_two_three_three_two ---stage_four
                if a_five_green and a_five_opens > a_three_closing:
                    print("flow_two_three_three_two ---stage_four")
                #flow_two_three_three_three ---stage_four
                if a_five_green and a_five_opens < a_two_closing:
                    print("flow_two_three_three_three ---stage_four")
                #flow_two_three_three_four ---stage_four
                if a_five_green and a_five_opens == a_two_closing:
                    print("flow_two_three_three_four ---stage_four")
                #flow_two_three_three_five ---stage_four
                if a_five_green and a_five_opens > a_two_closing and a_five_opens < a_four_closing:
                    print("flow_two_three_three_five ---stage_four")
                #flow_two_three_three_six ---stage_four
                if a_five_wread and a_five_opens < current_closing:
                    print("flow_two_three_three_six ---stage_four")
                #flow_two_three_three_seven ---stage_four
                if a_five_wread and a_five_opens > current_closing:
                    print("flow_two_three_three_seven ---stage_four")





        #flow_two_three_two ----stage_four_starts -copied
        if a_three_green and a_three_opens > a_two_closing:
            print("flow_two_three ---stage_four_starts -copied")
            #flow_two_three_four ---stage_three
            if a_four_wread and a_four_opens > a_three_closing and a_four_opens < current_closing:
                print("flow_two_three_four ---stage_three")
                #flow_two_three_four_one ---stage_four_starts
                if a_five_green and a_five_opens > a_four_closing:
                    print("flow_two_three_four_one ---stage_four_started")
                #flow_two_three_four_two ---stage_three
                if a_five_green and a_five_opens == a_four_closing:
                    print("flow_two_three_four_two ---stage_three")
                #flow_two_three_four_three ---stage_three
                if a_five_green and a_five_opens < a_two_closing:
                    print("flow_two_three_four_three ---stage_three")
                #flow_two_three_four_four ---stage_three
                if a_five_wread and a_five_opens < current_closing:
                    print("flow_two_three_four_four ---stage_three")
                #flow_two_three_four_five ---stage_three
                if a_five_green and a_five_opens == a_two_closing:
                    print("flow_two_three_four_five ---stage_three")





        #flow_two_four --stage_three_starts -copied
        if a_three_green and a_three_opens < a_two_closing:
            print("flow_two_four --stage_three_starts -copied")

            #flow_two_four_one --stage_three_starts
            if a_four_green:
                print("flow_two_four_one --stage_three -copied")
                #flow_two_four_one_one ----stage_four_starts
                if a_five_green:
                    print("#flow_two_four_one_one ----stage_four_started")
                #flow_two_four_one_two ----stage_four
                if a_five_wread and a_five_opens < a_four_closing:
                    print("flow_two_four_one_two ----stage_four")
                #flow_two_four_one_three ----stage_four
                if a_five_wread and a_five_opens == a_four_closing:
                    print("flow_two_four_one_three ----stage_four")
                #flow_two_four_one_four ----stage_four
                if a_five_wread and a_five_opens > a_four_closing and a_five_opens < a_three_closing:
                    print("flow_two_four_one_four ----stage_four")
                #flow_two_four_one_five ----stage_four
                if a_five_wread and a_five_opens == a_three_closing:
                    print("flow_two_four_one_five ----stage_four")
                #flow_two_four_one_six ----stage_four
                if a_five_wread and a_five_opens > a_three_closing and a_five_opens < current_closing:
                    print("flow_two_four_one_six ----stage_four")
                #flow_two_four_one_seven ----stage_four
                if a_five_wread and a_five_opens > current_closing:
                    print("flow_two_four_one_seven ----stage_four")





    #flow_two_four --stage_three_starts -copied
    if a_three_green and a_three_opens < a_two_closing:
        print("flow_two_four --stage_three_starts -copied")

        #flow_two_four_two --stage_three_starts
        if a_four_wread and a_four_opens < a_three_closing:
            print("flow_two_four_two --stage_three_starts_for_four - copied")
            #flow_two_four_two_one --stage_four
            if a_five_green and a_two_opens < a_four_closing:
                print("flow_two_four_two_one --stage_three_started")
            #flow_two_four_two_two --stage_three
            if a_five_green and a_five_opens == a_four_closing:
                print("flow_two_four_two_two --stage_three")
            #flow_two_four_three --stage_three
            if a_five_green and a_five_opens < a_four_closing:
                print("flow_two_four_three --stage_three")
            #flow_two_four_two_four --stage_three
            if a_five_wread and a_five_opens < a_four_closing:
                print("flow_two_four_two_four --stage_three")
            #flow_two_four_two_five --stage_three
            if a_five_wread and a_five_opens == a_four_closing:
                print("flow_two_four_two_five --stage_three")
            #flow_two_four_two_six --stage_three
            if a_five_wread and a_five_opens > a_four_closing and a_five_opens < current_closing:
                print("flow_two_four_two_six --stage_three")
            #flow_two_four_two_seven --stage_three
            if a_five_wread and a_five_opens > current_closing:
                print("flow_two_four_two_seven --stage_three")









