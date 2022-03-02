import random
from re import A
        #afficher les instructions ici

        #Il faut utiliser un dictionnaire ou des listes, le type de variable str ne fonctionne pas
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
    print(MDP)