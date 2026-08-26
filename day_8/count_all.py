positive_count = 0
negative_count = 0
zero_count = 0
for i in range(1,11):
    num = int(input("Enter a number: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Total positive numbers : {positive_count}")
print(f"Total negative numbers : {negative_count}")
print(f"Total zero's are : {zero_count}")

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print(total)