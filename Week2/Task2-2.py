#Task 2: Convert GMT to PST to CET

def convert_hours(hours, offset):
    #Return the hour in another timezone using 24 hour clock
    return (hours + offset) % 24

#Ask the user for the time in GMT (24 hour clock)
gmt_hours = int(input("Enter the hours in GMT (0-23): "))
gmt_minutes = int(input("Enter the minutes in GMT (0-59)"))

#PST is GMT -8 and CET is GMT +1 (Minutes stay the same)
pst_hours = convert_hours(gmt_hours, -8)
cet_hours = convert_hours(gmt_hours, 1)

#Output the time in each zone
print(f"PST: {pst_hours:02d}:{gmt_minutes:02d}")
print(f"CET: {cet_hours:02d}:{gmt_minutes:02d}")