i = 1
while True:
    if i%2 != 0:
        i += 1
        continue
    print(f"Try {i}")
    i += 1
    if i > 100:
        break 