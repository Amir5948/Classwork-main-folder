#Task 4: Security Event Logger

import random
import socket
from datetime import datetime

#The correct credentials
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "admin123" 

def get_ip_address():
    #Return the IP address of this system
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

def create_event(username, event_type):
    #Create security event record for login attempt
    return {
        "Event ID": random.randint(1000, 9999),
        #Random 4 digit number
        "Username": username,
        "IP Address": get_ip_address(),
        "Event": event_type,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        #Readable date and time
    }

#List that stores the event log for every login attempt
event_log = []

#Keep asking until the correct username and password is entered
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        event_log.append(create_event(username, "Successful login"))
        break #Correct credentials so loop is broken
    else:
        event_log.append(create_event(username, "Failed login"))

#Event log is printed for all attempts
print("\nSecurity event log")
print("---------------------")
for event in event_log:
    print()
    for key, value in event.items():
        print(f"{key}: {value}")