unit = int(input("Enter the number of electricity unit used: "))
if unit <= 100:
    print(f"{unit * 2} rupees per unit")
elif unit <= 300:
    print(f"{unit * 5} rupees per unit")
else:
    print(f"{unit * 8} rupees per unit")