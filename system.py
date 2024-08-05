class system:
    def __init__(self,nom_sys,version):
        self.nom_sys=nom_sys
        self.version=version
        
    def afficher_sys(self):
        print(self.nom_sys)
        print(self.version)