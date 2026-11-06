# Task 08: Security Tool
 
# Stored credentials and passwords
USERNAME = "admin"
PASSWORD = "admin123"                 # correct password for the program and event counter
BRUTE_FORCE_PASSWORD = "Pass1234!"    # password for the brute-force
 
MAX_BRUTE_FORCE_ATTEMPTS = 5          # maximum guesses in the brute-force simulation
MAX_FAILED_LOGINS = 3                 # failed logins allowed before the account is frozen
 
 
def authenticate(username, password):
    #Return true if the username and password are correct, otherwise false
    return username == USERNAME and password == PASSWORD
 
 
def start_authentication():
    #The user must authenticate before the menu is shown
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if authenticate(username, password):
            print("Authentication successful.")
            return
        print("Authentication failed. Try again.")
 
 
def security_event_counter():
    #Ask for a password 10 times and count the correct and incorrect
    correct = 0
    incorrect = 0
 
    for i in range(10):
        guess = input(f"Enter password ({i + 1}/10): ")
        if guess == PASSWORD:
            correct += 1
        else:
            incorrect += 1
 
    # Calculate the percentage of incorrect passwords
    percentage = incorrect / 10 * 100
 
    print("Correct passwords:", correct)
    print("Incorrect passwords:", incorrect)
    print(f"Percentage of incorrect passwords: {percentage}%")
 
    # Raise an alert if more than 50% were incorrect
    if percentage > 50:
        print("ALERT: More than 50% of the passwords entered were incorrect!")
 
 
def brute_force_simulation():
    #Allow a maximum number of guesses
    attempts = 0
 
    while attempts < MAX_BRUTE_FORCE_ATTEMPTS:
        guess = input("Enter a password guess: ")
        attempts += 1
 
        if guess == BRUTE_FORCE_PASSWORD:
            print(f"Correct password found in {attempts} attempt(s).")
            return
 
    # The loop ended because the maximum number of attempts was reached
    print("Maximum number of attempts reached. Password not found.")
 
 
def login_authentication():
    #Ask for credentials and allow 3 failed logins
    failed_logins = 0
 
    while failed_logins < MAX_FAILED_LOGINS:
        username = input("Enter username: ")
        password = input("Enter password: ")
 
        if authenticate(username, password):
            print("Authentication succeeded.")
            return
 
        failed_logins += 1
        print("Authentication failed.")
 
    # Three failed logins reached
    print("Maximum failed logins reached. Your account is frozen for 24 hours.")
 
 
# Main program: the user must authenticate first
start_authentication()
 
# Show the menu until the user chooses Exit
while True:
    print("\nSecurity Menu")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")
    choice = input("Enter your choice: ")
 
    if choice == "1":
        security_event_counter()
    elif choice == "2":
        brute_force_simulation()
    elif choice == "3":
        login_authentication()
    elif choice == "4":
        print("Thank you for using the security tool.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
 