age = int(input("Enter your age: "))
citizen = input("Did you belong to india citizen? (yes/no): ")
if age >= 18 and citizen.lower() == "yes":
    print("You are eligible to vote")
elif age < 18 and citizen.lower() == "yes":
    print("You are not eligible to vote. You are underage")
elif age >= 18 and citizen.lower() == "no":
    print("You are not eligible to vote. You are not an Indian citizen")
else:
    print("You are not eligible to vote. You are underage and not an Indian citizen")