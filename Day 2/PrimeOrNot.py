num = int(input('Enter a number:'))

if num <= 1:
    print('Not a prime number')
else :
    for i in range(2,num):
        if num % i == 0:
            print('Not a prime number')
            break
    else :
        print('Prime number')


# # pythonic way

# num = int(input('enter a number :'))
# if num > 1 and all(num % i != 0 for i in range(2,num)):
#     print('Prime number')
# else :
#     print('Not a prime number')
