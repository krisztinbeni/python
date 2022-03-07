# Kérjük be egy dolgozó bruttó fizetését 12 hónapra. 
#	Számoljuk ki mennyi SZJA –t fizet (az évi fizetés összegének 33,5%-a)
#	Számoljuk ki mennyi egészségügyi hozzájárulást (SZJA 45%-a) és nyugdíjalapot fizetett (SZJA 55%-a )

# 0. importálás
# 1. halmaz feltöltése a fizetés értékével -> List[int]
# 2. hónaponkénti kiiras -> List[int], -> None
# 3. évi fizetés összege -> List[int], -> int
# 4. SZJA kiszámítása -> int (összeg), -> float
# 5. TB hozzájárulás -> float(SZJA értéke), -> float

import random
from typing import *

# változók
honapok: Tuple[str] = (
    "Január",
    "Február",
    "Március",
    "Április",
    "Május",
    "Június",
    "Július",
    "Augusztus",
    "Szeptember",
    "Október",
    "November",
    "December",
)
fizetesek: List[int] = []
szjaErteke: float = None
tbErteke: float = None

def fizetesekGeneralasa() -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, 12, 1):
        eredmeny.append(random.randint(200, 1000))

    return eredmeny

def fizetesekKiirasa(berek: List[int], honapok: Tuple[str]) -> None:

    for index in range(0, 12, 1):
        print(f"{honapok[index]} - {berek[index]} HUF")

def fizetesekOsszege(berek: List[int]) -> int:
    osszeg: int = 0

    for ber in berek:
        osszeg += ber

    return osszeg

def SZJA(berek: List[int]) -> float:
    osszeg: int = fizetesekOsszege(berek)
    return osszeg * 0.335

def TB(szja: float) -> float:
    return szja * 0.45

# főprogram
fizetesek = fizetesekGeneralasa()
fizetesekKiirasa(fizetesek, honapok)

szjaErteke = SZJA(fizetesek)
tbErteke = TB(szjaErteke)
print(f"SZJA: {szjaErteke} HUF")
print(f"TB hozzájárulás: {tbErteke} HUF")