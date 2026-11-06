#Task 2: Login Authentication Function

#The credentials that the users input is compared with
STORED_USERNAME = "admin"
STORED_PASSWORD = "admin123"

def authenticate(username, password):
    #Returns True if both username and password are correct, otherwise false
    if username == STORED_USERNAME and password == STORED_PASSWORD:
        return True
    return False

#Main program, keep asking until valid credentials
while True:
    #try-except handles problems with the users input
    try:
        #Asking user for username and password
        username = input("\nEnter username: ").strip()
        password = input("Enter password: ").strip()

        #An empty input is invalid, so error is raised
        if username == "" or password == "":
            raise ValueError("Username and password cannot be empty")

        #Call authenticate function and display result
        if authenticate(username, password):
            print("Login Successful")
            break #Correct credentails so loop is broken
        else:
            print("Invalid username or password")

    except ValueError as error:
        #Runs when input was empty
        print("Invalid input:", error)
    
    