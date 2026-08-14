positive_sum = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number < 0:
        continue
    else:
        positive_sum += number

print(f"Total positive sum: {positive_sum}")
