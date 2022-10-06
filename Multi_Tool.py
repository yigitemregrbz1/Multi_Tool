#!/usr/bin/env python

import os
import colorama
from colorama import Fore, Back, Style


print(Back.RED)
os.system("figlet MULTI TOOL")
print(Style.RESET_ALL)
print("""

Multi Tool Aracina Hos Geldiniz

1) PortScanner
2) ZaafiyetTarama
3) ExploitArama
4) Yakinda...

""")

print(Fore.YELLOW)
islemno = raw_input("Islem Numarasini Girin:")
print(Style.RESET_ALL)

if(islemno=="1"):
          print(Fore.MAGENTA)
          hedefip = raw_input("Hedef Ip Girin:")
          os.system("nmap " + hedefip)
          print(Style.RESET_ALL)

elif(islemno=="2"):
          print(Fore.GREEN)
          hedefip2 = raw_input("Hedef Ip Girin:")
          os.system("nikto -h " + hedefip2)
          print(Style.RESET_ALL)
elif(islemno=="3"):
      print(Fore.BLUE)
      anahtarkelime = raw_input("Anahtar Kelime Girin:")
      os.system("searchsloit " + anahtarkelime)
      print(Style.RESET_ALL)

elif(islemno=="4"):
            print(Fore.RED)
            print("Yakinda...")
            print(Style.RESET_ALL)
else:
       print(Fore.RED)
       print("Hatali Secim")




