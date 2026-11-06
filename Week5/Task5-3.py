#Task 3: Security Incident Manager using Dictionaries

# Dictionary stores information about a security incident as key-value pairs, and can be updated after its created.
#Dictionary uses curly brackets {} and stores information as key vlaue pairs
incident = {
    "username": "smith",
    "ip_address": "192.168.1.15",
    "event_type": "Failed login",
    "severity": "Medium",
}

def show_incident(record):
    #items() gives each key together with its value
    for key, value in record.items():
        print(f" {key}: {value}")

#Values are accessed using their keys inside square brackers []
print("Username: ", incident["username"])
print("IP address:", incident["ip_address"])

#Added a new field called status
incident["status"] = "Under Investigation"
print("\nAfter adding status:")
show_incident(incident)

#Updated the risk level, assigning to an exisiting key replaces the old value
incident["risk_level"] = "High"
print("\nAfter updating risk level:")
show_incident(incident)

#Removes the key and the value from the dictionary
del incident["event_type"]

#Displays all the remaining keys and values
#keys() returns the keys and values() returns the values and items() returns both as pairs
print("\nRemaining keys: ",list(incident.keys()))
print("Remaining values: ",list(incident.values()))
print("Remaining key-value pairs:")
show_incident(incident)

#len() counts how many pairs the dictionary holds
print("\nTotal key-value pairs: ", len(incident))
