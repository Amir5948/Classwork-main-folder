#Task 1: Suspicous IP Address Manager using Lists

ips = ["192.168.1.15", "10.0.0.23", "172.16.5.9", "203.0.113.45", "198.51.100.7"]

def add_ip(ip_list):
    #Ask user to type in new IP address
    new_ip = input("Enter an IP address to add: ")
    #Append adds new item to the end of list
    ip_list.append(new_ip)
    #Confirm to user than IP is added
    print(new_ip, "added.")

def change_ips(ip_list):
    #Ask which IP address should be changed
    old_ip = input("Enter the IP address to change: ")
    #Continue if IP is in list
    if old_ip in ip_list:
        #index finds position of old IP in list
        index = ip_list.index(old_ip)
        #Replace old IP by assigning new one
        ip_list[index] = input("Enter the new IP address: ")
        print("IP address updated.")

def remove_ip(ip_list):
    #Ask which IP address should be removed
    ip = input("Enter an IP address to remove: ")
    #Check first, remove may cause error if item is missing
    if ip in ip_list:
        #Remove deletes the first item which matches the value
        ip_list.remove(ip)
        print(ip, "removed.")
    else:
        #The IP was not found, nothing to remove
        print(ip, "not found.")

def search_ip(ip_list):
    #Ask which IP address to look for
    ip = input("Enter an IP address to search for: ")
    #The "in" operator becomes true if the item is in list
    if ip in ip_list:
        print(ip, "exists in the list.")
    else:
        print(ip, "does not exist in the list.")

#Main program

#Whole list is displayed
print("Suspicous IP list", ips)
#First and last IP is displayed
print("First IP", ips[0]) #Index 0 is first item
print("Last IP", ips[-1]) #Index -1 is the last item

#Add new IP address
add_ip(ips)

#Change existing IP address
change_ips(ips)

#Remove existing IP address
remove_ip(ips)

#Display the total number of IP addresses
#len returns how many items are in list
print("Total IP addresses:", len(ips))

#Search for IP address
search_ip(ips)

#Final list is shown
print("Final list:", ips)




    
