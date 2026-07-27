number = int(input("Enter a number: "))
if number%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible for voting.")

number1 = int(input("Enter a number: "))
if number1 > 0:
    print("positive number")
else:
    print("negative number")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > b:
    print(f"{a} is larger number")
else:
    print(f"{b} is larger number")

password = input("Enter your password: ")
if password == "python@123":
    print("Login successful")
else:
    print("Enter the correct password")