marks = int(input("Enter your marks of previous semester: "))
attendance = int(input("Enter your attendance percentage: "))
if marks >= 80 and attendance >= 75:
    print("You are eligible for scholarship")
elif marks < 80 and attendance >= 75:
    print("You are not eligible for scholarship. Your marks are less than 80")
elif marks >= 80 and attendance < 75:
    print("You are not eligible for scholarship, Your attendance is less than 75%")
else:
    print("You are not eligible for scholarship. Your marks are less than 80 and attendance is less than 75%")