import sys

def get_error_message(error, error_detail: sys):
    # Extract the traceback object
    _, _, exc_tb = error_detail.exc_info()
    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Create a detailed error message
    error_message = (
        f"Error occurred in script: [{file_name}], "
        f"line number: [{exc_tb.tb_lineno}], "
        f"error message: [{error}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the base Exception class with the error message
        super().__init__(error_message)
        # Get a detailed error message
        self.error_message = get_error_message(error_message, error_detail)

    def __str__(self):
        # Return the detailed error message when the exception is printed
        return self.error_message
