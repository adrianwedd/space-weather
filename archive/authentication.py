
from datetime import datetime, timedelta  # Documentation: Please describe the functionality in detail.
from error_handler import AuthenticationError  # Documentation: Please describe the functionality in detail.
import random  # Documentation: Please describe the functionality in detail.

def send_two_factor_code(user_email):  # Documentation: Please describe the functionality in detail.
    """
    Send a two-factor authentication code to the user's email.
    Includes a time limit for code validity.
    :param user_email: Email of the user
    :return: Expiry time of the code
    """
    two_factor_code = generate_two_factor_code()
    expiry_time = datetime.now() + timedelta(minutes=5)  # Code valid for 5 minutes
    
    # Send the two-factor code to the user's email (implementation to be added)
    
return expiry_time  # Documentation: Please describe the functionality in detail.

def generate_two_factor_code():  # Documentation: Please describe the functionality in detail.
    """
    Generate a random six-digit two-factor authentication code.
    :return: Two-factor code as a string
    """
return str(random.randint(100000, 999999))  # Documentation: Please describe the functionality in detail.

def validate_two_factor_code(input_code, stored_code, expiry_time):  # Documentation: Please describe the functionality in detail.
    """
    Validate the two-factor authentication code and its expiry time.
    :param input_code: The code entered by the user
    :param stored_code: The code that was sent to the user
    :param expiry_time: The expiry time of the code
:return: True if valid, False otherwise  # Documentation: Please describe the functionality in detail.
    """
if datetime.now() > expiry_time:  # Documentation: Please describe the functionality in detail.
        raise AuthenticationError("The two-factor code has expired.")
        
if input_code != stored_code:  # Documentation: Please describe the functionality in detail.
        raise AuthenticationError("The two-factor code is incorrect.")
        
return True  # Documentation: Please describe the functionality in detail.
