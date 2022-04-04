from Teglalap import Teglalap
from Kor import Kor
from Haromszog import Derekszogu, Egyenloszaru, Haromszog

# példányosítás
teglalap: Teglalap = Teglalap(10, 20)
print("\nteglalap:")
print(teglalap)

negyzet: Teglalap = Teglalap(10, 10)
print("\nnégyzet:")
print(negyzet)

kor: Kor = Kor(5)
print("\nkör:")
print(kor)

# HF: Még három darab osztály: derékszögű, egyenlő oldalú, egyenlő szárú

derekszogu: Derekszogu = Derekszogu(3, 4, 5, 3)
print("\nderékszögű háromszög:")
print(derekszogu)

egyenloszaru: Egyenloszaru = Egyenloszaru(3, 5, 5, 4)
print("\negyenlőszárú háromszög:")
print(egyenloszaru)

szabalyos: Szabalyos = Szabalyos(3, 3, 3, 3.5)
print("\nszabályos háromszög:")
print(szabalyos)