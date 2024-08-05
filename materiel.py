from carte_mere  import Carte_mere

class Materiel(Carte_mere):
    
    def __init__(self,ram,rom,nom,num,type_resaux,micro_processeur,ecran,coque,battrie,equipment_reseaux,camera,ecouteur,mic,capteur):

        super().__init__(ram,rom,nom,num,type_resaux,micro_processeur)
        self.ecran=ecran
        self.coque=coque
        self.battrie=battrie
        self.equipment_reseaux=equipment_reseaux
        self.camera=camera
        self.ecouteur=ecouteur
        self.mic=mic
        self.capteur=capteur
    
    def afficher_materiel(self):
        super().afficher_carte_mere()
        print(self.ecran)
        print(self.coque)
        print(self.battrie)
        print(self.equipment_reseaux)
        print(self.camera)
        print(self.ecouteur)
        print(self.mic)
        print(self.capteur)
        
     

    


