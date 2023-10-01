# This program calculates and diplays travel expenses
# 09/29/2023
# CTI-110 P1HW2 - Travel Expense
# Derek Paci
#


print('This program calculates and displays travel expense')

print('Enter budget:', end ='')
num1 = int(input())

print('Enter travel destination:', end ='')
num2 = input()

print('How much do you think you will spend on gas?', end ='')
num3 = int(input())

print('Approximately, how much will you need for accomodation/hotel?', end ='')
num4 = int(input())

print('Last, how much do you need for food?', end ='')
num5 = int(input())

print('-------Travel Expenses------')
print('Location:', num2)
print('Initial Budget:', num1)
print()

print('Fuel:', num3)
print('Acommodation:', num4)
print('Food:', num5)
print()

print('Total expense:', end ='')
print(num3 + num4 + num5)
print()

print('Remaining balance:', end ='')
print(num1 - num3 - num4 - num5)
print()














