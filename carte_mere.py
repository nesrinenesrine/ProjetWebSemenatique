class Memoire :
    def __init__(self,ram,rom):
        self.ram=ram
        self.rom=rom
    
    def afficher_memoire(self):
        print(self.ram)
        print(self.rom)



class Sim :
    def __init__(self,nom,num,type_resaux):
        self.nom=nom
        self.num=num
        self.type_resaux=type_resaux
        
    def afficher_sim(self):
        print(self.nom)
        print(self.num)
        print(self.type_resaux)




class Carte_mere (Memoire ,Sim) :
    def __init__(self,ram,rom,nom,num,type_resaux,micro_processeur):
        Memoire.__init__(self,ram,rom)
        Sim.__init__(self,nom,num,type_resaux)
        self.micro_processeur = micro_processeur
    
    def afficher_carte_mere(self):
        Memoire.afficher_memoire(self)
        Sim.afficher_sim(self)
        print(self.micro_processeur)

