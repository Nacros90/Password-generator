import random
from re import A
        #afficher les instructions ici
print()
print("Ce programme sert à générer un mot de passe de manière totalement aléatoire. L'utilisateur peut définir la longueur du mot de passe, c'est à dire le nombre de caractère du mot de passe.")
print()
print("Les caractères prit en compte pour le mot de passe sont : les lettres majuscule et minuscule (sauf les caractères accentutués), les chiffres de 0 à 9, et les caractères spéciaux (&; #; {; }; (; ); -; +; /; *; $; %; ?; !, @; <; >.).")
MDP=[]
start=1
while start==1:
    nb_cara=int(input("Nombre de caractére du MDP ?"))
    for x in range(0,nb_cara):
        n=random.randint(1,80)
        if n==1:
            MDP.append("a")
        elif n==2:
            MDP.append("b")
        elif n==3:
            MDP.append("c")
        elif n==4:
            MDP.append("d")
        elif n==5:
            MDP.append("e")
        elif n==6:
            MDP.append("f")
        elif n==7:
            MDP.append("g")
        elif n==8:
            MDP.append("h")
        elif n==9:
            MDP.append("i")
        elif n==10:
            MDP.append("j")
        elif n==11:
            MDP.append("k")
        elif n==12:
            MDP.append("l")
        elif n==13:
            MDP.append("m")
        elif n==14:
            MDP.append("n")
        elif n==15:
            MDP.append("o")
        elif n==16:
            MDP.append("p")
        elif n==17:
            MDP.append("q")
        elif n==18:
            MDP.append("r")
        elif n==19:
            MDP.append("s")
        elif n==20:
            MDP.append("t")
        elif n==21:
            MDP.append("u")
        elif n==22:
            MDP.append("v")
        elif n==23:
            MDP.append("w")
        elif n==24:
            MDP.append("x")
        elif n==25:
            MDP.append("y")
        elif n==26:
            MDP.append("z")
        elif n==27:
            MDP.append("A")
        elif n==28:
            MDP.append("B")
        elif n==29:
            MDP.append("C")
        elif n==30:
            MDP.append("D")
        elif n==31:
            MDP.append("E")
        elif n==32:
            MDP.append("F")
        elif n==33:
            MDP.append("G")
        elif n==34:
            MDP.append("H")
        elif n==35:
            MDP.append("I")
        elif n==36:
            MDP.append("J")
        elif n==37:
            MDP.append("K")
        elif n==38:
            MDP.append("L")
        elif n==39:
            MDP.append("M")
        elif n==40:
            MDP.append("N")
        elif n==41:
            MDP.append("O")
        elif n==42:
            MDP.append("P")
        elif n==43:
            MDP.append("Q")
        elif n==44:
            MDP.append("R")
        elif n==45:
            MDP.append("S")
        elif n==46:
            MDP.append("T")
        elif n==47:
            MDP.append("U")
        elif n==48:
            MDP.append("V")
        elif n==49:
            MDP.append("W")
        elif n==50:
            MDP.append("X")
        elif n==51:
            MDP.append("Y")
        elif n==52:
            MDP.append("Z")
        elif n==53:
            MDP.append("1")
        elif n==54:
            MDP.append("2")
        elif n==55:
            MDP.append("3")
        elif n==56:
            MDP.append("4")
        elif n==57:
            MDP.append("5")
        elif n==58:
            MDP.append("6")
        elif n==59:
            MDP.append("7")
        elif n==60:
            MDP.append("8")
        elif n==61:
            MDP.append("9")
        elif n==62:
            MDP.append("/")
        elif n==63:
            MDP.append("*")
        elif n==64:
            MDP.append("-")
        elif n==65:
            MDP.append("+")
        elif n==66:
            MDP.append("(")
        elif n==67:
            MDP.append(")")
        elif n==68:
            MDP.append("{")
        elif n==69:
            MDP.append("}")
        elif n==70:
            MDP.append("<")
        elif n==71:
            MDP.append(">")
        elif n==72:
            MDP.append("@")
        elif n==73:
            MDP.append("&")
        elif n==74:
            MDP.append("#")
        elif n==75:
            MDP.append("!")
        elif n==76:
            MDP.append("?")
        elif n==77:
            MDP.append("$")
        elif n==78:
            MDP.append("0")
        elif n==79:
            MDP.append("_")
    print("Votre MDP est :",MDP)
    print("Il faut ignorer les crochets, les apostrophes et les virgules.")
    del MDP[0:nb_cara]                                                              #système permettant de vider la liste
    start=int(input("Vouler générer un nouveau MDP ? (1.Oui; 2.Non)"))
print()
print("Fin du programme")
print()