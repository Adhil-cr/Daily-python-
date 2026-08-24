'''
Problem: Ask the user for a positive integer n.
         Print all even numbers from 1 through n.

Example:

Input: 10

Output:
2
4
6
8
10

Explanation:
-Only numbers divisible by 2 should be printed.

Constraints:
-n must be a positive integer.

Edge Cases:
n = 1
n = 2
Odd n
Negative input

Hints:
-Use for.
-Think about range().
-Think about the remainder operator %.

'''

# Algorithm
# 1.Start using While True : read user_input number and validate it 
# 2.after validating start for loop with start = 2 , stop = user_input+1 , step = 2 
# 3.print each iterable number 

while True:
    user_input = int(input("Enter the number: "))

    if user_input <= 0 :
        print("-----Invalid Input-----")

    else :
        break

for even in range(2,(user_input+1),2):
    print(even)