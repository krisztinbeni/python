# 1. 1-tea
    # 2-kávé
    # 3-víz

szam: int = None
data: str = ""

print("1 - tea")
print("2 - kávé")
print("3 - víz")

while (szam == None or szam < 1 or szam > 3):
    data = input("Adja meg az innivaló számát: ")
    if (data.replace("-", "").isnumeric()):
        szam = int(data)
        if (szam < 1 or szam > 3):
            print("Nem kap üdítőt!")
    else:
        print("Nem kap üdítőt!")

if (szam == 1):
    print("tea")
elif (szam == 2):
    print("kávé")
elif (szam == 3):
    print("víz")
else:
    print("Nem kap üdítőt!")