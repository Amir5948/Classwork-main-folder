#Task 1: Password String Analysis

def analyse_password(password):

    #Counters for each character type
    uppercase = 0
    lowercase = 0
    numbers = 0
    symbols = 0

#Examine each character in the password
    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
        else:
            #Anything that is not a letter or digit counts as symbol
            symbols += 1

    return uppercase, lowercase, numbers, symbols

#Get password from the user
password = input("Enter your password: ")

#Call the function to analyse the password
uppercase, lowercase, numbers, symbols = analyse_password(password)

#Display the analysis (len() counts the total characters
print("Password Length", len(password))
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Numbers:", numbers)
print("Symbols:", symbols)