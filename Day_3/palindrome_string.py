word = input('Enter a string :')
length_word = len(word)
print(type(length_word))

print(length_word)
is_palindrome = True

for i in range(length_word // 2):

    if word[i] != word[length_word - 1 - i]:
        is_palindrome = False
        break

if is_palindrome :
    print(word,' is palindrome')
else :
    print('Is not palindrome')