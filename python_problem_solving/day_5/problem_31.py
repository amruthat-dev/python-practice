positive_count = 0
positive_sum = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number < 0:
        continue
    positive_count += 1
    positive_sum += number

print(f"Total positive numbers:{positive_count}")
print(f"sum of positive numbers:{positive_sum}")