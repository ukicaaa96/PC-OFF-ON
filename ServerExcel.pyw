import xlwt
import xlrd
import socket
import pickle
from xlutils.copy import copy
import os

def start():
    #os.system('cmd /k "ipconfig"')
    imeRacunara = socket.gethostname()    
    IP_Adresa = socket.gethostbyname(imeRacunara)
    HOST = IP_Adresa
    PORT = 3333

    #kreiramo socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))

    def slanjeOK(IP):
        podatak = {"komanda" : "OK"}
        podatakByte = pickle.dumps(podatak)
        s.sendto(podatakByte, (IP,2222))

    while True:
        primljeniPodaci = s.recv(1024)
        primljeniOdgovorRecnik = pickle.loads(primljeniPodaci)
        if(primljeniOdgovorRecnik["komanda"] == "DATA"):
            slanjeOK(primljeniOdgovorRecnik["IP"])
            

            klijentIme = primljeniOdgovorRecnik["IME"]
            klijentIP = primljeniOdgovorRecnik["IP"]
            klijentBroj = primljeniOdgovorRecnik["BROJ"]
            klijentMAC = primljeniOdgovorRecnik["MAC"]

        
            fajl = ("podaci.xls")
            rb = xlrd.open_workbook(fajl)
            sheet = rb.sheet_by_index(0)


            pozicija = 1
            for i in range(1,25):
                if (sheet.cell_value(i, 0) == klijentIme):
                    print("Racunar " + klijentIme +" vec postoji")
                    break
                elif (sheet.cell_value(i, 0) == "NONE"):
                    print("Racunar "+ klijentIme+ " je poslao svoje podatke")
                    pozicija = i
                    wb = copy(rb)
                    w_sheet = wb.get_sheet(0)

                    w_sheet.write(pozicija,0,klijentIme)
                    w_sheet.write(pozicija,1,klijentIP)
                    w_sheet.write(pozicija,2,klijentBroj)
                    w_sheet.write(pozicija,3,klijentMAC)

                    wb.save("podaci.xls")
                    break





