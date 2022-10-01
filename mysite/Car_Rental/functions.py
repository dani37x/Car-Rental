import random
import string
from datetime import datetime

def random_pass():
    small = string.ascii_lowercase
    big = string.ascii_uppercase
    special = string.punctuation
    numbers = string.digits
    s =  small + big + special + numbers
    random_choices = random.sample(s, 10)
    random.shuffle(random_choices)
    new_password = "".join(random_choices)
    return new_password


def allowed_password(password, password_2):
    if len(password) < int(6):
        print('password is too short')
        return False
    if password == password_2:
        print('p1 == p2')
        special = string.punctuation
        big = string.ascii_uppercase
        number = string.digits
        special_char = False
        big_char = False
        number_char = False
        for char in special:
            if char in password:
                special_char = True
                break
        for char in big:
            if char in password:
                big_char = True
                break
        for char in number:
            if char in password:
                number_char = True
                break
        if special_char == True and big_char == True and number_char == True:
            print('secure password')
            return True
        else:
            print('Your password is not secure')
            return False
    else:
        print('passwords are different')
        return False
    
        
# allowed_password(password='hej^K55' , password_2='hej^K55')


def days(date_from, date_to):
    date_from = datetime.strptime(date_from, "%Y-%m-%d")
    date_to = datetime.strptime(date_to, "%Y-%m-%d")
    return int((date_from-date_to).days)