eredmeny: int=0

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 2 != 0 and i % 3 == 0):
        eredmeny += i  

print(f"{eredmeny} db páratlan és hárommal osztható szám van.")