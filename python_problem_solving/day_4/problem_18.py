purchase_amount = int(input("Enter the purchase amount: "))
if purchase_amount >= 5000:
    discount = purchase_amount * 0.20
    final_amount = purchase_amount - discount
    print(f"You are eligible for a 20% discount. Your final amount to pay is: {final_amount}")
elif purchase_amount >= 2000:
    discount = purchase_amount * 0.10
    final_amount = purchase_amount - discount
    print(f"You are eligible for a 10% discount. Your final amount to pay is: {final_amount}")
else:
    print(f"You are not eligible for any discount. Your final amount to pay is: {purchase_amount}")