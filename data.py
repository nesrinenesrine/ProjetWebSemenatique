
class Data_id :
    def __init__(self,numSerieSim,IMEI,IMSI,numTel):
        self.numSerieSim=numSerieSim
        self.IMEI=IMEI
        self.IMSI=IMSI
        self.numTel=numTel
        
    def afficher_data_id(self):
        print(self.numSerieSim)
        print(self.IMEI)
        print(self.IMSI)
        print(self.numTel)


class Data_tel:
    def __init__(self, modele,marque,prix,stockage,cap_bat,numSerie):
        self.modele =modele
        self.marque =marque
        self.prix =prix
        self.numSerie =numSerie
        self.stockage=stockage
        self.cap_bat=cap_bat
        
    def afficher_data_tel(self):
        print(self.modele)
        print(self.marque)
        print(self.prix)
        print(self.numSerie)
        print(self.stockage)
        print(self.cap_bat)

class Data_app :
    
    def __init__(self,nom_user,prenom,email,password,numTelApp):
        self.nom_user=nom_user
        self.prenom=prenom
        self.emial=email
        self.password=password
        self.numTelApp=numTelApp
        
    def afficher_data_app(self):
        print(self.nom_user)
        print(self.prenom)
        print(self.emial)
        print(self.password)
        print(self.numTelApp)
        
          
class Data ( Data_id,Data_tel, Data_app):
    def __init__(self,numSerieSim,IMEI,IMSI,numTel,modele,marque,prix,stockage,cap_bat,numSerie,nom_user,prenom,email,password,numTelApp):
        Data_id.__init__(self,numSerieSim,IMEI,IMSI,numTel)
        Data_tel.__init__(self, modele, marque,  prix,stockage,cap_bat, numSerie)
        Data_app.__init__(self,nom_user,prenom,email,password,numTelApp)
        
    
    def afficher_data(self):
        Data_id.afficher_data_id(self)
        Data_tel.afficher_data_tel(self)
        Data_app.afficher_data_app(self)
        
        