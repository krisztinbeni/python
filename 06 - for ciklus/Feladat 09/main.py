print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

if (kezdoErtek % 2 == 0):
    vegErtek-=1

for i in range(vegErtek, kezdoErtek-1, -2):
    print(i)