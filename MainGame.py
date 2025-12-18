#Writing a game here
#let player to enter thier name and gender first 

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


print("Game Start!!!")
print("------------------------------------------------------------------------------------------ ")
print("You are a university student who has already passed the SPM exam for a long time. One day, when youwalked back home after ")
print("you finished your lectures,suddenly fell into a big hole… ")
input()
