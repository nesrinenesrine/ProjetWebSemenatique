class Software:
    def __init__(self,nom,type,stockage) :
        self.nom=nom
        self.type=type
        self.stockage=stockage
    
    def afficher_software(self):
        print(self.nom)
        print(self.type)
        print(self.stockage)
        
        

class Jeux(Software) : pass

class Education(Software) : pass

class Traiding(Software) :pass



class Communication(Software):
    def __init__(self,nom,type,stockage,type_comm) :
        super().__init__(nom)
        super().__init__(type)
        super().__init__(stockage)
        self.type_comm=type_comm
        
    def afficher_commincation(self):
        super().afficher_software()
        print(self.type_comm)
        