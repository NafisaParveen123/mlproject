import sys
from src.logger import logging
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message
    
class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        message = error_message_detail(error, error_detail)
        super().__init__(message)
        self.error_message = message

    
    def __str__(self):
        return self.error_message
    


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divide by zero")
        raise CustomException(e,sys)   