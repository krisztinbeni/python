print("x =")
x: int = int (input())

print("y =")
y: int = int (input())

print("z =")
z: int = int (input())

if (x % y == 0 and x % z == 0):
    print(f"A {x} osztható {y} és {z}")
elif (x % y == 0):
    print(f"A {x} osztható {y}.")
elif (x % z == 0):
    print(f"A {x} osztható {z}")
else:
    print(f"A {x} nem osztható {y}, {z}.")