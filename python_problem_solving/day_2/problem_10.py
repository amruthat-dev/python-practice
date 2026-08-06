pin = int(input("Enter your PIN: "))
if pin == 1234:
    print("Login successful")
    balance = 5000
    amount = int(input("Enter the withdrawal amount: "))
    if amount <= balance:
         print(f"withdrawal of {amount} is successful. Please collect your cash. your remaining balance is {balance-amount}")
    else:
         print("Insufficient balance")
else:
    print("Invalid PIN")