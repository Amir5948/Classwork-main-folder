#Task 3: Converting eggs into gross dozen and single eggs

def convert_eggs(eggs):
    #144 eggs in one gross
    gross = eggs // 144
    remaining = eggs - gross * 144

    #12 eggs in one dozen
    dozen = remaining // 12
    singles = remaining - dozen * 12
    return gross, dozen, singles

#Accept a whole number of eggs from user
eggs = int(input("Enter the number of eggs: "))

#Convert the eggs and display the result
gross, dozen, singles = convert_eggs(eggs)
print(f"{eggs} eggs is {gross} gross eggs + {dozen} dozen eggs + {singles} eggs")
                                                                                                                                                                        