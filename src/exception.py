import sys
from src.logger import logging

# tells what happened and where

#accident investigator
def error_message_detail(error, error_detail:sys): #sys->imports investigators toolbox
    _,_,exc_tb = error_detail.exc_info() #it uses sys tool to get the last exceptions info. we just care bout traceback

    file_name = exc_tb.tb_frame.f_code.co_filename #finding the exact file name of the accident
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error))
   #it takes file name the exact line number and the original msg error
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): #instruction to filling out the form.  it reqs the og error msg and investigators toolbox(error detail)
        super().__init__(error_message) #its like writing the og ouch msg at thr top of the form just for reference
        self.error_message=error_message_detail(error_message,error_detail=error_detail) #calls the main func

    def __str__(self):
        return self.error_message


if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys) # 1. dont ignore this simple ouch error 2. i want to raise a new better error 3. creating a new customexp giving it the og ouch and the investigators toolbox.
    #This triggers the def __init__() which calls the investigator func who builds detialed report. the raise command then stops the program and shows that new detailed report to the user
    
