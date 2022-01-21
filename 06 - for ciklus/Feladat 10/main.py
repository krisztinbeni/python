sum: int=0
szorzat: int=1

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    sum += i
    szorzat *= i

print(f"A számok összege {sum}. A számok szorzata {szorzat}.")