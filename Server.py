import tkinter as tk
from tkinter import *
import pickle
import socket
import time
from tkinter import messagebox
import os
import xlrd
import xlwt
from xlutils.copy import copy
from ServerExcel import start
from threading import Thread
from wakeonlan import send_magic_packet
import ctypes



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
 def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        imeServera= socket.gethostname()    
        IP_Servera = socket.gethostbyname(imeServera)

        myHOST = IP_Servera
        myPORT = 1612

        def on_closing():
            if messagebox.askokcancel("Izlaz", "Da li si siguran da zelis da zatvoris porgram?"):
                self.destroy()
                exit()
            
        def dugme(ID,a,b):
            fajl = ("podaci.xls") 
          
            wb = xlrd.open_workbook(fajl) 
            sheet = wb.sheet_by_index(0) 
          
            ime = sheet.cell_value(ID, 0)
            IP = sheet.cell_value(ID, 1)
            zadnjiBroj = sheet.cell_value(ID, 2)
            MAC = sheet.cell_value(ID, 3)

            color = "dark blue"
            
            if (IP != "NONE"):

                try:
                    s.settimeout(1)
                    podatak = {"komanda" : "CHECK" , "PORT" : 1612}
                    podatakByte = pickle.dumps(podatak)
                    s.sendto(podatakByte, (IP,2222))
                    
                    time.sleep(1)
            
                    primljeniPodaci = s.recv(1024)
                    primljeniOdgovorRecnik = pickle.loads(primljeniPodaci)
                    if(primljeniOdgovorRecnik["STATE"] == "ON"):
                        color = "green"
                
                       
                except:
                    color = "red"


            
            
            return tk.Button(self,
                         bg = color,
                         fg = "white",
                         image = photo,
                         border = 4,
                         text = ime,
                         command=lambda:slanjeOFF(IP, 2222, ime, MAC, color),
                         compound = TOP,
                         height=60, width=60,
                         ).place(x=a, y=b)
            
        def slanjeOFF(HOST,PORT,ime, MAC, color):
            
            if(color == "green"):
                podatak = {"komanda" : "OFF"}
                podatakByte = pickle.dumps(podatak)
                s.sendto(podatakByte, (HOST,PORT))
                ctypes.windll.user32.MessageBoxW(0, "Racunar: " + ime +" "+ "je iskljucen" , "Uspesno!", 1)
                    
            if(color == "red"):
                send_magic_packet(MAC)
                ctypes.windll.user32.MessageBoxW(0, "Racunar: " + ime +" "+ "je ukljucen" , "Uspesno!", 1)
                    
            if(color == "dark blue"):
                ctypes.windll.user32.MessageBoxW(0, "Racunar ne postoji u bazi" , "Upozorenje!", 1)
                    

        def refresh():
            return buttons()

        def buttons():
            listaButtons =[
            dugme(25, 20,10),
            dugme(21,20,100),
            dugme(17, 20,190),
            dugme(13, 20,280),
            dugme(9,20,370),
            dugme(5, 20,460),
            dugme(1, 20,550),
            
            dugme(26, 110,10),
            dugme(22, 110,100),
            dugme(18, 110,190),
            dugme(14, 110,280),
            dugme(10, 110,370),
            dugme(6, 110,460),
            dugme(2, 110,550),

            dugme(27, 200,10),
            dugme(23, 200,100),
            dugme(19, 200,190),
            dugme(15, 200,280),
            dugme(11, 200,370),
            dugme(7, 200,460),
            dugme(3, 200,550),

            dugme(28, 400,10),
            dugme(24, 400,100),
            dugme(20, 400,190),
            dugme(16, 400,280),
            dugme(12, 400,370),
            dugme(8, 400,460),
            dugme(4, 400,550)
            ]

            for i in listaButtons:
                return i
            self.update()
            

        #reiramo socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((myHOST, 1612))

        #Port za slanje klijentu
        PORT = 2222

        self.configure(bg='SkyBlue3')

        photo = PhotoImage(file = "Slike/PC.png")
        
        tk.Button(self , text = imeServera ,image = photo,font='Helvetica 12 bold',height = 90  , width = 130 ,border = 4,compound = TOP,command=lambda:refresh(), fg = "white" ,bg = "dark blue").place(x=70 , y =670)



        buttons()



###########################################################


class Page2(Page):
 def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        imeServera= socket.gethostname()    
        IP_Servera = socket.gethostbyname(imeServera)

        myHOST = IP_Servera
        myPORT = 1612

        def on_closing():
            if messagebox.askokcancel("Izlaz", "Da li si siguran da zelis da zatvoris porgram?"):
                self.destroy()
                exit()
            
        def dugme(ID,a,b):
            fajl = ("podaci.xls") 
          
            wb = xlrd.open_workbook(fajl) 
            sheet = wb.sheet_by_index(0) 
          
            ime = sheet.cell_value(ID, 0)
            IP = sheet.cell_value(ID, 1)
            zadnjiBroj = sheet.cell_value(ID, 2)
            MAC = sheet.cell_value(ID, 3)

            color = "dark blue"


            if (IP != "NONE"):

                try:
                    s.settimeout(1)
                    podatak = {"komanda" : "CHECK_SCR", "PORT" : 1234}
                    podatakByte = pickle.dumps(podatak)
                    s.sendto(podatakByte, (IP,2222))
                    
                    time.sleep(1)
            
                    primljeniPodaci = s.recv(1024)
                    primljeniOdgovorRecnik = pickle.loads(primljeniPodaci)
                    
                    if(primljeniOdgovorRecnik["STATE"] == "ON"):
                        color = "green"
                        
                
                       
                except:
                    color = "red"



            
            
            return tk.Button(self,
                         bg = color,
                         fg = "white",
                         image = photo,
                         border = 4,
                         text = ime,
                         command=lambda:get_image(IP, ime, color),
                         compound = TOP,
                         height=60, width=60,
                         ).place(x=a, y=b)


            
        def get_image(IP,ime,color):
            
            if(color == "red"):
                ctypes.windll.user32.MessageBoxW(0, "Racunar nije ukljucen, ne mozete zahtevati screenshot", "Upozorenje!", 1)

            elif(color == "dark blue"):
                ctypes.windll.user32.MessageBoxW(0, "Racunar ne postoji u bazi", "Upozorenje!", 1)

            elif(color == "green"):
                podatak = {"komanda" : "GET_IMAGE"}
                podatakByte = pickle.dumps(podatak)
                s.sendto(podatakByte, (IP,2222))

                
                def recive_image():
                   
                    #sock = socket.socket()         # Create a socket object
                    #host = "192.168.0.144" # Get local machine name
                    #port = 8888                 # Reserve a port for your service.
                    #sock.bind((host, port))        # Bind to the port
                    f = open(ime+ '.png','wb')
                    sock.listen(5)
                    # Now wait for client connection.
                    while True:
                        c, addr = sock.accept()     # Establish connection with client.
                        print ('Got connection from', addr)
                        print ("Receiving... first while")

                        l = c.recv(1024)

                        
                        while (l):
                            print ("Receiving... sec while")
                            f.write(l)
                            l = c.recv(1024)
                        f.close()
                        print ("Done Receiving")
                        c.close()
                        break
                        print("gotovo")
                        
                    #sock.shutdown(socket.SHUT_RDWR)

                recive_image()

        

        def refresh():
            return buttons()

        def buttons():
            listaButtons =[
            dugme(25, 20,10),
            dugme(21,20,100),
            dugme(17, 20,190),
            dugme(13, 20,280),
            dugme(9,20,370),
            dugme(5, 20,460),
            dugme(1, 20,550),
            
            dugme(26, 110,10),
            dugme(22, 110,100),
            dugme(18, 110,190),
            dugme(14, 110,280),
            dugme(10, 110,370),
            dugme(6, 110,460),
            dugme(2, 110,550),

            dugme(27, 200,10),
            dugme(23, 200,100),
            dugme(19, 200,190),
            dugme(15, 200,280),
            dugme(11, 200,370),
            dugme(7, 200,460),
            dugme(3, 200,550),

            dugme(28, 400,10),
            dugme(24, 400,100),
            dugme(20, 400,190),
            dugme(16, 400,280),
            dugme(12, 400,370),
            dugme(8, 400,460),
            dugme(4, 400,550)
            ]

            for i in listaButtons:
                return i
            self.update()

        #reiramo socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((myHOST, 1234))
        #kreiramo TCP socket
        sock = socket.socket()         # Create a socket object
        host = "192.168.0.144" # Get local machine name
        port = 8888                 # Reserve a port for your service.
        sock.bind((host, port))

        #Port za slanje klijentu
        PORT = 2222

        self.configure(bg='SkyBlue3')

        photo = PhotoImage(file = "Slike/PC.png")
        
        tk.Button(self , text = imeServera ,image = photo,font='Helvetica 12 bold',height = 90  , width = 130 ,border = 4,compound = TOP,command=lambda:refresh(), fg = "white" ,bg = "dark blue").place(x=70 , y =670)

        buttons()



###########################################################


class Page3(Page):
 def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


###########################################################

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="ON - OFF", command=p1.lift, width = 23,fg = "white", bg = "dark blue")
        b2 = tk.Button(buttonframe, text="Empty", command=p2.lift, width = 23,fg = "white", bg = "dark blue")
        b3 = tk.Button(buttonframe, text="Empty", command=p3.lift, width = 23,fg = "white", bg = "dark blue")

        b1.pack(side = "left")
        b2.pack(side = "left")
        b3.pack(side = "left")

        p1.show()

if __name__ == "__main__":
    
   
    def on_closing():
            if messagebox.askokcancel("Izlaz", "Da li si siguran da zelis da zatvoris porgram?"):
                root.destroy()              
                exit()
                
    t1 = Thread(target = start)
    t1.start()
                
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.resizable(height = False , width = False)
    root.resizable(height = False , width = False)
    root.iconbitmap(r"Slike/off.ico")
    root.title("Aplikacija ON-OFF")
    root.wm_geometry("513x790")
    root.configure(bg='SkyBlue3')


    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

