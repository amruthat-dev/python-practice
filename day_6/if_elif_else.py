marks = int(input("Enter your marks: "))
if marks >=90:
    print("Grade A+")
elif marks >=75:
    print("Grade A")
elif marks >=50:
    print("Grade B")
elif marks >=35:
    print("Grade C")
else:
    print("Fail")

age = int(input("Enter your age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("teenager")
elif age <=59:
    print("adult")
else:
    print("senior citizen")