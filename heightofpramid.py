blocks = int(input("Enter the number of blocks: "))

height = 0

while True:
    required = (height + 1) * (height + 2) * (2 * (height + 1) + 1) // 6
    if required <= blocks:
        height += 1
    else:
        break
print("The height of the pyramid:", height)

