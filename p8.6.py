#Shreyash Kadam
import logging

logging.basicConfig(filename="error.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")
try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError occurred: %s", e)
    print("An error occurred. Check error.log for details.")
