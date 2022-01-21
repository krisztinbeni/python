from typing import *

text: str = "bonjoure le monde"
textAsList: List[str] = text.split()

print(textAsList)


text = "Katarzyna Skoworonska Dolata; Polladn; 190; center"
textAsList = text.split(";")

print(textAsList)