from matematikaFuggvenyek import *
from inputLib import *

osszeg: float = None
kulombseg: float = None
szorzat: float = None
hanyados: float = None

x: float = None
y: float = None

x = tizedesSzamBeolvasasa("Kérem az X értéket: ")
y = tizedesSzamBeolvasasa("Kérem az Y értéket: ")

osszeg = osszeadas(x, y)
kulombseg = kivonas(x, y)
szorzat = szorzas(x, y)
hanyados = osztas(x, y)

print(f"\n{x} + {y} = {osszeg}")
print(f"\n{x} - {y} = {kulombseg}")
print(f"\n{x} * {y} = {szorzat}")
print(f"\n{x} / {y} = {hanyados}")