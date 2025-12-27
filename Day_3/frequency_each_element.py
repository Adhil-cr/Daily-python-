# nums = [1,2,5,4,3,2,2,1,6]
# frequence = {}

# for i in nums:
#     count = 0
#     for j in nums:
#         if j == i :
#             count += 1

    
#     frequence[i] = count

# print(frequence)

# Time complexity → O(n) solution
nums = [1, 2, 5, 4, 3, 2, 2, 1, 6]
frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else :
        frequency[num] = 1

print(frequency)