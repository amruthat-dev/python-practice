unit = int(input("Enter the number of units used: "))
if unit <= 100:
    print(f"Your total bill is : {unit * 2}")
elif unit <= 200:
    print(f"Your total bill is : {100 * 2 + (unit - 100) * 3}")
elif unit <= 300:
    print(f"Your total bill is : {100 * 2 + 100 * 3 + (unit - 200) * 5}")
else:
    print(f"Your total bill is : {100 * 2 + 100 * 3 + 100 * 5 + (unit - 300) * 7}")