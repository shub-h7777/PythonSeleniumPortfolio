from utilities import read_utils

"""
test invalid login data consist following:
Blank email, Blank password
Blank email, Invalid password
Blank email, Valid password
Invalid email, Blank password
Invalid email, Invalid password
Invalid email, Valid password
Valid email, Blank password
Valid email, Invalid password
"""

test_invalid_login_data = [
     ("", "", "Login was unsuccessful. Please correct the errors and try again."),
     ("", "Invalid", "Login was unsuccessful. Please correct the errors and try again."),
     ("", "Demo@123", "Login was unsuccessful. Please correct the errors and try again."),
     ("invalid@gmail.com", "", "Login was unsuccessful. Please correct the errors and try again."),
     ("invalid@gmail.com", "Invalid", "Login was unsuccessful. Please correct the errors and try again."),
     ("invalid@gmail.com", "Demo@123", "Login was unsuccessful. Please correct the errors and try again."),
     ("shuham122@gmail.com", "", "Login was unsuccessful. Please correct the errors and try again."),
     ("shuham122@gmail.com", "Invalid", "Login was unsuccessful. Please correct the errors and try again."),
    ]

test_valid_login_data = [
     ("shuham122@gmail.com", "Demo@123"),
     ("demo@shubham.com", "demo@shubham.com")
    ]

test_invalid_register_data = [
     ("male", "sh", "sh", "sh@gmail.com", "passw", "confirm passw"),
     ("male", "sh", "sh", "sh@gmail.com", "passw", "confirm passw")
    ]

test_invalid2_register_data = [
     ("male", "", "sh", "sh@gmail.com", "passw", "confirm passw", "First name is required.", "", "", "", "")
    ]