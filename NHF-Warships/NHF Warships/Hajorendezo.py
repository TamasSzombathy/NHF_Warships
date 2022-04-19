import Grafika
def adatiro(koordinatak,hajorend):
    for koordinata in koordinatak:
        hajorend.write(str(koordinata))
        hajorend.write("\n")
    hajorend.close()

def hajoiro(hajoorr,orientacio,hossz,koordinatak):
    for i in range(0,hossz):
        if orientacio=="v":
            koordinatak.append([hajoorr[0],hajoorr[1]-i])
        elif orientacio=="f":
            koordinatak.append([hajoorr[0]+i,hajoorr[1]])
    return koordinatak

def utkozes_kereso(hajoorr,orientacio,hossz,koordinatak):
    temp=[]
    utkozes=None
    for i in range(0,hossz):
        if orientacio=="v":
            if koordinatak.count([hajoorr[0],hajoorr[1]-i])>0:
                return True
        elif orientacio=="f":
            if koordinatak.count([hajoorr[0]+i,hajoorr[1]])>0:
                return True
    return False
            
def beolvaso():
    nev=input("Írd be a hajóelrendezésed nevét (fájlkiterjesztés nem kell): ")+".txt"
    if nev==".txt":
        nev="Hajorend 1.txt"
    hajorend=open(nev,"w",encoding="UTF-8")
    koordinatak=[]
    hajoorr=[]
    Grafika.palya()
    hozzaad=[]
    for i in range(1,6):
        hossz=i
        print(i,"méretű hajó elhelyezése.")
        print("Függőleges elhelyezésnél lefelé, vízszintesnél balra folytatódnak a hajók az orrhoz képest!")
        if hossz==1:
            while True:
                try:
                    sor=int(input("Írd be, hogy a hajó hanyadik sorban van: "))
                    oszlop=int(input("Írd be, hogy a hajó hanyadik oszlopban van: "))
                    if sor>=1 and sor<10 or oszlop>=1 and oszlop<10:
                        break
                    elif sor=="reset" or oszlop=="reset":
                        beolvaso()
                    else:
                        print("Rossz válasz érkezett!\n")
                except ValueError:
                    print("Rossz válasz érkezett!\n")
            Grafika.elfogad_e([[sor,oszlop]])
            elfogad=input("Elfogadod ezt az elhelyezést? (i/n): ")
            if elfogad=="i":
                Grafika.elfogadta([[sor,oszlop]])
                koordinatak.append([sor,oszlop])
            else:
                Grafika.torol([[sor,oszlop]])
                beolvaso()
        else:
            while True:
                try:
                    orientacio=str(input("Írd be, hogy vízszintesen vagy függőlegesen álljon a hajó (v/f): "))
                    sor=int(input("Írd be, hogy a hajó hanyadik sorban van: "))
                    oszlop=int(input("Írd be, hogy a hajó hanyadik oszlopban van: "))
                    if orientacio=="v" and oszlop<hossz or orientacio=="f" and sor>(10-hossz)+1:
                        print("A hajó így nem fér rá a pályára!\n") 
                    elif sor>=1 and sor<10 and oszlop>=1 and oszlop<10 or orientacio!="" and type(orientacio)==str:
                        break
                    elif orientacio=="reset" or sor=="reset" or oszlop=="reset":
                        beolvaso()
                    else:
                        print("Rossz válasz érkezett!\n")
                except ValueError:
                    print("Rossz válasz érkezett!\n")
            hajoorr=[sor,oszlop]
            if utkozes_kereso(hajoorr,orientacio,hossz,koordinatak)==True:
                print("Így a hajók egymásra generálódnának!")
                beolvaso()
            else:
                for m in range(hossz):
                    if orientacio=="v":
                        hozzaad.append([hajoorr[0],hajoorr[1]-m])
                    elif orientacio=="f":
                        hozzaad.append([hajoorr[0]+m,hajoorr[1]])
                Grafika.elfogad_e(hozzaad)
                elfogad=input("Elfogadod ezt az elhelyezést? (i/n): ")
                if elfogad=="i":
                    Grafika.elfogadta(hozzaad)
                    hajoiro(hajoorr,orientacio,hossz,koordinatak)
                    hozzaad=[]
                else:
                    Grafika.torol(hozzaad)
                    beolvaso()
    adatiro(koordinatak,hajorend)
    print(koordinatak,"\n")
beolvaso()
