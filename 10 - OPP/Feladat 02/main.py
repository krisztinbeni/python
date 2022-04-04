# Motorkerékpár:
# - gyártó
# - típusa
# - kivitel
# - teljesítmény
# - súly
# - hengerűrtartalom

from Motor import Motor, Tulajdonos

motor: Motor = Motor("Honda", "B400", "Hornet", "98 Kw", "254 kg", "50 l")
print(f"\nA motor adatai: ")
print(f"{motor}")

tulajdonos: Tulajdonos = Tulajdonos("Krisztin Benedek", "2004.11.29.", "férfi", "Szeged")
print(f"\nA tulajdonos adatai: ")
print(f"{tulajdonos}")