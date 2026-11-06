#Task 1: Arithmetic operations on 2 values

def display_results(first, second):
    #Display results on 2 values
    print("Sum:", first + second)
    print("Product:", first * second)
    print("Second value subtracted from the first value:", first - second)
    print("First value divided by the second value:", first / second)
    print("Integer divison:", first//second)
    print("Modulus:", first % second)
    print("First value raised to the power of the second value:", first ** second)

#Request the two values from the user
first_value = int(input("Enter the first value: "))
second_value = int(input("Enter the second value"))

#Calls the function to output the results
display_results(first_value, second_value)