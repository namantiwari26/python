'''
Write a function that uses regular expressions to validate if a given string is a valid
email address

'''
import re

def validate_email(email):
    pattern=(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')

    if re.match(pattern,email):

        return True
    
    else:
        return False
    
email1="example26@example.com"
email2="invalid_email.com"
print("Email1 is valid:",validate_email(email1))
print("Email2 is valid:",validate_email(email2))
