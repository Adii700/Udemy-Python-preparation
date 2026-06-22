# Pyramid using asterisks
n = int(input("Enter the height of pyramid: "))

print("\n--- Simple Pyramid ---")
for i in range(1, n + 1):
    print("*" * i)

print("\n--- Centered Pyramid ---")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("\n--- Inverted Pyramid ---")
for i in range(n, 0, -1):
    print("*" * i)