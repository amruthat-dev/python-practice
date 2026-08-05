i = 1
while i <=5:
    print(i)
    i +=1

i = 1
while i <= 10:
    print(i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1

i = 2
while i <= 20:
    print(i)
    i += 2

i = 1
while i <= 19:
    print(i)
    i += 2

i = int(input("Enter a number: "))
while i <= 5 and i >= 1:
    print(i)
    i -= 1

    
#multiplication table of a number using while loop
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1


#sum of first 10 natural numbers using while loop
total = 0
i = 1
while i <= 10:
    total += i
    i += 1

print(f"Sum of first 10 natural numbers is: {total}")


#factorial of a number using while loop
number = int(input("Enter a number: "))
factorial = 1
i =1
while i<= number:
    factorial *= i
    i += 1

print(f"Factorial of {number} is: {factorial}")