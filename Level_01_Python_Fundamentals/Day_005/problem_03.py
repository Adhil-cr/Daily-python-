'''
Problem: Ask the user for a number and print its multiplication table from 1 to 10.

Example:

Input:
7


Output:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70

Constraints:
-Input must be an integer.

Edge Cases:
    0
    Negative numbers
    Large numbers

Hints:

Use:
range(1, 11)
'''

# Algorithm
# 1. Read and validate user input 
# 2. Using for loop calculate multiplication of the number using range(1,11)
# 3. Stop


# Reading a valid user input

while True :
    user_input = int(input("Enter an integer number :"))

    if user_input :
        break
    else :
        print("Invalid input, Try again")

# Displaying Multiplication table of the number
for number in range(1,11):
    print(f"{user_input} x {number} = {user_input * number}")