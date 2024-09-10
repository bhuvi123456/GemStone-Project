import sys
from Source.Logger import logging
def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name  = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"The error occured in the file named as [{file_name}] at line number [{line_number}] and the error is [{str(error)}]"
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
    def __str__(self):
        return self.error_message
if __name__ == '__main__':    # Just to test whether the code is working
    logging.info("Logging has started")
    try:
        a = 1
        b = 0
        a / b
    except Exception as e:
        logging.error("Division by zero error")
        raise CustomException(e, sys)
