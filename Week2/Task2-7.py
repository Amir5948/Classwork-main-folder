#Task 7: Printing the first 20 terms of the fibonacci series

def display_fibonacci(count):
    #First 2 terms are 0 and 1
    current = 0
    following = 1

    for i in range(count):
        if i < count -1:
            #end="," keeps the output on same line
            print(current, end=",")
        else:
            #Last term ends the line
            print(current)

        #Next term is the sum of previous 2 terms
        current, following = following, current + following

#Print first 20 terms
display_fibonacci(20)