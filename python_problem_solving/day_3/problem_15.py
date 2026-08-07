library_card = input("Do you have a library card? (yes/no): ")
pending_fine = input("Do you have any pending fine? (yes/no): ")
library_card = library_card.lower()
pending_fine = pending_fine.lower()
if library_card == "yes" and pending_fine == "no":
    print("You are eligible to borrow books from library")
elif library_card == "no" and pending_fine == "no":
    print("You are not eligible to borrow books from library. You need to have a library card. please apply for library card first")
elif library_card == "yes" and pending_fine == "yes":
    print("You are not eligible to borrow books from library. You have pending fine. please clear your fine first")
else:
    print("You are not eligible to borrow books from library. You need to have a library card and clear your pending fine first")
