'''
Student Marks Analyzer

Build a CLI program that analyzes student marks.

The program should first ask:

How many students?:

Then collect the marks for each student.

For example:

How many students?: 5


Enter mark for student 1: 78
Enter mark for student 2: 65
Enter mark for student 3: 91
Enter mark for student 4: 42
Enter mark for student 5: 88

Then produce:

===== Student Marks Report =====


Students: 5
Highest Mark: 91
Lowest Mark: 42
Average Mark: 72.8


Passed: 4
Failed: 1
Rules

Passing mark:

40

A student passes if:

mark >= 40
Requirements

Your program must calculate:

Number of students
Highest mark
Lowest mark
Average mark
Number of passed students
Number of failed students
Restrictions

For the main analysis:

Use a for loop.
Do not use max() or min().
Maintain the required values yourself.

Edge Cases:
Think about:
1 student
all students pass
all students fail
same mark for everyone
mark = 0
mark = 100
'''

# Algorithm
# 1. Initialize total_marks, passed_students, failed_students.
# 2. Read and validate number of students.
# 3. For each student:
#    a. Read and validate mark.
#    b. If this is the first student:
#       - Set highest = mark
#       - Set lowest = mark
#    c. Compare mark with highest.
#    d. Compare mark with lowest.
#    e. Add mark to total_marks.
#    f. Update passed/failed count.
# 4. Calculate average.
# 5. Display the report.



# Initialize variables
total_marks = 0
passed_students = 0
failed_students = 0


# Reading and validating user_input number_of_students
while True:
    number_of_students = int(input('How many students?:'))

    if number_of_students > 0 :
        break
    else : 
        print("Invalid Input , Try again")

# Reading marks of each student
for student in range(1,number_of_students+1):
   
    while True:
        mark = int(input(f'Enter mark for student {student}: '))
        if mark < 0 or mark > 100 :
            print("Invalid Mark , Try again")
        else :
            break

    # Initialize highest and lowest using the first mark.
    if student == 1 :
        lowest_score = mark
        highest_score = mark

    # validating pass or fail
    if mark >= 40:
        passed_students +=1
    else :
        failed_students +=1

    # Finding largest and lowest
    if mark > highest_score:
        highest_score = mark

    if mark < lowest_score :
        lowest_score = mark

    # Storing mark for calculate average 
    total_marks += mark

print('===== Student Marks Report =====')

print(f"Students: {number_of_students}\n" 
f"Highest Mark: {highest_score}\n"
f"Lowest Mark: {lowest_score}\n"
f"Average Mark: {total_marks/number_of_students}\n\n"

f"Passed: {passed_students}\n"
f"Failed: {failed_students}"
)
