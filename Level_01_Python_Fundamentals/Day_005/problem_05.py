'''
Problem: Ask the user for a positive integer n.
         For every number from 1 through n, print whether it is: Even or Odd
         Additionally, maintain separate counts for each category.

Example:

Input:
5

Output:
1 - Odd
2 - Even
3 - Odd
4 - Even
5 - Odd


Even Count: 2
Odd Count: 3

Constraints:
- n > 0
- Use a for loop.
- Do not manually write individual checks for each number.

Edge Cases:
- n = 1
- n = 2
- Large n

Hints:

You need:

iteration
+
condition
+
two counters

'''

# Algorithm
# 1. Initialize even_counter and odd_counter for store total counts
# 2. Read and validate an integer from user


# Initializing counter variables
even_counter = 0
odd_counter = 0

# Reading and validating user input
while True :
    user_input = int(input("Enter an integer : "))

    if user_input > 0 :
        break
    else :
        print("Invalid Input ,Try again")

for number in range(1,user_input+1):
    if number % 2 == 0 :
        print(f"{number} - Even")
        even_counter += 1

    else :
        print(f"{number} - Odd")
        odd_counter += 1

print(f"Even count : {even_counter}")
print(f"Odd count : {odd_counter}")
