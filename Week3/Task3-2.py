#Task 2: Password Policy Validator

def validate_password(password):
    #Return if true if password follows policy otherwise false
    uppercase = 0
    lowercase = 0
    digits = 0
    symbols = 0

    #Counts each type of character in the password
    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char in "!@#$%":
            #Only these symbols are allowed in the policy
            symbols += 1

    #Check every rule in the policy
    if len(password) < 10:  #Minimum length 10 chars
        return False
    if uppercase < 1:  #At least 1 uppercase letter
        return False
    if lowercase < 1:   #At least 1 lowercase letter
        return False
    if digits < 2:  #At least 2 digits
        return False
    if symbols <1:  #At least 1 symbol
        return False
    if " "  in password: #No spaces
        return False

    return True

#Keep asking until user enters a valid password
while True:
    password = input("Enter your password: ")

    if validate_password(password):
        print("Password accepted")
        break
    else:
        print("Password rejected, it does not follow the policy")
