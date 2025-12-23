#Writing a game here
#let player to enter thier name and gender first 

import termcolor
import pyfiglet
name=str(input("Enter your name: "))
while name=="" or name==" ":
    print("You did not enter your name!")
    name=str(input("Enter your name: "))
 
gender=["m","f","M","F","Male","male","MALE","Female","female","FEMALE"]
playerG=str(input("Enter your gender(M/F): ") )
while playerG not in gender :
    print("Invalid Gender!")
    playerG=str(input("Enter your gender(M/F): ") )
    
#setting number of attempts
attempts=1 
with open("playerdata.txt","a") as f:
   f.write("Player Name: "+name+"\n")
   f.write("Player Gender:"+playerG.capitalize()+"\n")
   f.write("Number of Attempts:"+str(attempts)+"\n")

#front part of story
print("Game Start!!!")
print("------------------------------------------------------------------------------------------ ")
print("You are a university student who has already passed the SPM exam for a long time. One day, when you walked back home after ")
print("you finished your lectures,suddenly fell into a big hole… ")
input()
print("After the you woke up,you noticed that you are in a new world that you never been in… suddenly a virtual taskbar appeared in front of you. ")
print("------------------------------------WELCOME TO SPM SURVIVAL SIMULATOR------------------------------------")
input()
print(f'A female voice echoed in your head:"Hi {name}",My name is Siri,I am your virtual assistant in this world.')
print("Let me simply explain what happened to you.You have been trapped in this world , all you have to do is finish the mission given to you. ")

#simply expalin to the player game rules

print("""
┌──────────────────────────┐
│  WELCOME TO SPM          │
│  SURVIVAL SIMULATOR!     │
│                          │
│  STUDY PROGRESS: 0       │
│  STRESS LEVEL: 0         │
│  MOOD STATE: NEUTRAL     │
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘
""")

print("A virtual task bar appeared in front of you,showing your current study progress,stress level and mood state.")
input()
print("Starting from today ,you will be given 20 days to study for your SPM exam.Everyday you will be given different types of" \
"activities,choose between leisure activities or study.Be careful with your choices because it will affect wether you can stay" \
"in this world forever or go back to your previous world.")

print("------------------------------------------------------------------------------------------------------------------------------")
input()
print("In daily life, if you choose to study, study progress +5, but if you answer the questios wrongly, stress level +2." \
"If you choose leisure activities, stress level-5.If your study progress less than 50 a day before SPM ,you cannot attempt SPM(Mission Fail).")
print("")
print("You should manage your stress level and study progress properly and pass ypur SPM exam withan overall average of 40% " \
"and above to win the game.You will be asigned for studying five subjects which are MAlay,English,Sejarah,Math and Science.")

print(pyfiglet.figlet_format("Good Luck!",font="starwars"))
input()

#let sp= study progress, sl=stress level
sp=int(0)
sl=int(0)
ms=["Happy","Neutral","Sad","Stressed"]
