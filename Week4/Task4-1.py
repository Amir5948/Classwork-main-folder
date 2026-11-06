#Task 1: Password Policy Validator using Functions

#The only symbols accepted by the policy
ALLOWED_SYMBOLS = "!@#$%"

def validate_password(password):
    #Count how many of each character type the password contains
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    symbol_count = 0

    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in ALLOWED_SYMBOLS:
            symbol_count += 1

    #Password is valid until a rule is broken
    valid = True

    #Minimum length of characters is 10
    if len(password) < 10:
        print("- Password must be at least 10 characters long")
        valid = False

    #At least 1 uppercase letter
    if uppercase_count < 1:
        print("- Password must have at least 1 uppercase letter.")
        valid = False

    #At least 1 lowercase letter
    if lowercase_count < 1:
        print("- Password must have at least 1 lowercase letter")
        valid = False

    #At least 2 digits
    if digit_count < 2:
        print("- Password must have at least 2 digits")
        valid = False

    #At least 1 symbol from the allowed list
    if symbol_count < 1:
        print("- Password must have at least 1 symbol from: ! @ # $ %")
        valid = False

    return valid

#Main program, keep asking until valid password in entered
while True:
    username = input("\nEnter a username: ")
    password = input("\nEnter a password: ")

    #Call validator and use true or false result
    if validate_password(password):
        print(f"\nPassword accepted. Welcome, {username}!")
        break #Valid password so loop is broken
    else:
        print("Password rejected, please try a new username and password")
