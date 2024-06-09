from lib import *
import time


def main_loop():
    while True:
        sleep_time = next_fivemloop_inseconds()

        if sleep_time != 0:
            start_time = time.time()
            while (time.time() - start_time) < sleep_time:
                ltp_target_checking()
                time.sleep(5)
        elif sleep_time <= 0:
            start_time = time.time()
            while (time.time() - start_time) < 300:
                ltp_target_checking()
                time.sleep(5)

        # Place your main function logic here that runs after the sleep period.
        print("Main loop is running.")

if __name__ == "__main__":
    main_loop()
