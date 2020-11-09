import socket
import pickle
import time
import os
import sys
import pyautogui as gui

imeRacunara = socket.gethostname()    
IP_Adresa = socket.gethostbyname(imeRacunara)
PoslednjiBroj = int(IP_Adresa.split(".")[3])


HOST = IP_Adresa
PORT = 2222
serverIP = "192.168.0.144" 
#kreiramo socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
s.settimeout(7)


def send_image(MyIP,serverIP):
    print("send brt")
    gui.screenshot("my_screenshot.png")
    
    sock = socket.socket()         # Create a socket object
    host = serverIP # Get local machine name
    port = 9999                 # Reserve a port for your service.
    #sock.bind((MyIP, 9999))
    sock.connect((host, 8888))
    #s.send("Hello server!")
    f = open('my_screenshot.png','rb')
    print ('Sending...')
    l = f.read(1024)
    while (l):
        print ('Sending...')
        sock.send(l)
        l = f.read(1024)
    f.close()
    sock.send(pickle.dumps("END"))
    time.sleep(3)
    print ("Done Sending")

    sock.close()   
    os.remove("my_screenshot.png")

    print("gotovo")
    sock.shutdown(socket.SHUT_RDWR)
    
    
def getMacAddress(): 
    for line in os.popen("ipconfig /all"): 
        if line.lstrip().startswith('Physical Address'): 
            mac = line.split(':')[1].strip().replace('-','.') 
            break 

    return mac

def slanjePodataka(serverIP):
    podatak = {"komanda" : "DATA","IME" : imeRacunara , "IP" : IP_Adresa , "BROJ" :  PoslednjiBroj, "MAC" : getMacAddress()}
    podatakByte = pickle.dumps(podatak)
    s.sendto(podatakByte, (serverIP,3333))
    
def slanjeStanjaRacunara(serverIP,PORT):
    podatak = {"komanda" : "STATE", "STATE" : "ON"}
    print(podatak)
    podatakByte = pickle.dumps(podatak)
    s.sendto(podatakByte, (serverIP,PORT))
 
    
    

    
saljiPodatke = True
serverIP = "192.168.0.144" 
while True:
    
    if(saljiPodatke == True):
        time.sleep(3)
        print("Klijent pokusava da posalje podatke")
        slanjePodataka(serverIP)
    try:
        primljeniOdgovor = s.recv(1024)
        primljeniOdgovorRecnik = pickle.loads(primljeniOdgovor)
        
        if (primljeniOdgovorRecnik["komanda"] == "OFF"):
            #os.system("shutdown /s /t 1")
            print("Gasim racunar")
            
        elif (primljeniOdgovorRecnik["komanda"] == "OK"):
            saljiPodatke = False
            print("Server je primio podatke")

        elif (primljeniOdgovorRecnik["komanda"] == "CHECK"):
            serverPORT = primljeniOdgovorRecnik["PORT"]
            slanjeStanjaRacunara(serverIP, serverPORT)

        elif (primljeniOdgovorRecnik["komanda"] == "CHECK_SCR"):
            serverPORT = primljeniOdgovorRecnik["PORT"]
            slanjeStanjaRacunara(serverIP, serverPORT)                                    

        elif (primljeniOdgovorRecnik["komanda"] == "GET_IMAGE"):
            print("run send image")
            send_image(HOST,serverIP)
            print("img")
            
    except:
        print("Nema podataka od servera")

        
    
