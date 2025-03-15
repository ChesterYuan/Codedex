rows = 5
for i in range(1, rows + 1):
    # Print spaces first
    print(" " * (rows - i), end="")
    # Then print the 1s
    print("1" * (2 * i - 1))
