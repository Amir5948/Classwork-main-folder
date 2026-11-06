#Task 3: Security Event String Analysis

def extract_ip_address(event):
    #find() gives the position of the text
    start = event.find("address ") + len("address ")

    #Slice the event from the start of the IP address onwards
    remaining_text = event[start:]

    #The IP address is the first word of the remaining text
    ip_address = remaining_text.split(" ")[0]

    #Remove the full stop at the end of the setence
    return ip_address.rstrip(".")

#The sample security event message
event = ("Security Alert: Failed login attempt detected from IP address 192.168.1.25. The user account admin was targetted at 22:45. The server blocked the login attempt after an incorrect password was entered.")

#Check whether the words failed and login appear in the event
failed_found = "Failed" in event
login_found = "login" in event

#Extracting the IP address
ip_address = extract_ip_address(event)

#Display the analysis
print("Security Event Analysis")
print("---------------------------")

if failed_found:
    print("Failed event: Yes")
else:
    print("Failed event: No")

if login_found:
    print("Login event: Yes")
else:
    print("Login event: No")

print("IP Address:", ip_address)

if failed_found:
    print("Warning: A failed securiy event was detected.")

if login_found:
    print("Login activity detected")

#Recommend an action when failed login was found
if failed_found and login_found:
    print("Action: Investifate the failed login attempt.")