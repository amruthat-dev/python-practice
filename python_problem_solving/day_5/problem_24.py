attempt = 0
while attempt < 3:
    pin = (input("Enter your PIN: "))
    if pin == "1234":
        print("Login successful")
        break
    else:
        print("Incorrect password")
        attempt += 1
if attempt == 3:
    print("account tempararily locked")
       