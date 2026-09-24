n = int(input("masukkan nilai n untuk bilangan ganjil: "))

print(f"Bilangan ganjil dari 1 sampai {n}:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()