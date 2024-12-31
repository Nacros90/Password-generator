import random
from re import A
print()
print("Ce programme sert à générer un mot de passe de manière totalement aléatoire. L'utilisateur peut définir la longueur du mot de passe, c'est à dire le nombre de caractère du mot de passe.")
print()
print("Les caractères prit en compte pour le mot de passe sont : les lettres majuscules et minuscules (sauf les caractères accentutués), les chiffres de 0 à 9, et les caractères spéciaux (&; #; {; }; (; ); -; +; /; *; $; %; ?; !, @; <; >).")
print()
print()
MDP=[]
start=True
while start:
    nb_cara=int(input("Nombre de caractére du MDP ? "))
    print()
    type=int(input("Quels type de caractères doit contenir de MDP ? ([1] Lettres; [2] Chiffres; [3] Lettres et chiffres; [4] Lettres et caractères spéciaux; [5] Lettres, chiffres et cractères spéciaux) : "))
    print()
    for x in range(0,nb_cara):
        if type==1:                                     #Lettres
            typevardebut=1
            typevarfin=52
            typevardebut2=0
            typevarfin2=0
        if type==2:                                     #Chiffres
            typevardebut=53
            typevarfin=62
            typevardebut2=0
            typevarfin2=0
        if type==3:                                     #Lettres et chiffres
            typevardebut=1
            typevarfin=62
            typevardebut2=1
            typevarfin2=52
        if type==4:                                     #Lettres et caractères spéciaux
            typevardebut=1
            typevarfin=52
            typevardebut2=1
            typevarfin2=84
        if type==5:                                     #Lettres, chiffres et caractères spéciaux
            typevardebut=1
            typevarfin=84
            typevardebut2=1
            typevarfin2=84
        n=random.randint(typevardebut,typevarfin)
        n2=random.randint(typevardebut2,typevarfin2)    #n2 est utilisé pour les types 3, 4 et 5, il nous permet de séléctionner autres choses que des lettres
        if type==1:
            n2=n
        if type==3 and n2>=1 and n2<=52:
            n2=n
        if type==4 and n2>=1 and n2<=52:
            n2=n
        if type==5 and n2>=1 and n2<=52:
            n2=n
        if n==1 and n2==n:
            MDP.append("a")
        elif n==2 and n2==n:
            MDP.append("b")
        elif n==3 and n2==n:
            MDP.append("c")
        elif n==4 and n2==n:
            MDP.append("d")
        elif n==5 and n2==n:
            MDP.append("e")
        elif n==6 and n2==n:
            MDP.append("f")
        elif n==7 and n2==n:
            MDP.append("g")
        elif n==8 and n2==n:
            MDP.append("h")
        elif n==9 and n2==n:
            MDP.append("i")
        elif n==10 and n2==n:
            MDP.append("j")
        elif n==11 and n2==n:
            MDP.append("k")
        elif n==12 and n2==n:
            MDP.append("l")
        elif n==13 and n2==n:
            MDP.append("m")
        elif n==14 and n2==n:
            MDP.append("n")
        elif n==15 and n2==n:
            MDP.append("o")
        elif n==16 and n2==n:
            MDP.append("p")
        elif n==17 and n2==n:
            MDP.append("q")
        elif n==18 and n2==n:
            MDP.append("r")
        elif n==19 and n2==n:
            MDP.append("s")
        elif n==20 and n2==n:
            MDP.append("t")
        elif n==21 and n2==n:
            MDP.append("u")
        elif n==22 and n2==n:
            MDP.append("v")
        elif n==23 and n2==n:
            MDP.append("w")
        elif n==24 and n2==n:
            MDP.append("x")
        elif n==25 and n2==n:
            MDP.append("y")
        elif n==26 and n2==n:
            MDP.append("z")
        elif n==27 and n2==n:
            MDP.append("A")
        elif n==28 and n2==n:
            MDP.append("B")
        elif n==29 and n2==n:
            MDP.append("C")
        elif n==30 and n2==n:
            MDP.append("D")
        elif n==31 and n2==n:
            MDP.append("E")
        elif n==32 and n2==n:
            MDP.append("F")
        elif n==33 and n2==n:
            MDP.append("G")
        elif n==34 and n2==n:
            MDP.append("H")
        elif n==35 and n2==n:
            MDP.append("I")
        elif n==36 and n2==n:
            MDP.append("J")
        elif n==37 and n2==n:
            MDP.append("K")
        elif n==38 and n2==n:
            MDP.append("L")
        elif n==39 and n2==n:
            MDP.append("M")
        elif n==40 and n2==n:
            MDP.append("N")
        elif n==41 and n2==n:
            MDP.append("O")
        elif n==42 and n2==n:
            MDP.append("P")
        elif n==43 and n2==n:
            MDP.append("Q")
        elif n==44 and n2==n:
            MDP.append("R")
        elif n==45 and n2==n:
            MDP.append("S")
        elif n==46 and n2==n:
            MDP.append("T")
        elif n==47 and n2==n:
            MDP.append("U")
        elif n==48 and n2==n:
            MDP.append("V")
        elif n==49 and n2==n:
            MDP.append("W")
        elif n==50 and n2==n:
            MDP.append("X")
        elif n==51 and n2==n:
            MDP.append("Y")
        elif n==52 and n2==n:
            MDP.append("Z")
        elif n==53 or n2==53:
            MDP.append("1")
        elif n==54 or n2==54:
            MDP.append("2")
        elif n==55 or n2==55:
            MDP.append("3")
        elif n==56 or n2==56:
            MDP.append("4")
        elif n==57 or n2==57:
            MDP.append("5")
        elif n==58 or n2==58:
            MDP.append("6")
        elif n==59 or n2==59:
            MDP.append("7")
        elif n==60 or n2==60:
            MDP.append("8")
        elif n==61 or n2==61:
            MDP.append("9")
        elif n==62 or n2==62:
            MDP.append("0")
        elif n==63 or n2==63:
            MDP.append("*")
        elif n==64 or n2==64:
            MDP.append("-")
        elif n==65 or n2==65:
            MDP.append("+")
        elif n==66 or n2==66:
            MDP.append("(")
        elif n==67 or n2==67:
            MDP.append(")")
        elif n==68 or n2==68:
            MDP.append("{")
        elif n==69 or n2==69:
            MDP.append("}")
        elif n==70 or n2==70:
            MDP.append("<")
        elif n==71 or n2==71:
            MDP.append(">")
        elif n==72 or n2==72:
            MDP.append("@")
        elif n==73 or n2==73:
            MDP.append("&")
        elif n==74 or n2==74:
            MDP.append("#")
        elif n==75 or n2==75:
            MDP.append("!")
        elif n==76 or n2==76:
            MDP.append("?")
        elif n==77 or n2==77:
            MDP.append("$")
        elif n==78 or n2==78:
            MDP.append("/")
        elif n==79 or n2==79:
            MDP.append("_")
        elif n==80 or n2==80:
            MDP.append("%")
        elif n==81 or n2==81:
            MDP.append("[")
        elif n==82 or n2==82:
            MDP.append("]")
        elif n==83 or n2==83:
            MDP.append("'")
        elif n==84 or n2==84:
            MDP.append(",")
    print("Votre MDP est :")
    for i in range(0,nb_cara):
        print(MDP[i],end="")
    print()
    MDP.clear()
    print()
    print()
    restart=str(input("Voulez-vous générer un autre MDP ? ([Y] Oui; [N] Non) : "))
    if restart=="Y" or restart=="y":
        start=True
    else:
        start=False
    print()
print()
print("Fin du programme")
print()