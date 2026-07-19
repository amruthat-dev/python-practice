tuple1 = ("Python", "Java")
tuple2 = ("C", "C++")
tuple3 = tuple1 + tuple2
print(tuple3)

colors = ("Red", "Blue")
print(colors * 3)

subjects = ("Python", "ADA", "DBMS")
print("Python" in subjects)
print("Biology" not in subjects)

numbers = (10, 20, 30, 40, 50)
print(len(numbers))

numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

fruits = ("Apple", "Banana", "Mango")
print(fruits.index("Banana"))

college_info = ("Acharya", "Bangalore", "AIML")
college, city, Branch = college_info
print(college)
print(city)
print(Branch)   