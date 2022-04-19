import turtle
def balos():
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(200)

def jobbos():
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    
def palya():
    turtle.speed(0)
    turtle.down()
    for i in range(5):
        balos()
        jobbos()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    for i in range(5):
        jobbos()
        balos()
    turtle.backward(200)
    turtle.up()

def elfogad_e(hozzaad):
    for tempkord in hozzaad:
        turtle.color("red")
        turtle.setpos(((int(tempkord[1])-1)*20)+10,((10-int(tempkord[0]))*20)+10)
        turtle.width(10)
        turtle.down()
        turtle.forward(1)
        turtle.up()

def berajz(koordinatak):
    for koordinata in koordinatak:
        turtle.setpos(((int(koordinata[1])-1)*20)+10,((10-int(koordinata[0]))*20)+10)
        turtle.width(10)
        turtle.down()
        turtle.forward(1)
        turtle.up()

def elfogadta(hozzaad):
    for tempkord in hozzaad:
        turtle.color("black")
        turtle.setpos(((int(tempkord[1])-1)*20)+10,((10-int(tempkord[0]))*20)+10)
        turtle.width(10)
        turtle.down()
        turtle.forward(1)
        turtle.up()

def torol(hozzaad):
    for tempkord in hozzaad:
        turtle.color("white")
        turtle.setpos(((int(tempkord[1])-1)*20)+10,((10-int(tempkord[0]))*20)+10)
        turtle.width(10)
        turtle.down()
        turtle.forward(1)
        turtle.up()
