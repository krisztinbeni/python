print("x =")
x: int = int (input())

if (x >= 0):
    print(f"A {x} pozitív.")
else:
    print(f"A {x} negatív.")
if (x % 2 == 0):
    print(f"A {x} páros.")
else:
    print(f"A {x} páratlan.")
if (x % 5 == 0):
    print(f"A {x} osztható 5-tel.")
else:
    print(f"A {x} nem osztható 5-tel.")