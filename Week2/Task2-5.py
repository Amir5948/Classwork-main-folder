#Task 5: Multiplaction table from 1 to 10

def display_table(number):
    #range (1,11) gives numbers 1 to 10
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

#Ask user to enter number
number = int(input("Enter a number: "))

#Display its multiplication table
display_table(number)