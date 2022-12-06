print("N.Peclet")
Mv=input("Entrez la masse volumique : ")
Cp=input("Entrez la capacité thermique massique : ")
v=input("Entrez la vitesse: ")
h=input("Entrez la coefficient de transfert thermique : ")
try:
    Cp = float(Cp)
    v = float(v)
    h = float(h)
    Mv = float(Mv)
    Ma = h/Mv*v*Cp
    print("Le nombre Margoulis", Ma)
except:
    print("erreur")