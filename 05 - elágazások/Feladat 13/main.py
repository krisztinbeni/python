print("x =")
x: int = int (input())

if (x >= 0 and x <= 9):
    print(f"A {x} egyjegyű szám.")
elif (x >= 10 and x <= 99):
    print(f"A {x} kétjegyű szám.")
elif (x >= 10 and x <= 999):
    print(f"A {x} háromjegyű szám.")
else:
    print(f"Nem egy, kettő, három jegyű a {x}")