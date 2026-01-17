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
        
#Write Game over as a function 
#game over for stress lvel and study progress


