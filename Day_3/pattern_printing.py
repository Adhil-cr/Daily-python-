limit = int(input("Enter a number : "))

# Outer loop for line switching and number of lines 
for i in range(1,limit+1):
    
    # Inner loop for printing "*"
    for j in range(i):
        print('* ',end=" ")

    print()

