#Task 4 Unique IP Address Analyser using Sets

#A set keeps only one copy of each value, a list is used here because it allows repeated values
log_ips = [
    "192.168.1.15", "10.0.0.23", "192.168.1.15", "172.16.5.9", "10.0.0.23", "203.0.113.45", "192.168.1.15", "198.51.100.7",
]
print("Log entries (with duplicates):", log_ips)
print("Number of log entries:", len(log_ips))

#set() automatically removes duplicate values
unique_ips = set(log_ips)

#Sets are unordered so the display order may change
print("\nUnique IP addresses:", unique_ips)

def add_ip(ip_set):
    new_ip = input("\nEnter an IP address to add: ").strip()
    #add() inserts the item, if it already exists in the set, it does nothing
    ip_set.add(new_ip)
    print(new_ip, "added.")

def remove_ip(ip_set):
    ip = input("\neEnter an IP address to remove: ").strip()
    #Check first, because remove() causes an error if item is missing
    if ip in ip_set:
        ip_set.remove(ip) #remove() deletes the item from the set
        print(ip, "removed.")
    else:
        print(ip, "not found in the set.")

def check_ip(ip_set):
    ip_input = input("\nEnter an IP address to check: ").strip()
    #The 'in' operator returns true if the item is in the set
    if ip_input in ip_set:
        print(ip_input, "is in the set.")
    else:
        print(ip_input, "is not in the set.")

#Calls the functions to work with the set
add_ip(unique_ips)
remove_ip(unique_ips)
check_ip(unique_ips)

#len() counts the elements in the set
print("\nUpdated unique IP addresses:", unique_ips)
print("Number of unique IP addresses:", len(unique_ips))