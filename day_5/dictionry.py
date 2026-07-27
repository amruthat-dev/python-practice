student = {
    "name" : "amrutha",
    "age" : 21,
    "branch" : "CSE"
}
print(student)
print(student["name"])
print(student["age"])
print(student.get("branch"))
print(student.get("city"))

student1 = {
    "name": "Amrutha",
    "age": 21
}
student1["branch"] = "CSE"
student1["college"] = "Acharya"
student1["age"] = 22
print(student1)

student2 = {
    "name": "Amrutha",
    "age": 21,
    "branch": "CSE",
    "college": "Acharya"
}
removed_value = student2.pop("branch")
print(f"Removed value : {removed_value}")

print(student2)
del student2["college"]
print(student2)
student2.clear()
print(student2)

student3 = {
    "name": "Amrutha",
    "age": 21,
    "branch": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())
print(len(student))
print("name" in student)
print("city" in student)