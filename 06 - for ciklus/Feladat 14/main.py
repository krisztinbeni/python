ottelOszthatoSzamokOsszege: int=0
hettelOszthatoSzamokOsszege: int=0
ottelEsHettelOsztahtó: int=0

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 5 == 0 and i % 7 == 0):
        ottelOszthatoSzamokOsszege += i
        hettelOszthatoSzamokOsszege += i
    elif (i % 5 == 0):
        ottelOszthatoSzamokOsszege += i
    elif (i % 7 == 0):
        hettelOszthatoSzamokOsszege += i
    else:
        ottelEsHettelOsztahtó += i

if (hettelOszthatoSzamokOsszege and ottelOszthatoSzamokOsszege == ottelEsHettelOsztahtó):
    print(f"Az öt és a hét ugyanannyiszor van meg benne.")
elif (hettelOszthatoSzamokOsszege > ottelOszthatoSzamokOsszege):
    print(f"A héttel osztható számok összege a nagyobb.")  
elif (ottelOszthatoSzamokOsszege > hettelOszthatoSzamokOsszege):
    print(f"Az öttel osztható számok összege a nagyobb.")
else:
    print(f"Az öttel és a héttel osztható számok összege egyenlő.") 