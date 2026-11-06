#Task 3: Failed Login Risk Calculator

def calculate_failed_percentage(failed, total):
    #Return percentage of failed login attempts
    return (failed / total) * 100

try:
    #Get the the nubmer of failed attempts and total attempts from the user
    failed_logins = int(input("Enter the number of failed login attempts"))
    total_logins = int(input("Enter the total number of login attempts: "))

    #Calculate the percentage of failed attempts
    percentage = calculate_failed_percentage(failed_logins, total_logins)
    print("Failed percentage", percentage, "%")

    #Label the result
    if percentage >= 50:
        print("High risk")
    elif percentage >= 25:
        print("Medium risk")
    else:
        print("Low risk")

except ValueError:
    #Runs if the input is not a number
    print("Please enter numbers only")
except ZeroDivisionError:
    #Runs if the total number of attempts is 0
    print("Total login attempts cannot be zero")