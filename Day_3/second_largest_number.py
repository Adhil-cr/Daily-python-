# nums = [10,4,76,6,56,7]
nums = []
limit = int(input("enter the limit:"))

# Reading list 
for i in range(limit):

    value = int(input(f"enter number i+1 = "))
    nums.append(value)

print("Orgina list:",nums)
len_nums = len(nums)

# Selection sort → O(n²)
for i in range(len_nums):
    smallest_index = i
    smallest_value = nums[i]
    # print(f"Smallest position{smallest_index} and Smallest value {smallest_value}")
    for j in range(i+1,len_nums):
        if nums[j] < nums[smallest_index]:
            # print(j,"-",nums[j])
            smallest_index = j
            smallest_value = nums[j]
            # print(f"Updated - Smallest index ={smallest_index} and Smallest value = {smallest_value} ")

    nums[i], nums[smallest_index] = nums[smallest_index], nums[i]

# Sorted list
print(f"Sorted list :{nums}")

# Second largest element
print(f"Second largest number in this list is {nums[len_nums-2]}")


 
# - - - - Time complexity O(n) - - - -


# nums = [54,63,1,34,2]
# 
# largest = second_largest = float('-inf')
# 
# for n in nums:
#     if n > largest:
#         second_largest = largest
#         largest = n
#     
#     elif n > second_largest and n != largest:
#         second_largest = n
# 
# 
# print(f'Second largest number in the list is {second_largest}')