num = [1,2,3,4,5,6]
print(f'Orginal list {num}')
reverser_list = []

for i in num[::-1]:
    reverser_list.append(i)

print(f'Reversed list {reverser_list}')



# # In-place reversal (NO extra list)

# num = [1,2,3,4,5,6]
# print(f'Orginal list {num}')

# left = 0 
# right = len(num)-1

# while left < right:
#     num[left] , num[right] = num[right] ,num[left] 
#     left += 1
#     right -= 1

# print(f"Reversed list: {num}") 