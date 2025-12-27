num = int(input('Enter a number :'))

a = 0
b = 1
c = 0 

temp = 1
print(a,end=" ")

while temp<num :
    a = b
    b = c
    c = a+b
    print(c,end=" ")

    temp +=1

# Version 2
num = int(input("Enter a number:"))
a, b = 0, 1

for _ in range(num):
    print(a,end=" ")
    a,b = b , a+b