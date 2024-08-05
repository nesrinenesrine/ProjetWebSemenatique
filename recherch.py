from system import system
from tkinter import *

def caseecron():
        window_ecron=Tk()
        val1=Label(window_ecron,text="Les tailles d'écrans disponible : \n 7,7 X 4,4 cm \n 8,9  X 5 cm \n 11,1 X 6,2 cm \n 13,3 X 7,5 cm \n 15,5 X 8,7 cm \n 17,5 X 10 cm \n 19,5 X 11,2 cm",font=('Arial',10,'bold')).pack()
        window_ecron.mainloop()
        
def casebattrie():
        window_bat=Tk()
        val1=Label(window_bat,text="Les capacités du battrie disponible:\n 1500 MAH  ",font=('Arial',10,'bold'))
        val2=Label(window_bat,text="2000 MAH",font=('Arial',10,'bold'))
        val3=Label(window_bat,text="2300 MAH",font=('Arial',10,'bold'))
        val4=Label(window_bat,text="2500 MAH",font=('Arial',10,'bold'))
        val5=Label(window_bat,text="2800 MAH",font=('Arial',10,'bold'))
        val6=Label(window_bat,text="3000 MAH",font=('Arial',10,'bold'))
        val7=Label(window_bat,text="3500 MAH",font=('Arial',10,'bold'))
        val8=Label(window_bat,text="3900 MAH",font=('Arial',10,'bold'))
        val9=Label(window_bat,text="4000 MAH",font=('Arial',10,'bold'))
        val10=Label(window_bat,text="8000 MAH",font=('Arial',10,'bold'))
        val1.pack()
        val2.pack()
        val3.pack()
        val4.pack()
        val5.pack()
        val6.pack()
        val7.pack()
        val8.pack()
        val9.pack()
        val10.pack()
        window_bat.mainloop()
        

def caseequipement_rsd():
        window_equipement_rsd=Tk()
        val1=Label(window_equipement_rsd,text="bluetooth \n wifi \n NCF",font=('Arial',10,'bold'))
        val1.pack()
        window_equipement_rsd.mainloop()

def casecamera():
        window_camera=Tk()
        val1=Label(window_camera,text="Les Qualités du caméra disponible : \n 12 MGP  ",font=('Arial',10,'bold'))
        val2=Label(window_camera,text="14 MGP",font=('Arial',10,'bold'))
        val3=Label(window_camera,text="16 MGP",font=('Arial',10,'bold'))
        val4=Label(window_camera,text="18 MGP",font=('Arial',10,'bold'))
        val5=Label(window_camera,text="20 MGP",font=('Arial',10,'bold'))
        val1.pack()
        val2.pack()
        val3.pack()
        val4.pack()
        val5.pack()
        window_camera.mainloop()
        
def caseecouteur():
        window_capteur=Tk()
        window_capteur.mainloop()


def casemic():
        window_mic=Tk()
        window_mic.mainloop()

def casecapteur():
        window_capteur=Tk()
        window_capteur.mainloop()

def casememoire():
        window_memoire=Tk()
        button1 = Button(window_memoire,text='RAM',command=caseram,font=('Arial',10,'bold')) 
        button2 = Button(window_memoire,text='ROM',command=caserom,font=('Arial',10,'bold'))
        button1.pack()
        button2.pack()
        
def caseram():
        window_ram=Tk()
        val1=Label(window_ram,text="Les Capacités du RAM disponible est \n 1GO  ",font=('Arial',10,'bold'))
        val2=Label(window_ram,text="2GO",font=('Arial',10,'bold'))
        val3=Label(window_ram,text="4GO",font=('Arial',10,'bold'))
        val4=Label(window_ram,text="6GO",font=('Arial',10,'bold'))
        val5=Label(window_ram,text="8GO",font=('Arial',10,'bold'))
        val6=Label(window_ram,text="16GO",font=('Arial',10,'bold'))
        val7=Label(window_ram,text="32GO",font=('Arial',10,'bold'))
        val1.pack()
        val2.pack()
        val3.pack()
        val4.pack()
        val5.pack()
        val6.pack()
        val7.pack()
        window_ram.mainloop()
        
def caserom():
        window_rom=Tk()
        val1=Label(window_rom,text="Les Capacités du ROM disponible est \n 2GO  ",font=('Arial',10,'bold'))
        val2=Label(window_rom,text="4GO",font=('Arial',10,'bold'))
        val3=Label(window_rom,text="8GO",font=('Arial',10,'bold'))
        val4=Label(window_rom,text="16GO",font=('Arial',10,'bold'))
        val5=Label(window_rom,text="32GO",font=('Arial',10,'bold'))
        val6=Label(window_rom,text="64GO",font=('Arial',10,'bold'))
        val7=Label(window_rom,text="128GO",font=('Arial',10,'bold'))
        val8=Label(window_rom,text="256GO",font=('Arial',10,'bold'))
        val9=Label(window_rom,text="512GO",font=('Arial',10,'bold'))
        Val10=Label(window_rom,text="1TO",font=('Arial',10,'bold'))
        val1.pack()
        val2.pack()
        val3.pack()
        val4.pack()
        val5.pack()
        val6.pack()
        val7.pack()
        val8.pack()
        val9.pack()
        Val10.pack()
        window_rom.mainloop()

def casesim():
        window_sim=Tk()
        window_sim.mainloop()

def casemat ():
        window_mat=Tk()
        button1 = Button(window_mat,text='écran',command=caseecron,font=('Arial',10,'bold')).pack()
        button2 = Button(window_mat,text='battrie',command=casebattrie,font=('Arial',10,'bold')).pack()
        button3 = Button(window_mat,text='équipement rsd',command=caseequipement_rsd,font=('Arial',10,'bold')).pack()
        button4 = Button(window_mat,text='caméra',command=casecamera,font=('Arial',10,'bold')).pack()
        button5 = Button(window_mat,text='écouteur',command=caseecouteur,font=('Arial',10,'bold')).pack() 
        button6 = Button(window_mat,text='mic',command=casemic,font=('Arial',10,'bold')).pack()
        button7 = Button(window_mat,text='capteur',command=casecapteur,font=('Arial',10,'bold')).pack()
        button8 = Button(window_mat,text='memoire',command=casememoire,font=('Arial',10,'bold')).pack()
        button9 = Button(window_mat,text='sim',command=casesim,font=('Arial',10,'bold')).pack()
        window_mat.mainloop()


def casemat_search():
        window_mat_search=Tk()
        button1 = Button(window_mat_search,text='écran',command=caseecron_search,font=('Arial',10,'bold')) 
        button2 = Button(window_mat_search,text='battrie',command=casebattrie_search,font=('Arial',10,'bold'))
        button3 = Button(window_mat_search,text='équipement rsd',command=caseequipement_rsd_search,font=('Arial',10,'bold'))
        button4 = Button(window_mat_search,text='Camera',command=casecamera_search,font=('Arial',10,'bold'))
        button5 = Button(window_mat_search,text='écouteur',command=caseecouteur,font=('Arial',10,'bold')) 
        button6 = Button(window_mat_search,text='Mic',command=casemic,font=('Arial',10,'bold'))
        button7 = Button(window_mat_search,text='Capteur',command=casecapteur,font=('Arial',10,'bold'))
        button8 = Button(window_mat_search,text='mémoire',command=casememoire_serch,font=('Arial',10,'bold'))
        button9 = Button(window_mat_search,text='sim',command=casesim,font=('Arial',10,'bold'))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()
        window_mat_search.mainloop()
        
        
def caseecron_search():
        def search_ecron():
                x=serche_input.get()
                ecron=["7,7X4,4","8,9X5","11,1X6,2","13,3X7,5","15,5X8,7","17,5X10","19,5X11,2"]
                if x in ecron:
                        reslt=Label(window_ecron_search,text="cette valeur existe",font=('Arial',12,'bold'))
                        reslt.pack()     
                else:
                        reslt=Label(window_ecron_search,text="cette valeur n'existe pas",font=('Arial',12,'bold'))
                        reslt.pack() 
                        
        window_ecron_search=Tk()
        serche_input=Entry(window_ecron_search)
        serch_button=Button(window_ecron_search,text="chercher",command=search_ecron,font=('Arial',10,'bold'))
        serch_button.pack()
        serche_input.pack()
        window_ecron_search.mainloop() 

def casebattrie_search():
        def search_battrie():
                x=serche_input.get()
                battrie=["1500MAH","2000MAH","2300MAH","2500MAH","2800MAH","3000MAH","3500MAH","3900MAH","4000MAH","8000MAH"]
                if x in battrie:
                        reslt=Label(window_battrie_search,text="cette valeur existe",font=('Arial',12,'bold'))
                        reslt.pack()     
                else:
                        reslt=Label(window_battrie_search,text="cette valeur n'existe pas",font=('Arial',12,'bold'))
                        reslt.pack() 
                        
        window_battrie_search=Tk()
        serche_input=Entry(window_battrie_search)
        serch_button=Button(window_battrie_search,text="chercher",command=search_battrie)
        serch_button.pack()
        serche_input.pack()
        window_battrie_search.mainloop() 

def caseequipement_rsd_search():
        def search_equipement_rsd():
                x=serche_input.get()
                equipement_rsd=["bluetooth","wifi","NCF"]
                if x in equipement_rsd:
                        reslt=Label(window_rsd_search,text="cette valeur existe",font=('Arial',10,'bold'))
                        reslt.pack()     
                else:
                        reslt=Label(window_rsd_search,text="cette valeur n'existe pas",font=('Arial',10,'bold'))
                        reslt.pack() 
                        
        window_rsd_search=Tk()
        serche_input=Entry(window_rsd_search)
        serch_button=Button(window_rsd_search,text="chercher",command=search_equipement_rsd,font=('Arial',10,'bold'))
        serch_button.pack()
        serche_input.pack()
        window_rsd_search.mainloop()

def casecamera_search():
        def camera_search():
                x=serche_input.get()
                camera=["12MGP","14MGP","16MGP","18MGP","20MGP"]
                if x in camera:
                        reslt=Label(window_camera_search,text="cette valeur existe",font=('Arial',10,'bold'))
                        reslt.pack()     
                else:
                        reslt=Label(window_camera_search,text="cette valeur n'existe pas",font=('Arial',10,'bold'))
                        reslt.pack() 
                        
        window_camera_search=Tk()
        serche_input=Entry(window_camera_search)
        serch_button=Button(window_camera_search,text="chercher",command=camera_search,font=('Arial',10,'bold'))
        serch_button.pack()
        serche_input.pack()
        window_camera_search.mainloop()

def caseram_serach():
        def ram_search():
                x=serche_input.get()
                ram=["1GO","2GO","4GO","6GO","8GO","16GO","32GO"]
                if x in ram:
                        reslt=Label(window_ram_search,text="cette valeur existe",font=('Arial',10,'bold'))
                        reslt.pack()     
                else:
                        reslt=Label(window_ram_search,text="cette valeur n'existe pas",font=('Arial',10,'bold'))
                        reslt.pack() 
                        
        window_ram_search=Tk()
        serche_input=Entry(window_ram_search)
        serch_button=Button(window_ram_search,text="chercher",command=ram_search,font=('Arial',10,'bold'))
        serch_button.pack()
        serche_input.pack()
        window_ram_search.mainloop()


def caserom_serach():
        def rom_search():
                x=serche_input.get()
                rom=["2GO","4GO","8GO","16GO","32GO","64GO","128GO","256GO","512GO","1TO"]
                if x in rom:
                        reslt=Label(window_rom_search,text="cette valeur existe",font=('Arial',10,'bold'))
                        reslt.pack()     
                else:
                        reslt=Label(window_rom_search,text="cette valeur n'existe pas",font=('Arial',10,'bold'))
                        reslt.pack() 
                        
        window_rom_search=Tk()
        serche_input=Entry(window_rom_search)
        serch_button=Button(window_rom_search,text="chercher",command=rom_search,font=('Arial',10,'bold'))
        serch_button.pack()
        serche_input.pack()
        window_rom_search.mainloop()

def casememoire_serch():
        window_memoire=Tk()
        button1 = Button(window_memoire,text='RAM',command=caseram_serach,font=('Arial',10,'bold')) 
        button2 = Button(window_memoire,text='ROM',command=caserom_serach,font=('Arial',10,'bold'))
        button1.pack()
        button2.pack()


def materiel():
    window = Tk()
    button1 = Button(window,text='Affichge du materiel',command=casemat,font=('Arial',15,'bold'))
    button2 = Button(window,text='Cherche sur une valeur de materiel',command=casemat_search,font=('Arial',15,'bold'))
    button1.pack()
    button2.pack()
    window.mainloop()

def Window():
    wwin = Toplevel()
    def submit_win() :
        v = str(wind_entry.get())
        S = system('Windows',v)
    
        M =["Me","2000SP2","XP","2000 SP3","XP MEDIA CENTER","XP SP3","VISTA","VISTA SP2","7","8","8.1","10","11"]
        if S.version in M :
                LL= Label(wwin,text="This version is available")
                LL.pack()
        else:
                LL= Label(wwin,text="This version is not available")
                LL.pack()
    
    L = Label(wwin,text="Please enter your Windows version :",font=('Arial',15,'bold')).pack()
    wind_entry = Entry(wwin,font=('Arial',10))
    wind_entry.pack()
    submit_button = Button(wwin,text="submit",command=submit_win).pack()

def IOS():
  iwin = Toplevel()
  def submit_ios() :
    v = int(ios_entry.get())
    S = system('IOS',v)
    if S.version<16 and S.version>0 :
      LL= Label(iwin,text="This version is available")
      LL.pack()
    else:
      LL= Label(iwin,text="This version is not available")
      LL.pack()

  L = Label(iwin,text="Please enter your ios version :",font=('Arial',15,'bold'))
  L.pack()
  ios_entry = Entry(iwin,font=('Arial',10))
  ios_entry.pack()
  submit_button = Button(iwin,text="submit",command=submit_ios).pack()

def ANDROID():
  awin = Toplevel()
  def submit_and() :
    v = float(and_entry.get())
    S = system('ANDROID',v)
    
    M =[1.0,1.1,1.5,1.6,2.0,2.1,2.2,2.3,3.0,3.1,3.2,4.0,4.1,4.2,4.3,4.4,5.0,5.1,6.0,7.0,7.1,8.0,8.1,9,10,11,12]
    for x in M :
     if S.version == x :
       LL= Label(awin,text="This version is available")
       LL.pack()
     else:
       LL= Label(awin,text="This version is not available")
       LL.pack()
     break
       

  L = Label(awin,text="Please enter your Android version :",font=('Arial',15,'bold'))
  L.pack()
  and_entry = Entry(awin,font=('Arial',10))
  and_entry.pack()
  submit_button = Button(awin,text="submit",command=submit_and).pack()

def sys():
    syswindow = Tk()
    ios = Button(syswindow,text="IOS",command=IOS,font=("Arial",10,'bold')).pack()
    android = Button(syswindow,text="ANDROID",command=ANDROID,font=("Arial",10,'bold')).pack()
    Windows = Button(syswindow,text="Windows",command=Window,font=("Arial",10,'bold')).pack()
    syswindow.mainloop()
    
windows_perncipal=Tk()
button_mat = Button(text="Materiel",command=materiel,font=('Arial',15,'bold'))
button_sys = Button(text="System d'exploitation",command=sys,font=('Arial',15,'bold'))
button_mat.pack()
button_sys.pack()
windows_perncipal.mainloop()
