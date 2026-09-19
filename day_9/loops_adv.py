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


#using enumerate to get index and value
students = ["John", "Alice", "Bob", "Eve"]
for index, student in enumerate(students):
    print(f"Index: {index}, student: {student}")


students = ["John", "Alice", "Bob", "Eve"]
marks = [85, 92, 78, 90]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)


#creating a list of squares using list comprehension
#exp for item in collection
l = [1, 2, 3, 4, 5]
dl = [num ** 2 for num in l]
print(dl)                   

l = [x for x in range(1,101)]
dl = [x**2 for x in l]
print(dl)
