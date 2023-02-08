from Insurance_machine_learning import logging
from Insurance_machine_learning.exception import Insurance_machine_learning_Exception
import os,sys

def test_logger_and_exception():
    try:
        logging.info("Starting the test_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("Ending point of the test_logger_and_exception")
    except Exception as e:
        logging.debug(str(e))
        raise Insurance_machine_learning_Exception(e,sys)

if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)

