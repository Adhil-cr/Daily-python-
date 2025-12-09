## Take 3 input from the user and print the largest among them
#num1 = int(input('Enter 3 numbers :'))
#num2 = int(input())
#num3 = int(input())
#
#if num1>num2:
#    if num1>num3:
#        print(f"{num1} is greter")
#    else:
#        print(f'{num3} is greater')
#else:
#    if num2>num3:
#        print(f'{num2} is greater')
#    else:
#        print(f'{num3} is grater')
#

# Solution in pythonic way

a, b, c = (int(input('enter the number:')) for _ in range(3))
print(f"{max(a, b, c)} is greater")