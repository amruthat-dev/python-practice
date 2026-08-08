attendance = int(input("Enter your attendance percentage: "))
marks = int(input("Enter your internal marks: "))
if attendance >=75 and marks >= 40:
    print("You are eligible to write the exam.")
elif attendance < 75 and marks >= 40:
    print("You are not eligible to write the exam. Your attendance is less than 75%.")
elif attendance >= 75 and marks < 40:
    print("You are not eligible to write the exam. Your internal marks are less than 40.")
else:
    print("You are not eligible to write the exam. Your attendance is less than 75% and your internal marks are less than 40.")