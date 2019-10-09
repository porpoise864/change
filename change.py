# Author: Sarah Oertly
# Date: 10/8/2019
# Description: The program will prompt the user to ask for an integer number of cents from 0 to 99.
# The program calculates and outputs the fewest total number of coins required to get those cent amount.
print("Please enter an amount in cents less than a dollar.")
amount = float(input())
Q = (amount % 25) + ((amount % 25)-(amount % 25))
D = (amount % 25) / 10 - (amount % 25) / 10
N = (amount % 25) / 5
P = ((amount % 25) / 5) - 1

print("Your change will be: ", "Q: ", Q, "D: ", D, "N: ", N, "P: ", P)
