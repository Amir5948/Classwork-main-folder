#Task 4: IP Address Validator

def validate_ip(ip):
    #Returns true if IP address meets requirements, otherwise false
    ip = ip.strip()

    #Check the IP address contains dots
    if "." not in ip:
        return False

    #Check that there is exactly 3 dots
    if ip.count(".") != 3:
        return False

    #Split the IP address into parts
    parts = ip.split(".")

    #Check that there are four parts
    if len(parts) != 4:
        return False

    for part in parts:
        #Check that eahc part contains only digits
        if not part.isdigit():
            return False

        #Change part into an integer
        number = int (part)

        #Check that the number is between 0 and 255
        if number < 0 or number > 255:
            return False

    return True

#Get the IP address from the user
ip_address = input("Enter an IP address: ")

#Display whether the IP address is valid
if validate_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")

    