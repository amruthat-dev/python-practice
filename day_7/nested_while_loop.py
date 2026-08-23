i = 0
while i <= 10:
    x = 0   
    while x < i:
        print("Amrutha")
        x += 1
    i += 1

pin = " "
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your pin: ")
    if pin != correct_pin:
        print("incorrect pin! Try again")
        
print("correct pin")