count = 0
while count < 5:
    number = int(input("Enter a number: "))
    if number <= 0:
        count += 1
        continue
    else:
        print(f"{number} is positive number")
        count += 1