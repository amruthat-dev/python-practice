while True:
    num = int(input("Enter a number: "))
    if num == 0:
       break


while True:
    num = int(input("Enter a number: "))
    if num < 0:
        continue
    if num == 0:
        break
    print(num)