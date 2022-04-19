import random
class Koordinata:
    def __init__(self,sor,oszlop):
        self.sor=sor
        self.oszlop=oszlop
    def __str__(self):
        return "{};{}".format(self.sor,self.oszlop)

def orientacio():
    if random.randint(0,1)==0:
        return "vízszintes"
    return "függőleges"

def orrgen(hajohossz,orientacio):
    hajoorr=[]
    if orientacio=="vízszintes":
        hajoorr.append([random.randint(1,10),random.randint(hajohossz,10)])
    else:
        hajoorr.append([random.randint(1,(10-hajohossz)+1),random.randint(1,10)])
    return hajoorr

def utkozes_kereso(hajoorr,orientacio,hajohossz,koordinatak):
    utkozes=None
    for i in range(hajohossz):
        if orientacio=="vízszintes":
            if koordinatak.count([hajoorr[0][0],hajoorr[0][1]-i])>0:
                print("Ütközés")
                return True
        else:
            if koordinatak.count([hajoorr[0][0]+i,hajoorr[0][1]])>0:
                print("Ütközés")
                return True
                 
    return False
def generalas():
    koordinatak=[]
    for hajohossz in range(1,6):
        orinetacio=orientacio()
        hajoorr=orrgen(hajohossz,orientacio)
        while utkozes_kereso(hajoorr,orientacio,hajohossz,koordinatak)==True:
            hajoorr=orrgen(hajohossz,orientacio)
        for k in range(0,hajohossz):
            if orientacio=="vízszintes":
                if k==0:
                    koordinatak.append([hajoorr[0][0],hajoorr[0][1]])
                else:
                    koordinatak.append([hajoorr[0][0],hajoorr[0][1]-k])

            else:
                if k==0:
                    koordinatak.append([hajoorr[0][0],hajoorr[0][1]])
                else:
                    koordinatak.append([hajoorr[0][0]+k,hajoorr[0][1]])
    return koordinatak
def main():
    poziciok=generalas()   
    for poz in poziciok:
        print(poz)
        print(poziciok.count(poz))
main()
                 
            
            
        
