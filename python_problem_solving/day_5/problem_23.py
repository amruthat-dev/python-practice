age = int(input("Enter your age: "))
if age <= 0:
    print("Invalid age. Please enter your valid age.")
elif age < 5:
    print(f"Your age is {age}. you got a free ticket for the movie.")
elif age <= 12:
    print(f"Your age is {age}. your ticket price is 100 ruppes.")
elif age <= 59:
    print(f"Your age is {age}. your ticket price is 200 ruppes.")
else:
    print(f"Your age is {age}. your ticket price is 120 ruppes.")
