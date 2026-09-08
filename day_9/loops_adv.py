#looping through a list
#sum of all numbers in a list 
list = [23, 45, 67, 89, 12]
total = 0
for num in list:
    total += num

print(f"Sum of all numbers in the list is: {total}")


#doubling each number in list
l = [23, 45, 67, 89, 12]
dl = []
for num in l:
    dl.append(num * 2)
print(f"Doubled list is: {dl}")


#looping through a dictionary
student_marks = {"John": 85, "Alice": 92, "Bob": 78, "Eve": 90}
for student in student_marks.keys():
    print(student)

for marks in student_marks.values():
    print(marks)
    
for student, marks in student_marks.items():
    print(f"{student} --- {marks}")
