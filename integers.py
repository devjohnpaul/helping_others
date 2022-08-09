# Helping Jan Henric
# Problem:
# Write a program that accepts three
# integers. The program should
# determine the highest and the
# lowest integers.
# The program should display the sum
# of the lowest and highest integers on
# the screen. You can use any selection
# control structures.
# Sample Run
# Enter integer1: 5
# Enter integer2: 7
# Enter integer3: 3
# Lowest: 3
# Highest: 7
# Sum: 10

integer_1 = int(input("Enter integer 1: "))
integer_2 = int(input("Enter integer 2: "))
integer_3 = int(input("Enter integer 3: "))


def lowest(integer1, integer2, integer3):
    if (integer1 < integer2) and (integer1 < integer3):
        global lowest_num
        lowest_num = integer1
    elif (integer2 < integer1) and (integer2 < integer3):
        lowest_num = integer2
    else:
        lowest_num = integer_3
    print("Lowest: ", lowest_num)


def highest(integer1, integer2, integer3):
    if (integer1 > integer2) and (integer1 > integer3):
        global highest_num
        highest_num = integer_1
    elif (integer_2 > integer_1) and (integer_2 > integer_3):
        highest_num = integer_2
    else:
        highest_num = integer_3
    print("Highest:", highest_num)


lowest(integer_1, integer_2, integer_3)
highest(integer_1, integer_2, integer_3)
print("Sum:", lowest_num + highest_num)
