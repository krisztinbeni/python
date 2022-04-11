# csoport: név, tanulók -> list[tanulo]
# tanuló: vezetéknév, keresztnév, születési dátum
# Hétfő Henrik
# Kedd Krisztián
# Szerda Szilárd

from typing import *
from Tanulok import Tanulok
from Tanulo import Tanulo1, Tanulo2, Tanulo3

tanulok: List[str, int] = []

tanulo1: Tanulo1 = Tanulo1("Hétfő", "Henrik", "2004.11.29.")
tanulo2: Tanulo2 = Tanulo2("Kedd", "Krisztián", "2005.12.24.")
tanulo3: Tanulo3 = Tanulo3("Szerda", "Szilárd", "2006.8.10.")
tanulok: Tanulok = Tanulok("10.b", tanulo1, tanulo2, tanulo3)

def tanulokLista(tanulok: List[str, int]) -> None:
    


print(f"{tanulok}")