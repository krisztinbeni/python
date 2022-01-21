#pip3 install keyboard

#csomagok inportálása
import os
#import keyboard
import time

#változók definiálása

#a szám amit be kell olvasni
#kezdőértéke None mivel a while ciklusban ki tudom ezt használni az ismétlések használatára,
#vagyis a ciklust mindaddig futtatjuk, még a number változónak nem lesz szám értéke
number: int = None

#segéd változó, a beolvasott értékét fogja tárolni
data: str = ""

#while ciklus, ami mindaddig fog futni meg a number változó nem kap szám értéket,
# azaz az értéke nem None lesz
while(number == None):
    #beolvasás a konzólról és a beolvasott értéket eltéroljuk a data változóban
    data = input("Kerem a szamot: ")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható-e
    #mindegy, hogy ez a szám int vagy float típusú
    #isdigit() -> bool változót ad vissza
    if (data.isdigit()):
        #ha az isdigit fügvény értéke ugyanaz akkor számot írt be a felhasználó
        #amit mi biztos át tudunk szám típussá alakítani
        number = int(data)
        #ha az isdigit() fügvény hamis, azaz a felhasználó nem számot írt be
        #így a number változó továbbra is None marad, azaz a felhasználó nem számot írt be
        # a ciklust ismételni kezd
    else:
        print("\n Nem szamot adott meg!")
        #a programot futtató szálat (thred) elaltatjuk 3 másodpercre
        time.sleep(3)
        #letöröljük a képernyőt
        os.system("cls")
        #print("\n A folytatashoz nyomjon meg az ENTER billentyut.")
        #egy végtelen while ciklust írunk mivel arra fogunk várni, hogy a felhasználó benyomja a kért billentyünket (ENTER)
        #while (True):
            #figyeljük, hogy a felhasználó lenyomta-e az ENTER gombot
        #    if (keyboard.is_pressed('enter')):
            #letöröljük a képernyőt
        #    os.system("cls")
            #kilépünk a belső (végtelen) while ciklusból
        #    break

#kiírjuk a beolvasott számot
print(f"A beolvasott szam: {number}")