#count the number of digits in a number using while loop
number = int(input("Enter a number: "))
count = 0
while number > 0:
    number //= 10
    count += 1

print(f"Number of digits in the number is: {count}")


#reverse a number using while loop
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print(f"Reverse of the number is: {reverse}")
