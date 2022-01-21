print("x =")
x: int = int (input())

if (x % 4 == 0 and x % 6 == 0):
    print(f"{x} osztható 4-gyel vagy 6-tal.")
else:
    print(f"{x} egyikszámmal sem osztható.")