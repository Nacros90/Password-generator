import random
from re import A
        #afficher les instructions ici

        #Il faut utiliser des listes, le type de variable str ne fonctionne pas
MDP=[]
start=1
while start==1:
    nb_cara=int(input("Nombre de caractére du MDP ?"))
    for x in range(0,nb_cara):
        n=random.randint(1,26)
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
                                #il faut continuer la génération de caractéres

    print("Votre MDP est :",MDP)
    print("Il faut ignorer les crochets, les apostrophes et les virgules.")
    start=int(input("Vouler générer un nouveau MDP ? (1.Oui; 2.Non)"))
print()
print("Fin du programme")
print()