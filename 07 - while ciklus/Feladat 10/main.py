n: int = None
data: str = ""
ottelOszthatoSzam: int = 0
tizeneggyelOszthatoSzam: int = 0

while (n == None or n < 0 or n > 99):
    data = input("Adjon meg 0-nál nagyobb és 99-nél nem nagyobb aszámot: ")
    if (data.replace("-", "").isnumeric()):
        n = int(data)
        if (n < 0 or n > 99):
            print("Nem jó számot adott meg!")
    else:
        print("Nem számot adott meg!")

for i in range(0, n+1, 1):
    if (i % 2 == 0):
        print(i, end=" " "\n")

for j in range(0, n+1, 1):
    if (j % 5 == 0):
        ottelOszthatoSzam += j

for k in range(0, n+1, 1):
    if (k % 11 == 0):
        tizeneggyelOszthatoSzam += k

print(f"5-tel osztható számok összege: {ottelOszthatoSzam}")
print(f"11-el osztható számok száma: {tizeneggyelOszthatoSzam}")
    
for l in range(0, n+1, 1):
    if (l % 7 == 3):
        print(l, end = " ")