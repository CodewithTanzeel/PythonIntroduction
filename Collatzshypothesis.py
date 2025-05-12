c0 = int(input("Enter a any non-negative and non-zero integer number"))

c0 = int(input("Enter a non-negative and non-zero integer: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(c0)

print(f"Total steps: {steps}")
