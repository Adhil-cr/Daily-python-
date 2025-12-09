# take a string input and count how many vowels (a,e,i,o,u)are in it.

word = input("enter a word:")
print(word)

count = 0
vowels = ['a','e','i','o','u']

#
for i in word:
    for j in vowels:
        if j==i:
            count+=1

print(f'Count :{count}')