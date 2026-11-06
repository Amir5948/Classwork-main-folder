# Task 2: Security Incident Record using Tuples

#A tuple stores the basic details of a security incident, a fixed record which cannot be altered after creation. 
#A tuple is created using round brackets ().
incident =  ("smith", "192.168.1.15", "Failed login", "High")

#Tuple indexes start at 0, so first item is incident[0].
print("Username: ", incident[0])
print("IP address: ", incident [1])
print("Event type: ", incident[2])
print("Severity: ", incident[3])

#len() returns how many items are in the tuple.
print("\nNumber of elements:", len(incident))

def check_event_type(record, event):
    #The 'in' operator checks if the item is true in tuple
    if event in record:
        print(f'"{event} appears in the record.')
    else:
        print(f'"{event}" does not appear in the record.')

#Checking whether event type is shown in record and one that is not.
print()
check_event_type(incident, "Failed Login")
check_event_type(incident, "Malware Detected")

#Tuples are immutable so it causes an error, try/except is used so the program does not crash when error occurs.
print("\nTrying to change the severity to 'Low'...")
try:
    incident[3] = "Low" #Not allowed: tuple items cant be reassigned
except TypeError as error:
    print("Error:", error)
    print("The tuple was not changed:", incident)
