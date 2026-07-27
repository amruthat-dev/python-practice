age = int(input("Enter age: "))
degree = input("Do you have a degree? (yes/no): ")

if age >= 21:
    if degree.lower() == "yes":
        print("Eligible for Job")
    else:
        print("you shoud complete your degree")
else:
    print("Not Eligible")