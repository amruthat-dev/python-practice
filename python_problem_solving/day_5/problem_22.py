temp = int(input("Enter the temperature in Celsius: "))
if temp < 0:
    print(f"The temperature {temp}°C is the freezing point.")
elif temp <= 15:
    print(f"The temperature {temp}°C is cold.")
elif temp <= 30:
    print(f"The temperature {temp}°C is normal.")
else:
    print(f"The temperature {temp}°C is Hot.")