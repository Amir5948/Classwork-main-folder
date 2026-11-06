#Task 6: Keep asking for the password till its correct

#The password
correct_password = "admin123"

#Ask the user to enter a password
password = input("Enter the password: ")

#Keep asking while the password is incorrect
while password != correct_password:
    password = input("Enter the password")

#The correct password entered
print("Access granted")