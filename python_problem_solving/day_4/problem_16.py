balance = 5000
amount = int(input("Enter the amount to withdraw: "))
if amount > 0 and amount <= balance:
    print("withdrawal successful.")
elif amount > 0 and amount > balance:
    print("withdrawal failed. Insufficient balance.")
elif amount <= 0 and amount <= balance:
    print("withdrawal failed. Please enter a valid amount.") 
else:
    print("withdrawal failed. Please check the amount and try again.")