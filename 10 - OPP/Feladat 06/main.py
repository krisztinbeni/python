# szuperhős: név (str), erő(int) -> random szám 50 - 100, életpont(int) -> random szám 60 - 90
# Támad(szuperhős)
#   erő > hp (bool) győz

from Szuperhos import *

vasember: Szuperhos = Szuperhos("Vasember")
thor: Szuperhos = Szuperhos("Thor")

print(vasember)
print(thor)

if vasember.tamadas(thor):
    print("Vasember győzött!")
else:
    print("Vasember vesztett!")