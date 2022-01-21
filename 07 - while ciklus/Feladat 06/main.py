eletkor: int = None
eletkorInput: str = ""

while(eletkor == None or eletkor < 0 or eletkor > 99):
    eletkorInput = input("Írja be az életkorát: ")
    if (eletkorInput.replace("-", "").isnumeric()):
        eletkor = int(eletkorInput)
        if (eletkor > 99 or eletkor < 0):
            print("0 és 99 közötti életkort adjon meg!")
    else:
        print("Nem számot adott meg!")

print(f"Életkora: {eletkor}")

if (eletkor >= 0 and eletkor <= 6):
    print("gyerek")
elif (eletkor >= 7 and eletkor <= 18):
    print("iskolás")
elif (eletkor >= 19 and eletkor <= 65):
    print("dolgozó")
elif (eletkor >= 65 and eletkor <= 99):
    print("nyugdíjas")
else:
    print("Túl nagy az életkora!")