import random
import time
from turtle import*
from math import *

setup(width = 1.0, height = 1.0)
window_y = window_height()
window_x = window_width()



bgcolor("#0c1445")
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t1.speed(0)
t2.speed(0)
t3.speed(0)
t1.ht()
t2.ht()
t3.ht()

#procédure du choix dalumettes à enlever
def choixJoueur(r,nbAllumettes):
    choix = False
    while choix == False:
        choixJoueur = int(numinput("À votre tour !","Retirez des allumettes ! "+str(r)))
        if choixJoueur in r and nbAllumettes >= choixJoueur:
            choix = True
    return choixJoueur
        
def choixOrdinateur(r,nbAllumettes):
    choix = False
    while choix == False:
        choixOrdinateur = random.choice(r)
        if nbAllumettes >= choixOrdinateur:
            choix = True
    return choixOrdinateur


#procédures éléments du décor
def asteroid(x,y,r): #allumettes
    t3.up()
    t3.goto(x,y)
    t3.down()
    t3.color("sienna")
    t3.pensize(5)
    i = 0
    t3.begin_fill()
    while i < 3:
        t3.circle(r,100 - 10*i)
        t3.right(75)
        t3.fd(r/10)
        t3.left(90)
        t3.fd(r/3)
        t3.left(90)
        t3.fd(r/10)
        t3.right(75)
        i=i+1
    t3.right(25)
    t3.circle(r,5)
    t3.end_fill()

    t3.up()
    t3.goto(x-0.3*r,y+0.6*r)
    t3.down()
    t3.dot(0.4*r,"saddlebrown")

    t3.up()
    t3.goto(x+0.6*r,y+1.2*r)
    t3.down()
    t3.dot(0.3*r,"saddlebrown")

    t3.up()
    t3.goto(x-0.25*r,y+1.3*r)
    t3.down()
    t3.dot(0.29*r,"saddlebrown")
    t3.left(20)

def asteroidExplose(x,y,t):
    t3.pensize(5)
    t3.up()
    t3.goto(x-0.2*t,y)
    t3.down()
    t3.color("red")
    t3.begin_fill()
    t3.left(70)
    t3.forward(0.7*t)
    t3.right(120)
    t3.forward(0.9*t)
    t3.left(150)
    t3.forward(0.85*t)
    t3.right(95)
    t3.forward(0.4*t)
    t3.left(130)
    t3.forward(0.5*t)
    t3.right(90)
    t3.forward(0.3*t)
    t3.left(160)
    t3.forward(0.3*t)
    t3.right(100)
    t3.forward(0.8*t)
    t3.left(150)
    t3.forward(0.7*t)
    t3.right(90)
    t3.forward(t)
    t3.left(160)
    t3.forward(0.8*t)
    t3.right(130)
    t3.forward(0.4*t)
    t3.left(140)
    t3.forward(0.4*t)
    t3.right(100)
    t3.forward(0.5*t)
    t3.left(150)
    t3.forward(0.4*t)
    t3.right(118)
    t3.forward(0.7*t)
    t3.end_fill()

    t3.up()
    t3.goto(x+0.6*t,y+0.8*t)
    t3.down()
    t3.color("sienna")
    t3.begin_fill()
    t3.forward(0.5*t)
    t3.left(90)
    t3.forward(0.3*t)
    t3.left(45)
    t3.forward(0.5*t)
    t3.left(45)
    t3.forward(0.2*t)
    t3.left(92)
    t3.forward(0.65*t)
    t3.end_fill()


    t3.up()
    t3.goto(x-0.6*t,y+1.6*t)
    t3.down()

    t3.begin_fill()
    t3.left(90)
    t3.forward(0.6*t)
    t3.left(30)
    t3.forward(0.4*t)
    t3.left(90)
    t3.forward(0.3*t)
    t3.left(100)
    t3.forward(0.5*t)
    t3.right(30)
    t3.forward(0.2*t)
    t3.right(10)
    t3.forward(0.24*t)
    t3.left(90)
    t3.forward(0.1*t)
    t3.end_fill()

    t3.up()
    t3.goto(x+0.7*t,y+2*t)
    t3.down()

    t3.begin_fill()
    t3.forward(0.3*t)
    t3.left(45)
    t3.forward(0.4*t)
    t3.left(90)
    t3.forward(0.2*t)
    t3.left(90)
    t3.forward(0.4*t)
    t3.right(20)
    t3.forward(0.2*t)
    t3.left(90)
    t3.forward(0.07*t)
    t3.end_fill()

    t3.up()
    t3.goto(x+0.8*t,y+1.7*t)
    t3.down()

    t3.begin_fill()
    t3.right(180)
    t3.forward(0.2*t)
    t3.left(120)
    t3.forward(0.2*t)
    t3.left(120)
    t3.forward(0.2*t)
    t3.end_fill()

    t3.up()
    t3.goto(x+0.05*t,y+0.3*t)
    t3.down()

    t3.begin_fill()
    t3.forward(0.2*t)
    t3.left(60)
    t3.forward(0.4*t)
    t3.left(90)
    t3.forward(0.5*t)
    t3.left(121)
    t3.forward(0.6*t)
    t3.end_fill()
    t3.right(85)

def etoile(x,y,t,c,a=0):
    t1.color(c)
    t1.up()
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.right(a)
    for i in range (5):
        t1.forward(t)
        t1.right(288)
        t1.forward(t)
        t1.right(144)
    t1.end_fill()
    t1.left(a)

def lune(x,y,t,c,a=0):
    t1.right(a)
    t1.color(c)
    t1.up()
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.circle(t,160)
    t1.right(160)
    t1.circle (-t,199)
    t1.end_fill()
    t1.right(161)
    t1.left(a)

def bulle(x,y,t):
    t1.up()
    t1.goto(x,y)
    t1.down()
    t1.color("white")
    t1.begin_fill()
    t1.left(30)
    t1.forward(0.07*t)
    t1.left(60)
    t1.forward(0.16*t)
    t1.circle(-0.06*t,90)
    t1.forward(t)
    t1.circle(-0.06*t,90)
    t1.forward(0.12*t)
    t1.circle(-0.06*t,90)
    t1.forward(1.02*t)
    t1.left(10)
    t1.forward(0.11*t)
    t1.end_fill()
    t1.right(190)

def planete(x,y,l):
    t1.speed(0)
    t1.up()
    t1.goto(x,y)
    t1.down()
    p=(l/150)
 
    t1.color('blue')
    t1.begin_fill()
    t1.circle(l)
    t1.end_fill()
 
    t1.goto(x,y)
 
    t1.color('green')
    t1.up()
    x=(x-l)
    y=(y+(l+(20*p)))
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.circle((2/3)*l,102)
    t1.left(98)
    t1.circle(l,63)
    t1.end_fill()
 
    t1.up()
    x=(x+(282*p))
    y=(y+(50*p))
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.right(90)
    t1.circle((2/3)*l,40)
    t1.left(50)
    t1.circle((2/3)*l,50)
    t1.right(60)
    t1.forward((1/5)*l)
    t1.circle((1/5)*l,70)
    t1.right(70)
    t1.forward((4/15)*l)
    t1.left(140)
    t1.circle(l,85)
    t1.end_fill()
 
    t1.up()
    x=(x-(260*p))
    y=(y-(150*p))
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.circle(-l,10)
    t1.right(120)
    t1.forward((2/15)*l)
    t1.left(30)
    t1.circle(-(2/3)*l,50)
    t1.right(50)
    t1.forward((1/5)*l)
    t1.left(50)
    t1.circle((7/15)*l,50)
    t1.right(90)
    t1.circle(-(7/15)*l,35)
    t1.right(62)
    t1.circle(-l,80)
    t1.end_fill()
 
    t1.up()
    x=(x+(148*p))
    y=(y+(180*p))
    t1.goto(x,y)
    t1.down()
    t1.left(90)
    t1.begin_fill()
    t1.circle((1/3)*l,30)
    t1.left(90)
    t1.circle((1/3)*l,50)
    t1.left(30)
    t1.forward((4/15)*l)
    t1.left(90)
    t1.circle((1/3)*l,50)
    t1.left(60)
    t1.end_fill()
    t1.forward((1/5)*l)
    t1.left(119)
    
def ovni(x,y,t):
    t1.up()
    t1.goto(x,y) #(x,y)
    t1.down()
    t1.color("slategrey")
    t1.begin_fill()
    t1.right(45)
    t1.circle(2.9*t,90)
    t1.circle(0.3*t,90)
    t1.circle(2.9*t,90)
    t1.circle(0.3*t,90)
    
    t1.end_fill()
    t1.color("#6CC417")
    t1.up()
    t1.goto(x+3.25*t,y+0.6*t)
    t1.down()
    t1.begin_fill()
    t1.left(135)
    t1.circle(1.2*t,180)
    t1.left(45.5)
    t1.circle(1.71*t,90)
    t1.end_fill()
    t1.right(45.53)
    
#procédure du décor
def decor():
    planete(0,-0.13*window_x,0.13*window_x)
    etoile(0.375*window_x,0.38*window_y,0.021*window_x,"gold",-5)
    etoile(0.375*window_x,-0.38*window_y,0.015*window_x,"gold",-15)
    etoile(0.36*window_x,-0.41*window_y,0.008*window_x,"gold",-14)
    etoile(-0.42*window_x,0.38*window_y,0.023*window_x,"gold",-10)
    etoile(-0.42*window_x,0.28*window_y,0.01*window_x,"gold",10)
    etoile(-0.36*window_x,0.34*window_y,0.006*window_x,"gold",-16)
    etoile(-0.42*window_x,-0.38*window_y,0.023*window_x,"gold",-30)
    etoile(-0.36*window_x,-0.37*window_y,0.016*window_x,"gold",-10)  
    etoile(-0.21*window_x,-0.19*window_y,0.008*window_x,"gold",-10)  
    etoile(0.21*window_x,0.2*window_y,0.006*window_x,"gold",20)
    lune(0.15*window_x,0.19*window_y,0.05*window_x,"khaki")
    ovni(-0.365*window_x,-0.05*window_y,0.016*window_x)
    bulle(-0.313*window_x,0,0.15*window_x)

#fonction qui affiche les allumettes et renvoie les informations dojnt on a besoin
def affichageAllumettes(nbAllumettes):
    #on predefini les positions des allumettes
    pos = [[0.1*window_x,0.19*window_y],[-0.16*window_x,0.14*window_y],[0.15*window_x,-0.19*window_y],[-0.16*window_x,-0.2*window_y],[-0.005*window_x,0.25*window_y],[0.005*window_x,-0.38*window_y],[0.13*window_x,0.31*window_y],[0.18*window_x,0],[-0.12*window_x,-0.31*window_y],[-0.18*window_x,0.36*window_y],[0.18*window_x,-0.35*window_y],[-0.24*window_x,0.08*window_y],[0.23*window_x,0.19*window_y],[-0.22*window_x,-0.3*window_y],[0.24*window_x,-0.16*window_y]]
    positions = []
    taille = []
    explosePos = []
    exploseTaille = []
    i = nbAllumettes
    t3.clear()
    #on tire au hasard un emplacement et une taille autant de fois qu'il le faut
    while i > 0:
        emplacement = random.randint(0,len(pos)-1)
        t = random.randint(ceil(0.05*window_y),ceil(0.08*window_y))
        x = pos[emplacement][0]
        y = pos[emplacement][1]
        del pos[emplacement]
        i = i-1
        positions.append([x,y])
        taille.append(t)
        asteroid(x,y,t)
    info = [positions]+[taille]+[explosePos]+[exploseTaille]
    return info


#maj affichage allumettes et renvoie les informations dojnt on a besoin 
def majAllumettes(nbAllumettes,info):
    pos = info[0]
    taille = info[1]
    explosePos = info[2]
    exploseTaille = info[3]
    t3.clear()
    #tire au sort les allumettes qu'on va enlever et trie les listes
    i = len(pos) - nbAllumettes
    while i > 0:
        choix = random.randint(0,len(pos)-1)
        explosePos.append(pos[choix])
        exploseTaille.append(taille[choix])
        del pos[choix]
        del taille[choix]
        i=i-1

    #dessine les allumettes qui vont rester
    j = len(pos)
    while j > 0:
        x = pos[j-1][0]
        y = pos[j-1][1]
        t = taille[j-1]
        asteroid(x,y,t)
        j = j - 1

    #dessine les allulmettes qui sont enlevés
    k = len(explosePos)
    while k > 0:
        x = explosePos[k-1][0]
        y = explosePos[k-1][1]
        t = exploseTaille[k-1]
        asteroidExplose(x,y,t)
        k = k-1
    #on renvoie les infos pour les garder
    info = [pos]+[taille]+[explosePos]+[exploseTaille]
    return info

#procédure pour afficher le nombre d'allumettes
def nbAllulmettes(nbAllumettes):
    t1.up()
    t1.goto(0.46*window_x,0.44*window_y)
    t1.down()
    t1.dot(0.1*window_y,"black")
    t1.up()
    t1.goto(0.46*window_x,0.426*window_y)
    t1.down()
    t1.color("white")
    t1.write(nbAllumettes,align="center",font=("Verdana",ceil(0.024*window_y), "normal"))

    
#procédure pour mettre à jour le nombre d'allumettes
def majNbAllumettes(nbAllumettes):
    t1.up()
    t1.goto(0.46*window_x,0.44*window_y)
    t1.down()
    t1.dot(0.1*window_y,"black")
    t1.up()
    t1.goto(0.46*window_x,0.426*window_y)
    t1.down()
    t1.color("white")
    t1.write(nbAllumettes,align="center",font=("Verdana",ceil(0.024*window_y), "normal"))

#procédure qui affiche l'écran de fin de partie
def finDuJeu(victoire):
    t1.dot(8000,"black")
    t1.victoire = str(victoire)
    t1.up()
    t1.goto(0,25)
    t1.down()
    t1.write("FIN",align="center",font=("Verdana",50, "normal"))
    t1.up()
    t1.goto(0,-25)
    t1.down()
    t1.write(str(victoire)+" victoire(s).",align="center",font=("Verdana",14, "normal"))

#procédure qui affiche le choix de l'orinateur
def afficheChoixOrdinateur(choix):
    t2.clear()
    t2.up()
    t2.goto(-0.22*window_x,0.027*window_y)
    t2.down()
    choix = str(choix)
    t2.color("black")
    t2.write("L'extraterrestre détruit "+choix+" astéroide(s)",align="center",font=("Arial",ceil(0.007*window_x), "normal"))
    time.sleep(1)




r=[1,2,3]
rejouer = "oui"
victoire = 0
tracer(False)
decor()
tracer(True)
while rejouer == "oui":
    nbAllumettes = random.randint(10,15)
    tracer(False)
    allumettesInfos = affichageAllumettes(nbAllumettes)
    tracer(True)
    winJoueur = False
    winOrdinateur = False
    while nbAllumettes > 0 and nbAllumettes >= min(r):
        nbAllulmettes(nbAllumettes)
#choix du joueur
        choix1 = choixJoueur(r,nbAllumettes)
        nbAllumettes = nbAllumettes - choix1
        majNbAllumettes(nbAllumettes)
        tracer(False)
        allumettesInfos = majAllumettes(nbAllumettes,allumettesInfos)
        tracer(True)
        if nbAllumettes == 0:
            winJoueur = True
        elif nbAllumettes < min(r):
            winJoueur = True
            winOrdinateur = False
#choix de l'ordinateur si le joueur n'a pas encore gagné
        else:
            choix2 = choixOrdinateur(r,nbAllumettes)
            afficheChoixOrdinateur(choix2)
            nbAllumettes = nbAllumettes - choix2
            majNbAllumettes(nbAllumettes)
            tracer(False)
            allumettesInfos = majAllumettes(nbAllumettes,allumettesInfos)
            tracer(True)
            if nbAllumettes == 0:
                winOrdinateur = True
            elif nbAllumettes < min(r):
                winJoueur = False
                winOrdinateur = True
#choix du gagnant
    if winJoueur == True:
        resultat="Vous avez gagné !"
        victoire += 1
    else:
        resultat="Vous avez perdu !"
#rejouer
    rejouer = textinput(resultat,"Pour rejouer écrivez 'oui'.")
finDuJeu(victoire)
exitonclick()
