#cancatenation of two strings
first_name = "Amrutha"
last_name = "T"
final_name = first_name +" "+ last_name
print(final_name)
#repetition
message = "warning! "
print(message * 5)
#string methods
name = "amrutha"
print(name.upper())
print(name.lower())
text = "hello, world!"
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.replace("world","ammu"))
print(len(text))
print(text.split(","))
print(name.split(","))
name = input("Enter your name: ")
print(f"The {name} in upper case {name.upper()}.")
print(f"The number of characters in {name} is {len(name)}.")
print(f"The name starts with A: {name.startswith('A')}")
print(f"The name ends with t: {name.endswith('t')}")
print(f"The {name} in lower case {name.lower()}.")
print(f"The first character of {name} is {name[0]}")
print(f"The last character of {name} is {name[-1]}.")
print(name[0:5])
print(name[:4])
print(name[::-1])
print(name[2:])
print(name[::2])
print(name[1:2])
                