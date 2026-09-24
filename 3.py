n = int(input("Enter a number: "))

a, b, c = 0, 1, 1
print("Fibonacci sequence:")
while c <= n:
    print(c, end=" ")
    a, b = b, a + b
print