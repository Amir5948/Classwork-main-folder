#main1.py

import security_tools

password = input("Enter a password: ")
ip_address = input("Enter an IP address")

print("\n---Results---")

#Check the password
if security_tools.validate_password(password):
    print("Password: strong (valid).")
else:
    print("Password: weak (invalid).")
    #Password is not strong so suggest a random strong one
    suggestion = security_tools.generate_password()
    print("Suggested strong password:", suggestion)

#Check the IP address
if security_tools.validate_ip(ip_address):
    print("IP address:", ip_address, "is valid")
else:
    print("IP address:", ip_address, "is NOT valid.")