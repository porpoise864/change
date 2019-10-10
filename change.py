# Author: Sarah Oertly
# Date: 10/8/2019
# Description: Write a program that asks the user for a (integer) number of cents, from 0 to
# 99, and outputs how many of each type of coin would represent that amount with the fewest total number
# of coins. When you run your program, it should match the
# following format:
print("Please enter an amount in cents less than a dollar.")
amount = int(input())
Q = (amount / 25) % 25
D = (amount % 25) % Q
N = (D % 10) / 5
P = (N % 5) % (N / 5)
print("Your change will be:\n ","Q:", Q, "\nD: ", D, "\nN: ", N, "\nP: ", P)