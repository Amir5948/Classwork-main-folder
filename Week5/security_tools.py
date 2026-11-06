#Reusable Cyber Security Utilities using User-Defined Modules

import random #used to generate random passwords
import string #provides ready-made sets of letters, digits, and symbols

def validate_password(password):
    #Minimum length check
    if len(password) < 8:
        return False

    #Start by assuming the password does not have letters, digits, or symbols
    has_letter = False
    has_digit = False
    has_symbol = False

    #Look at each character and record which types we find
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True
    #The password is valid only if all 3 types were found
    return has_letter and has_digit and has_symbol

def validate_ip(ip_address):
    #Split the address at each dot
    octets = ip_address.split('.')

    #3 dots means exactly 4 parts
    if len(octets) != 4:
        return False
    for octet in octets:
        #Each part must only contain digits
        if not octet.isdigit():
            return False
        #Each number must be in the range of 0 to 255
        if int(octet) < 0 or int(octet) > 255:
            return False
    #All 4 octets are valid
    return True

def generate_password():
    #Pick a random legnth between 10 and 16 each time
    length = random.randint(10, 16)
    #Ensure the password has at least one of each type of character
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    #Fill the reamaining length with random characters from all groups
    all_chars = string.ascii_letters + string.digits + string.punctuation
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    #Shuffle so that the characters are not always at the start
    random.shuffle(password_chars)
    #Join the list of characters into a single string
    return "".join(password_chars)

