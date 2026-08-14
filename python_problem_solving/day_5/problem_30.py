largest = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number < 0:
        continue
    if number > largest:
        largest = number
print(f"largest number: {largest}")