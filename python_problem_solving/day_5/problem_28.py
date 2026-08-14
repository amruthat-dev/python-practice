positive_count = 0
negative_count = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number > 0:
        positive_count += 1
    else:
        negative_count += 1

print(f"positive numbers: {positive_count}")
print(f"negative numbers: {negative_count}")