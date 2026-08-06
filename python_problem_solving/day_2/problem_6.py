#largest of three numbers
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if a >= b and a >= c:
    print(f"{a} is largest number")
elif b >= a and b >= c:
    print(f"{b} is largest number")
else:
    print(f"{c} is largest number")
