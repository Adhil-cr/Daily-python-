'''
Problem: Ask the user for a string and count how many vowels it contains.

Consider:
a e i o u

and their uppercase versions.

Example:

Input:Python Programming

Output:
Vowels: 4

Explanation:

The program should inspect each character and determine whether it is a vowel.

Constraints:
-Input may contain spaces.
-Input may contain uppercase and lowercase letters.

Edge Cases:
-Empty string
-No vowels
-All vowels
-Uppercase vowels

Hints:

You can use:

for character in text:

and think about:

character in "aeiouAEIOU"
'''

# Algorithm
# 1. Initialize variable vowels="aeiouAEIOU" and count=0
# 2. Using while read a valid user_input 
# 3. Use nested for loop to iterate each character from user_input compare with each character in vowels 
# 4. when character matches any vowels increment count and continue the loop 
# 5. Stop 

# Initializing variables
vowels = "aeiouAEIOU"
count = 0

# Reading a valid user input
while True :
    user_input = input("Enter the string: ").strip()

    if user_input:
        break
    else :
        print("Please enter a valid string")

# Iterating over each character from user_input compare with vowels
for character in user_input :
    for vowel in vowels :
        if character == vowel:
            count +=1

# Displaying the result
print(f'{user_input} has {count} vowels')