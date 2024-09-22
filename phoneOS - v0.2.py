import time 
import sys
 # Made by @L_oeildulynx aka LynxFR
print("Welcome")

reponse = input("type start to continue...")
if reponse == "start":
    print("Press Enter to confirm...")
    input()
else:
    reponse = input("Are you sure")
    if reponse == "no":
        print("Press enter to continue...")
        input
    else:
        print("Shuttingdown...")
        exit()
        


time.sleep(2)
print("Loading...")
time.sleep(1)
print("1%")
time.sleep(1)
print("2%")
time.sleep(1)
print("3%")
time.sleep(1)
print("4%")
time.sleep(1)
print("5%")
time.sleep(1)
print("6%")
time.sleep(1)
print("7%")
time.sleep(1)
print("8%")
time.sleep(1)
print("9%")
time.sleep(1)
print("10%")
time.sleep(1) # que 14% pour le moment mais bientot les 100%
time.sleep(0)
print("Welcome to phoneOs")
print("                   made by @L_oeildulynx")

time.sleep(2)
print("Welcome User1 press enter to continue")
input()
reponse = input ("Password:   ")
if reponse == "124":
    print("Welcome user1")
    time.sleep(5)
else:
    print("The passwor is incorrect try again")
    time.sleep(2)
    reponse = input ("Password:   ")
    if reponse == "124":
        print("Welcome user1")
        time.sleep(5)
    else:
        print("To many incorrect password as been tried, shuting down for safety reasons !!!")
        time.sleep(3)
        exit()# fin du programme (big up a ce qui regarde ce message)
