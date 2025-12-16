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
title=pyfiglet.figlet_format("SPM SURVIVAL SIMULATOR",font="big")
title=termcolor.colored(title,color="green")
print(title)
print("Welcome to SPM Survival Simulator! you will be experiencing the life of a SPM student and with some challenges and miracle adventures!")
print("----------------------------------------------------------------------------------------------------------------------------------------")

#creating menu 
coloredMenu=termcolor.colored("MENU",color="blue")
coloredMenu=pyfiglet.figlet_format("MENU",font="isometric1")
print(coloredMenu)

def menu():
    print("[1] Start Game")
    print("[2]View History")
    print("[3] Exit Game\n")

menu()
option=int(input("Please select an option: "))
while option !=3:
    if option==1:
       option1()
      
    elif option==2:
     with open("playerdata.txt","r") as f:
        content=f.read()
        print(content)
    
    elif option<1 or option>3:
        print("Invalid Option!")
         
    else:
        break
    
    print()
    menu()
    option=int(input("Please select an option: "))
print("Thank you for joining the game!")

#game starting...
def opyion1():
    name=str(input("Enter your name; "))
    gender=str(input("enter your gender(M/F): "))
     #setting number of attempts
    attempts=1 
    with open("playerdata.txt","a") as f:
         f.write("Player Name: ",name,"\n")
         f.write("Player Gender:",gender.capitalize(),"\n")
         f.write("Number of Attempts:", int(attempts),"\n")


