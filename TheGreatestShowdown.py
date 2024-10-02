# Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your 
# code should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest
# number among the three and print it out.

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"The smallest number is {smallest}. The largest number is {largest}")