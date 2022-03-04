import random
from re import A
        #afficher les instructions ici

        #Il faut utiliser des listes, le type de variable str ne fonctionne pas
MDP=[]
start=1
while start==1:
    nb_cara=int(input("Nombre de caractére du MDP ?"))
    for x in range(0,nb_cara):
        n=random.randint(1,2)
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
                                #il faut continuer la génération de caractéres

    print("Votre MDP est :",MDP)
    print("Il faut ignorer les crochets, les apostrophes et les virgules.")
    start=int(input("Vouler générer un nouveau MDP ? (1.Oui; 2.Non)"))
print()
print("Fin du programme")
print()