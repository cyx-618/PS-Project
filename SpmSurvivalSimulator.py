#***************************************************************************
#Course:CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
#LECTURE / LAB SECTION: TC2L/TL8L
#Trimester:2530
#Group Name: TL8L-14
#Names: CHEONG YI XUAN | KWONG JIA QI
#IDs: 252FC25349 | 252FC253R0
#***************************************************************************

import termcolor
import pyfiglet
import sys
title=pyfiglet.figlet_format("SPM SURVIVAL SIMULATOR",font="big")
title=termcolor.colored(title,color="green")
import colorama
from colorama import Fore
print(title)
print("Welcome to SPM Survival Simulator! you will be experiencing the life of a SPM student and with some challenges and miracle adventures!")
print("-------------------------------------------------------------------------------------------------------------------------------------")
input()
#creating menu 
coloredMenu=pyfiglet.figlet_format("Menu",font="isometric1")

def menu():
    print(coloredMenu)
    print("[1] Start Game")
    print("[2]View History")
    print("[3] Exit Game\n")
    option=int(input("Please select an option: "))
    while option !=1:
        if option==3:
         print("Thank you for joining the game!")
         sys.exit()
         break
        elif option==2:
         print("Showing History...")
         input()
         with open("playerdata.txt","r") as f:
            content=f.read()
            print(content)
         option=int(input("Please select an option: "))
        elif option not in ["1","2","3"]:
            print("Invalid Option!")
            option=int(input("Please select an option: "))
        else:
            print("Game Start!")
            
        
    exit

menu()    
#Write Game over as a function 
#game over for stress lvel and study progress


#writing function for the sl and sp
def sp_gameover():
   sp=30
   if sp<=50 :
      print("Your study progress is less than 50,You could not attend SPM.")
      choice=input("Do you want to start over again(Yes/No): ").upper()
      if choice not in ["YES","NO"]:
         print("Invalid Answer!") 
         choice=input("Do you want to start over again(Yes/No): ").upper()
      if choice=="YES":
         menu()
      if choice=="No":
         exit
def sl_gameover():
   sl=99 
   if sl>=80:
      print("Your stress level is too high to attend SPM.")
      print(f"{Fore.RED}Mental Unstable-Game Over")

sp_gameover()
sl_gameover()


