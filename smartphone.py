from telephone_mobile import Telephone_mobile
from data import Data
from materiel import Materiel
from system import system
from tkinter import *

class Smartphone (Telephone_mobile,Materiel,Data,system):
    def __init__(self,ram,rom,nom,num,type_resaux,micro_processeur,ecran,coque,battrie,
                 equipment_reseaux,camera,ecouteur,mic,capteur ,numSerieSim,IMEI,IMSI,numTel,modele,marque,prix,stockage,cap_bat,
                 numSerie,nom_user,prenom,email,password,numTelApp,nom_sys,version):
        
        Materiel. __init__(self,ram,rom,nom,num,type_resaux,micro_processeur,ecran,coque,battrie,equipment_reseaux,camera,ecouteur,mic,capteur)
        Data. __init__(self,numSerieSim,IMEI,IMSI,numTel,modele,marque,prix,stockage,cap_bat,numSerie,nom_user,prenom,email,password,numTelApp)
        system. __init__(self,nom_sys,version)
        
    def afficher_telephone(self):
        Materiel.afficher_materiel(self)
        Data.afficher_data(self)
        system.afficher_sys(self)