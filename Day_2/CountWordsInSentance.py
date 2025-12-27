sentance = input('Enter a sentance :')
print(f'The sentance : {sentance}')
print(type(sentance))

count = len(sentance.split())
print(f'word count : {count}')


# # Manual counting logic 
# sentance = input('Enter a sentance :')
# print(f'The sentance : {sentance}')

# count = 0 
# in_word = True


# for ch in sentance:
#     if ch != ' ' and not in_word:
#         count += 1
#         in_word = True
#     elif ch == ' ':
#         in_word = False

# print(f"Word count: {count}")
