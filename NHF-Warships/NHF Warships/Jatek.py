import Grafika
import Hajogeneralas



def tablak():
    gephajok=[]
    userhajok=[]
    gephajok=Hajogeneralas.generalas()
    dontes=input("Gépi vagy manuálisan elrendezett hajókkal szeretnél játszani (a/m)?: ")
    if dontes=="a":
        userhajok=Hajogeneralas.generalas()
    elif dontes=="m":
        melyik=input("Melyik hajóelrendezésedet szeretnéd használni (fájlkiterjesztés nem kell)?: ")+".txt"
        userhajok=hajorend_beolvaso(melyik)
        
