smallest = 0
found_positive = False

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number < 0:
        continue

    if found_positive == False:
        smallest = number
        found_positive = True

    elif number < smallest:
        smallest = number

if found_positive:
    print(f"Smallest positive number: {smallest}")
else:
    print("No positive numbers entered.")