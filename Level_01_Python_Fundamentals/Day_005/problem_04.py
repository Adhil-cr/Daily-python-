'''
Problem: Ask the user how many numbers they want to enter.
         Then read those numbers one by one and determine 
         the largest number without using Python's built-in: max()

Example:
Input:
5

12
7
25
3
19


Output:
Largest: 25

Explanation:
-You need to maintain a variable representing the largest value found so far.
-Think carefully about how you initialize it.

Constraints:
-At least one number will be entered.
-Do not use max().

Edge Cases:
-One number
- All numbers equal
- All numbers negative
- Largest number appears first
- Largest number appears last

Hints:

Think about the concept of a running maximum.

Don't initialize the largest value to 0 automatically. Why could that fail?

'''

# Algorithm
# 1. Initialize variables limit = 0, temp = 0
# 2. Read limit and validate it 
# 3. Read values according to limit, store the current value into temp 
# 4. Compare temp value with largest , if temp is largest number then store it into the largest 
# 5. Repeat until reaches the limit 
# 6. Print the largest variable 
# 7. Stop


# Initializing variables 
limit = 0 
temp = 0

# Reading and validating limit 
while True :
    limit = int(input('Enter the limit(minimum 1): '))

    if limit >= 1:
        break
    else :
        print("Please enter a valid limit(minimum 1)")


for number in range(1,limit+1):

    temp = int(input(f"Enter {number} number:")) 

    # Initializing largest as first real data
    if number == 1:
        largest = temp

    # Identifying the largest number
    if temp > largest :
        largest = temp


print(f"The largest number among them is {largest}")

