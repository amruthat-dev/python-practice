fruits = {"apple", "cherry", "banana"}
print(fruits)
fruits.add("orange")
fruits.remove("banana")
print("apple" in fruits)
print(fruits)

fruits1 = {"apple", "banana", "mango"}
fruits1.add("orange")
fruits1.add("grapes")
fruits1.remove("apple")
print("banana" in fruits1)
print(fruits1)
fruits1.discard("orange")
removed = fruits1.pop()
print(f"removed element : {removed}")
print(f"final result : {fruits1}")


A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)

numbers = {20, 40, 60, 80, 100}

print(len(numbers))
print(max(numbers))
print(min(numbers))

