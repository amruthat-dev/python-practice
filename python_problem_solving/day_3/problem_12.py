username = input("Enter your user name: ")
password = input("Enter your password: ")
if username != "admin" and password != "python123":
    print("Invalid username and password")
elif username != "admin":
    print("Invalid username")
elif password != "python123":
    print("Invalid password")       
else:
    print("Login successful")