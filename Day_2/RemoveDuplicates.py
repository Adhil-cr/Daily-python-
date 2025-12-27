# Remove Duplicates From List

# Orginal list
nums = [1,2,3,4,5,5,5,3,1,6]

# Empty new list 
new_list = []
print(type(new_list))

# Boolean flag to track whether the current number already exists in new_list
not_existed = False

# Outer for loop for iterate through each number of Orginal list
for i in nums:

    # Assuming that the current number does not exits in the new_list 
    not_existed = True

    # If new list is empty.Then the first element must be unique, so add it
    if not new_list:
        new_list.append(i)

    # Compare the current number with each element already in new_list
    for j in new_list:

        # if a match found , the number already exists
        if i == j :
            not_existed = False # Mark as already exits (duplicate)
            break # Stop checking further elements 

    # After checking all existing elements,
    # if the number was never found, add it to new_list
    if not_existed == True:
        new_list.append(i)


# Final list with no duplicates 
print(new_list)
        
        