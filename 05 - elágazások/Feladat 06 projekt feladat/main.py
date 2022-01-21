print("x =")
x: int = int (input())

print("y =")
y: int = int (input())

print("z =")
z: int = int (input())

if (x > y > z):
    print(f"{z}, {y}, {x}")
elif (x > z > y):
    print(f"{y}, {z}, {x}")
elif (y > x > z):
    print(f"{z}, {x}, {y}")
elif (y > z > x):
    print(f"{x}, {z}, {y}")
elif (z > x > y):
    print(f"{y}, {x}, {z}")
elif (z > y > x):
    print(f"{x}, {y}, {z}")
else:
    print(f"{x}, {y}, {z}")