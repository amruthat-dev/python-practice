count = 0
for i in range(1,6):
    num = int(input("Enter a number: "))
    if num > 0:
        count += 1

print(f"Total positive numbers {count}")

sum = 0
for i in range(1, 6):
    num = int(input("Enter a number: "))
    sum += num

print(f"Total sum = {sum}")

total = 0
for i in range(1, 6):
    num = int(input("Enter a number: "))
    if num > 0:
        total += num

print(f"sum of all positive numbers: {total}")