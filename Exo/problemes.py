from math import ceil



#Probleme 1
#142 eleves, 9 adultes, 58 places
#probleme 2
#98 eleves, 4 adultes, 58 places
#probleme 3
#376 eleves, 12 adultes, 52 places

#variables
#bus = [58, 58, 52]
#adultes = [9, 4, 12]
#eleves = [142, 98, 376]
class OUI():
    def __init__(self, bus, adultes, eleves):
        self.eleves = eleves
        self.adultes = adultes
        self.bus = bus
        


        #print(f'le nombre de place restante du probleme {self.probleme+1} est : {self.test(self.eleves,self.adultes, self.bus)}')

    def test(self):
        place_vide = (ceil((((self.eleves+self.adultes)/self.bus)))*self.bus)-(self.adultes+self.eleves)
        return place_vide

    def nbCar(self):
        return ceil((self.adultes+self.eleves)/self.bus)


    def __str__(self):
        t= ['Il y a '+str(self.test())+' places vides']
        s= 'Il y a '+str(self.nbCar())+' bus'
        t.append(s)
        return '\n'.join(t)

#for i in range (0,3):
#    print(OUI(bus[i],adultes[i],eleves[i]))

#total_bus = 0
#places_restante = 0
#boucle de calcul
#for i in range (0,3):
#   while (total_bus < (eleves[i]+adultes[i])):
#       total_bus+=bus[i]

#   places_restante = (total_bus - (eleves[i] + adultes[i]))

    #affichage du resultat
#   print(f'Il reste : {places_restante} places restantes')

#for i in range (0,3):
#    place_vide = (ceil((((eleves[i]+adultes[i])/bus[i])))*bus[i])-(adultes[i]+eleves[i])
#    print(f'il reste {place_vide} places, soit autant qu avec ma boucle')


#for i in range (0,3):
#   print(f'Pour le probleme {i+1},\nIl reste {test(eleves[i],adultes[i],bus[i])} places vides')

#def test(eleves, adultes, places):
#    place_vide = (ceil((((eleves+adultes)/places)))*places)-(adultes+eleves)
#    return place_vide

from Graphique import *
FenetrePrincipale().mainloop()

