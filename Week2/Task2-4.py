#Task 4: Check a number between 1 and 100 and check if its odd or even

def check_number(number):
    #Return message about the number entered
    if number < 1 or number > 100:
        #The number is outside the 1-100 range
        return "Error: the number must be between 1 and 100.:"
    elif number % 2 == 0:
        #The modulus operator gives 0 for even numbers
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"

#Ask the user for a positive number between 1 and 100
number = int(input("Enter a positive number between 1 and 100: "))

#Display the message for outcome
print(check_number(number))