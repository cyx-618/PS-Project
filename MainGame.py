#Writing a game here
#import random module for emoji, can ask emoji randomly no need to insert emoji one by one
import random
emoji_happy=['😀', '😁', '😆', '😄', '😃', '😊', '😇', '🤗', '😎', '🥳','😀','😁','😆','😄','😃','😊','😇','🤗','😎','🥳', '🤗', '😌', '😏', '😙', '😚', '😛', '😜', '😝', '🤪', '😍', '😆', '😄', '😃', '😁']
emoji_study=['📚','📖','📝','🖊️','🖋️','✏️','📒','📓','📔','📕','📗','📘','📙','📑','🔖','🏷️','🗂️','🗒️','🗓️','📅']
emoji_correct=['✅','✔️','👍','👏','🙌','💪','🌟','🏆','🎉','🥳']
emoji_wrong=['❌','✖️','👎','😞','😔','😕','🙁','☹️']
emoji_rest=['😴','💤','🛌','🛏️','🛋️','🪑','🧸','🛍️','🎮','🕹️']
emoji_fighting=['💪','🔥','⚔️','🏋️‍♂️','🤼‍♀️','🤺','🥊','🤜','🤛','🛡️']
kaomoji_fighting=["(ง •̀_•́)ง","٩(ˊᗜˋ*)و","(ง'̀-'́)ง","(ง°ل͜°)ง","(ง⌐□ل͜□)ง","(ง ͠° ͟ل͜ ͡°)ง","(ง •̀_•́)ง🔥","(ง'̀-'́)ง🔥","٩(๑`ȏ´๑)۶","(ง'̀-'́)ง💥"]
kaomoji_happy=['(＾▽＾)','(≧ω≦)','(☆▽☆)','(•‿•)','(｡•̀ᴗ-)✧','(★^O^★)','(⌒‿⌒)','(•‿•)','(｡♥‿♥｡)','(づ｡◕‿‿◕｡)づ']
#import emoji module end

#color
color_red="\033[31m"
color_green="\033[32m"
color_yellow="\033[33m"
color_blue="\033[34m"
color_reset="\033[0m"
color_pink="\033[35m"
color_skyblue="\033[36m"
#color end
#let player to enter thier name and gender first (by kjq)

import termcolor
import pyfiglet
import colorama
from colorama import Fore,Back  #(by rc)

colorama.init(autoreset=True)
name=str(input("Enter your name: "))
while name=="" or name==" ":
   print(f"{Fore.RED}You did not enter your name!")
   name=str(input("Enter your name: "))

gender=["m","f","M","F","Male","male","MALE","Female","female","FEMALE"]
playerG=str(input("Enter your gender(M/F): ") )
while playerG not in gender :
   print(f"{Fore.RED}Invalid Gender!")
   playerG=str(input("Enter your gender(M/F): ") )
   
#setting number of attempts
attempts=1 
with open("playerdata.txt","a") as f:
   f.write("Player Name: "+name+"\n")
   f.write("Player Gender:"+playerG.capitalize()+"\n")
   f.write("Number of Attempts:"+str(attempts)+"\n")

#front part of story
print(f"{Fore.GREEN}Game Start!!!")
print("------------------------------------------------------------------------------------------ ")
print("You are a university student who has already passed the SPM exam for a long time. One day, when you walked back home after you finished your lectures,suddenly fell into a big hole…  ")

print(f"""{Fore.CYAN}
      
            |   _   _                 
      . | . x .|.|-|.|                  __
   |\ ./.\-/.\-|.|.|.|                 (  )
~~~|.|_|.|_|.|.|.|_|.|~~~               ‾‾

""")
input()
print("After the you woke up,you noticed that you are in a new world that you never been in… suddenly a virtual " \
"taskbar appeared in front of you. ")
print(f"{Fore.CYAN}------------------------------------WELCOME TO SPM SURVIVAL SIMULATOR------------------------------------")
input()
print(f'A female voice echoed in your head:"Hi {name}",My name is Siri,I am your virtual assistant in this world.')
print("Let me simply explain what happened to you.You have been trapped in this world , all you have to do is fin-" \
"ish the mission given to you. ")

#simply expalin to the player game rules

print(f"""{Fore.BLUE}
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

print("A virtual task bar appeared in front of you,showing your current study progress,stress level and mood" \
" state.")
input()
print("Starting from today ,you will be given 20 days to study for your SPM exam.Everyday you will be given different types of " \
"activities,choose between leisure activities or study.Be careful with your choices because it will affect wether you can stay" \
"in this world forever or go back to your previous world.")

print(f"""{Fore.LIGHTMAGENTA_EX}
      
   _______                  ____  ____ 
   /      /,                / __ \/ __ \                   ___
  /      //                / / / / /_/ /                  |[_]|
 /______//                / /_/ / _, _/                   |+ ;|    
(______(/                 \____/_/ |_|                    `---'
         
      
""")

print("----------------------------------------------------------------------------------------------------------")
input()
print(f"In daily life, if you choose to study, study progress +5, but if you answer the questios wrongly, stress level +2." \
      "If your stree level reaches 80 and above it consider as {Fore.RED}Mission Fail."\
f"If you choose leisure activities, stress level-5.If your study progress less than 50 a day before SPM ,you cannot attempt SPM {Fore.RED}(Mission Fail).")
print("")
input()
print(f"You should manage your{Fore.RED} stress level and study progress properly and pass ypur SPM exam withan overall average of 40% " \
f"{Fore.RED}and above {Fore.RESET}to win the game.You will be asigned for studying five subjects which are {Fore.YELLOW}Malay,English,Sejarah,Math and Science.")
input()
print(f"{Fore.MAGENTA}{pyfiglet.figlet_format('Good Luck Pals!',font='starwars')}")
input()

#20 days simulation before spm start
#DAY 1
#let sp =study progress, sl=stress level

sp=0
sl=0

print("Today is the first day of your SPM exam preparation journey.")
print("Your main mission for today is study ",f"{color_blue}Bahasa Melayu!{color_reset}")
print(f"{color_green}(⚠️ Notice: This subject is very important in SPM!){color_reset}")
print("Stay focused and keep pushing forward!",random.choice(kaomoji_fighting))
print()
print("Do you want to "
      f"{color_red}STUDY{color_reset}", #change "study" to red and then reset the color 
      random.choice(emoji_study),
      "or ",
      f"{color_red}PLAY GAMES(Card game){color_reset}", #change "play games" to red and then reset the color
      random.choice(emoji_rest),"today?")
print("STUDY or PLAY")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="PLAY":
   print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or PLAY.{color_reset}")
   choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end
#user want to study
if choice=="study" or choice=="STUDY" or choice=="Study":
   #study progress+5 
   #use for loop to ask 5 questions
   sp+=5
   questions=[
      "1) Dalam cerita-cerita zaman dahulu, Sang Kancil ialah seekor __________ yang pintar.",
      "2) Selepas mandi, dia mengenakan __________ pada badannya agar harum.",
      "3) Ah Meng terpaksa bercakap dengan nada yang _______ kerana ayahnya mengalami masalah pendengaran.",
      "4) Kenaikan harga barangan keperluan menjelang musim perayaan begitu ___________ sehingga sukar dikawal oleh kerajaan.",
      "5) Kamus dwibahasa edisi baharu yang __________ itu berharga RM45.00 sahaja."
   ]
   #multiple choice 4 options for each question
   options=[
      ["A. Orang","B. Haiwan","C. Makhluk","D. Ternakan"],
      ["A. bunga-bungaan","B. ubat-ubatan","C. biji-bijian","D. bau-bauan"],
      ["A. kuat","B. kasar","C. tinggi","D. kesat"],
      ["A. mengejut","B. menonjol","C. mendesak","D. mendadak"],
      ["A. nipis","B. tebal","C. berkilat","D. berwarna"]
   ]
   #store for correct answer for each question
   answers=[
      "B","D","C","D","B"
   ]
   #explaination for each questions
   explainations=[
      "Sang Kancil adalah watak dalam cerita rakyat yang terkenal sebagai haiwan yang cerdik. Oleh itu, pilihan yang tepat untuk melengkapkan ayat tersebut adalah 'Haiwan', kerana ia merujuk kepada jenis makhluk yang dimaksudkan.",
      "Pilihan yang tepat adalah 'bau-bauan' kerana ia merujuk kepada wangian yang digunakan selepas mandi untuk membuat badan harum. 'Bunga-bungaan', 'ubat-ubatan', dan 'biji-bijian' tidak sesuai dalam konteks ini.",
      "Ah Meng perlu bercakap dengan nada yang tinggi kerana ayahnya mengalami masalah pendengaran. Ini bermakna suara perlu lebih kuat dan jelas agar ayahnya dapat mendengar dengan baik.",
      "Kenaikan harga barangan keperluan yang 'mendadak' menunjukkan perubahan yang cepat dan drastik, menjadikannya sukar untuk dikawal oleh kerajaan. Pilihan lain tidak sesuai dengan konteks yang menggambarkan situasi ini.",
      "Kamus dwibahasa yang 'tebal' menunjukkan bahawa ia mempunyai banyak halaman dan maklumat, menjadikannya lebih berharga. Pilihan lain seperti 'nipis' dan 'berkilat' tidak sesuai dengan konteks harga yang diberikan."
   ]
   #initial score and question number
   score=0
   question_number=0
   #queation loop
   print("Great! Let's do some quiz for Bahasa Melayu.",random.choice(emoji_happy))
   #use for loop to go through all questions
   for question_number in range(len(questions)):
      print("-"*100)
      print()
      print(questions[question_number])
      #print iption for each question
      for option in options[question_number]:
            print(option)
      print()
      #ask for answer
      answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      while answers_input not in ["A","B","C","D"]:
            #check whether the input is valid or not
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      #check the correctness of the answer
      if answers_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}Excellent!! You got it right.{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
      else:
            sl+=2
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Almost there! Try again.{color_reset}",random.choice(kaomoji_fighting))
      print()
      print(f"{color_skyblue}Explanation:",explainations[question_number],f"{color_reset}")
      print()
      print("Your current score is :", score,"out of",len(questions))
      print()
      print("Keep moving forward!",random.choice(kaomoji_fighting))
      print()
      input(f"{color_red}Press Enter to continue...{color_reset}")

   question_number=question_number+1
   print()
   print("💪",f"{color_pink}Quiz Ended!!!{color_reset}") 
   print("Your final score is:",score,"out of",len(questions),random.choice(kaomoji_happy))
   
else:
   #stress level-5
   sl-=5
   #user want to play game
   ascii_art_games="""
   ┌─────────┐
   │A        │
   │         │
   │    ♠    │
   │         │
   │        A│
   └─────────┘
   """
   print("You chose to play games today. Enjoy your time! (｡•̀ᴗ-)✧") 
   print(ascii_art_games)
   print()
   print("See you tomorrow for more studying!", random.choice(kaomoji_happy))

#define a special function for mood state
ms=None
def mood_state(ms):
   if sl>=80:
      print(f"{Fore.RED}Mission Fail! ")
      return "Stressed Out"
      
   elif sl>=65:
      print(f"{Fore.RED}Caution!⚠️ Your stress level is at a dangerous !Low down your stress level first!")
      return "High Stress"
      

   else:
      print(f"Your mood state is stable")
      return"Good"
      
input()
print(f"""{Fore.BLUE}
      
┌──────────────────────────┐
│  DAY 1:                  │
│                          |
│  STUDY PROGRESS:{sp}     
│  STRESS LEVEL: {sl}      
│  MOOD STATE: {mood_state(ms)}      
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘

""")
input()
#Day 1 End
#Day2 START

print("Day 2...")
print("18Days left")
print("-"*100)
print("Today is the second day of your SPM exam preparation journey.")
print("Your main mission for today is study ",f"{color_blue}Bahasa Melayu!{color_reset}")
print(f"{color_green}(⚠️ Notice: This subject is very important in SPM!){color_reset}")
print("Stay focused and keep pushing forward!",random.choice(kaomoji_fighting))
print()
print("Do you want to ",f"{color_red}STUDY{color_reset}", random.choice(emoji_study), "or ",f"{color_red}WATCH CARTOON{color_reset}",random.choice(emoji_rest),"today?",f"{color_pink}(Watching Totoro, which used to be your and your brother's favourite cartoon.)",f"{color_reset}")
print("STUDY or WATCH CARTOON")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="WATCH CARTOON":
   print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or WATCH CARTOON.{color_reset}")
   choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#loop for study
if choice=="STUDY":
   sp+=5
   print("Great! Let's do some quiz for Bahasa Melayu.",random.choice(emoji_happy))
   
   #use for loop to ask 5 questions
   questions=[
      "1) Pertahanan pasukan Perak __________ akibat daripada asakan bertubi-tubi pasukan lawan.",
      "2) Biskut coklat yang dibeli oleh emak sungguh enak dan ________ .",
      "3) Jalan di Bandaraya Kuala Lumpur menjadi_____________ apabila menjelang Hari Raya Aidil Fitri.",
      "4) Arshad makan sepuluh __________ sate dan tiga __________ nasi himpit di warung Mak Cik Gayah.",
      "5) Budak itu _________oleh ayahnya sebanyak dua kali kerana berbohong."
   ]

   #multiple choice 4 options for each question
   options=[
      ["A. hiruk-pikuk","B. kucar-kacir","C. kacau-bilau","D. haru-biru"],
      ["A. rangup","B. lemau","C. rapuh","D. hangit"],
      ["A. lengang","B. senyap","C. muram","D. suram"],
      ["A. batang...potong","B. cucuk...ketul","C. ketul...ulas","D. bungkus...butir"],
      ["A. dihentam","B. desebat","C. digasak","D. ditindas"],
   ]
   #store for correct answer for each question
   answers=[
      "B","A","A","B","B"
   ]

   #explaination for each questions
   explainations=[
      "Pilihan 'kucar-kacir' menggambarkan keadaan yang tidak teratur dan huru-hara, sesuai dengan situasi pertahanan pasukan Perak yang terjejas akibat asakan bertubi-tubi. Pilihan lain tidak tepat menggambarkan konteks ini.",
      "Pilihan 'rangup' adalah yang paling sesuai kerana ia menggambarkan biskut coklat yang enak dan mempunyai tekstur yang garing. 'Lemau', 'rapuh', dan 'hangit' tidak sesuai kerana tidak mencerminkan rasa enak dan tekstur yang diinginkan.",
      "Jalan di Bandaraya Kuala Lumpur menjadi 'lengang' menjelang Hari Raya Aidil Fitri kerana ramai orang pulang ke kampung, menyebabkan suasana menjadi tenang dan kurang sibuk.",
      "Pilihan 'cucuk...ketul' adalah tepat kerana 'cucuk' merujuk kepada cara penyajian sate, manakala 'ketul' sesuai untuk nasi himpit yang biasanya dihidangkan dalam bentuk ketulan.",
      "Pilihan 'disebat' adalah tepat kerana ia merujuk kepada tindakan menghukum dengan menggunakan rotan atau sebat, yang sesuai dalam konteks ayah menghukum anaknya kerana berbohong."
   ]
   #initial score and question number
   score=0
   question_number=0
   #queation loop           
   #use for loop to go through all questions
   for question_number in range(len(questions)):
      print("-"*100)
      print()
      print(questions[question_number])
      #print option for each question
      for option in options[question_number]:
            print(option)
      print()
      #ask for answer
      answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      while answers_input not in ["A","B","C","D"]:
            #check whether the input is valid or not
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      #check the correctness of the answer
      if answers_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}That's right, keep going!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
      else:
            sl+=2
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Don't worry, try again.{color_reset}",random.choice(kaomoji_fighting))
      print()
      print(f"{color_skyblue}Explanation:",explainations[question_number],f"{color_reset}")
      print()
      print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
      print()
      print("Keep going!",random.choice(kaomoji_fighting))
      print()
      input(f"{color_red}Press Enter to continue...{color_reset}")
   question_number=question_number+1
   print()
   print("🔥",f"{color_pink}Quiz Ended!!!{color_reset}") 
   print("Your final score is:",score,"out of",len(questions),random.choice(kaomoji_happy))

#if user want to watch cartoon
else:
   sl-=5
   ascii_art_cartoon="""
   
            ,.  ,.
            ||  ||
           ,''--''.
          : (.)(.) :
         ,'        `.
         :          :
         :          :
   -ctr- `._m____m_,' 
   """

   print("You chose to watch cartoon today. Enjoy your time!", random.choice(kaomoji_happy)) 
   print(ascii_art_cartoon)
   print
   print("See you tomorrow for more studying!", random.choice(kaomoji_happy))
   input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")

input() 
print(f"""{Fore.BLUE}
      
┌──────────────────────────┐
│  DAY 2:                  │
│                          |
│  STUDY PROGRESS:{sp}     
│  STRESS LEVEL: {sl}      
│  MOOD STATE: {mood_state(ms)}      
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘

""")
input()
#Day2 End
#Day3 Start

print("Day 3...")
print("17Days left")
print("-"*100)
print("Today is the third day of your SPM exam preparation journey.")
print("Your main mission for today is study ",f"{color_blue}Bahasa Melayu!{color_reset}")
print(f"{color_green}(⚠️ Notice: This subject is very important in SPM!){color_reset}")
print("Turn challenges into opportunities. Keep pushing forward!",random.choice(kaomoji_fighting))
print()
print("Do you want to ",f"{color_red}STUDY{color_reset}",random.choice(emoji_study),"or ",f"{color_red}DRAWING{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or DRAWING")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="DRAWING":
   print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or DRAWING.{color_reset}")
   choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#loop for study
if choice=="STUDY":
   sp+=5
   print("Great! Let's begin today's learning.",random.choice(emoji_happy))
   
   #use for loop to ask 5 questions
   questions=[
      "1) Walaupun Suraya dan Tania bukan adik-beradik tetapi _______________ sangat rapat seperti isi dengan kuku.",
      "2) Mahasiswa dan mahasiswi di __________ diingatkan supaya menumpukan perhatiansemasa mengikuti kuliah.",
      "3) __________ itu terlalu kacak jika dibandingkan dengan adik-beradiknya yang lain.",
      "4) Semua seluarnya sudah menjadi __________ kerana badannya sudah berisi.",
      "5) __________ yang dijual di kedai Kak Som itu segar-segar belaka kerana baru dipetik."
   ]

   #multiple choice 4 options for each question
   options=[
      ["A. dia","B. kita","C. kami","D. mereka"],
      ["A. universiti","B. sekolah","C. tadika","D. kolej"],
      ["A. Gadis","B. Wanita","C. Pemudi","D. Pemuda"],
      ["A. ketat","B. besar","C. singkat","D. longgar"],
      ["A. Kuih","B. Lauk","C. Sayur","D. Barang"],
   ]

   #store for correct answer for each question
   answers=[
      "D","A","D","A","C"
   ]

   #explaination for each questions
   explainations=[
      "Kata ganti 'mereka' digunakan untuk merujuk kepada Suraya dan Tania secara kolektif. Dalam konteks ini, 'mereka' menunjukkan hubungan rapat antara dua orang yang bukan adik-beradik, sesuai dengan frasa 'seperti isi dengan kuku'.",
      "Pilihan 'universiti' adalah tepat kerana mahasiswa dan mahasiswi biasanya merujuk kepada pelajar di institusi pengajian tinggi, di mana mereka perlu menumpukan perhatian semasa kuliah. Pilihan lain tidak sesuai dalam konteks ini.",
      "Kata 'Pemuda' merujuk pada seorang pria muda, yang sesuai dengan konteks kalimat yang membandingkan penampilan. 'Gadis', 'Wanita', dan 'Pemudi' tidak tepat karena merujuk pada perempuan, sedangkan subjeknya adalah laki-laki.",
      "Jawapan yang tepat adalah 'ketat' kerana jika badannya sudah berisi, seluar yang dipakai akan menjadi ketat. Pilihan lain seperti 'besar', 'singkat', dan 'longgar' tidak sesuai dengan konteks yang diberikan.",
      "Pilihan yang tepat adalah 'Sayur' kerana konteks menyebutkan bahawa barang yang dijual segar-segar belaka dan baru dipetik, yang merujuk kepada sayur-sayuran. Kuih dan lauk tidak sesuai dengan deskripsi tersebut."
   ]

   #initial score and question number
   score=0
   question_number=0
   
   #queation loop
   #use for loop to go through all questions
   for question_number in range(len(questions)):
      print("-"*100)
      print()
      print(questions[question_number])
      
      #print option for each question
      for option in options[question_number]:
            print(option)
      print()
      
      #ask for answer
      answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      while answers_input not in ["A","B","C","D"]:
            #check whether the input is valid or not
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      #check the correctness of the answer
      if answers_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}Well done! Keep it up.{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
      else:
            sl+=2
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Don't give up! Try again.{color_reset}",random.choice(kaomoji_fighting))
      print()
      print(f"{color_skyblue}Explanation:",explainations[question_number],f"{color_reset}")
      print()
      print("Your current score is :", score,"out of",len(questions),random.choice(kaomoji_happy))
      print()
      print("Stay motivated!",random.choice(kaomoji_fighting))
      print()
      input(f"{color_red}Press Enter to continue...{color_reset}")
   question_number=question_number+1
   print()
   print(random.choice(emoji_fighting),f"{color_pink}You've completed all the questions!{color_reset}")
   print("Your final score is:", score, "out of", len(questions), random.choice(emoji_happy))
#choice for drawing
else:
   sl-=5
   ascii_art_drawing="""
   ______
   |  O   |
   | ,|._ |
   | `A  _|__
   |__|\_\   \ O
         \  ._|.)
         \___A
         _|_ |\  SSt
   """
   print("You chose to do drawing today. Enjoy your time!", random.choice(kaomoji_happy)) 
   print(ascii_art_drawing)
   print() 
   print("See you tomorrow for more studying!", random.choice(emoji_happy))
   input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
input()
print(f"""{Fore.BLUE}
      
┌──────────────────────────┐
│  DAY 3:                  │
│                          |
│  STUDY PROGRESS:{sp}     
│  STRESS LEVEL: {sl}      
│  MOOD STATE: {mood_state(ms)}      
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘

""")
input()
#Day3 End
#Day4 Start

print("Day 4...")
print("16Days left")
print("-"*100)
print("Today is the fourth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}Bahasa Melayu!{color_reset}")
print(f"{color_green}(⚠️ Notice: This subject is very important in SPM!){color_reset}")
print("Believe in yourself and keep pushing forward!",random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or",f"{color_red}WATCHING MOVIE AT CINEMA{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or WATCH MOVIE")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="WATCH MOVIE":
   print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or WATCH MOVIE.{color_reset}")
   choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#loop for study
if choice=="STUDY":
   sp+=5
   print("Great! Let's do some quiz for Bahasa Melayu.",random.choice(emoji_happy))
   
   #use for loop to ask 5 questions
   questions=[
      "1) Walaupun harga barang-barang di kedai itu ________ namun pelanggannya tetap ramai.",
      "2) Encik Salleh berasa bangga apabila memandu kereta Ptoton buatan __________.",
      "3) Janganlah __________ bermain, banyak lagi kerja rumah yang perlu kamu selesaikan.",
      "4) Cikgu Rozita merupakan bekas __________ di Maktab Perguruan Perempuan Melayu, Melaka.",
      "5) Kaki Pak Senin digigit pacat, darah __________ meleleh di kakinya."
   ]

   #multiple choice 4 options for each question
   options=[
      ["A. murah","B. tinggi","C. mahal","D. rendah"],
      ["A. Malaysia","B. Korea","C. Jepun","D. China"],
      ["A. asyik","B. tekun","C. sering","D. kurang"],
      ["A. murid","B. pelatih","C. pelajar","D. mahasiswa"],
      ["A. cair","B. putih","C. pekat","D. merah"],
   ]

   #store for correct answer for each question
   answers=[
      "C","A","A","B","D"
   ]

   #explaination for each questions
   explainations=[
      "Pilihan 'mahal' adalah yang tepat kerana walaupun harga barang-barang di kedai itu tinggi, pelanggan tetap ramai. Ini menunjukkan bahawa harga yang tinggi tidak menghalang orang untuk membeli.",
      "Encik Salleh berasa bangga kerana memandu kereta Proton yang merupakan jenama kereta buatan Malaysia. Ini menunjukkan sokongan terhadap produk tempatan dan kebanggaan terhadap industri automotif negara.",
      "Kata 'asyik' paling sesuai untuk melengkapkan ayat tersebut, kerana ia menunjukkan bahawa seseorang terlalu terlibat dalam bermain, sehingga mengabaikan kerja rumah yang perlu diselesaikan.",
      "Cikgu Rozita merupakan bekas pelatih di Maktab Perguruan Perempuan Melayu, Melaka. Istilah 'pelatih' merujuk kepada individu yang sedang menjalani latihan untuk menjadi guru, berbeza dengan murid, pelajar, atau mahasiswa.",
      "Darah yang keluar akibat gigitan pacat biasanya berwarna merah, karena itu adalah warna darah manusia. Pilihan lain seperti cair, putih, dan pekat tidak tepat dalam konteks ini."
   ]

   #initial score and question number
   score=0
   question_number=0
   #queation loop
   #use for loop to go through all questions
   for question_number in range(len(questions)):
      print("-"*100)
      print()
      print(questions[question_number])
      #print option for each question
      for option in options[question_number]:
            print(option)
      print()
      #ask for answer
      answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      while answers_input not in ["A","B","C","D"]:
            #check whether the input is valid or not
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      #check the correctness of the answer
      if answers_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}You are amazing!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
      else:
            sl+=2
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Keep trying! You can do it.{color_reset}",random.choice(kaomoji_fighting))
      print()
      print(f"{color_skyblue}Explanation:{color_reset}",explainations[question_number])
      print()
      print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
      print()
      print("Keep going!!!",random.choice(kaomoji_fighting))
      print()
      input(f"{color_red}Press Enter to continue...{color_reset}")
   question_number=question_number+1
   print()
   print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
   print("Your final score is:", score, "out of", len(questions), random.choice(emoji_happy))

#else user want to watch movie
else:
   sl-=5
   ascii_art_movie="""
                           o
         o       /
            \     /
            \   /
            \ /
+--------------v-------------+
|  __________________      @ |
| /                  \       |
| |             ,--, |  (\)  |
| |       _ ___/ /\| |       |
| |   ,;`( )__, )  ~ |  (-)  |
| |  // o//   '--;   |       |
| \  ' o \     |     / :|||: |
|  -ooo--------------  :|||: |
+----------------------------+
   []                    []
   """
   print("You choose to watch movie at cinema today. Enjoy your time!", random.choice(kaomoji_happy)) 
   print(ascii_art_movie)
   print()
   print("See you tomorrow for more studying!", random.choice(emoji_happy))
   input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")

input()
print(f"""{Fore.BLUE}
      
┌──────────────────────────┐
│  DAY 4:                  │
│                          |
│  STUDY PROGRESS:{sp}     
│  STRESS LEVEL: {sl}      
│  MOOD STATE: {mood_state(ms)}      
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘

""")
input()
#Day4 End
#Day5 Start

print("Day 5...")
print("15Days left")
print("-"*100)
print("Today is the fifth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}FISHING{color_reset}", random.choice(emoji_rest), "today?")
print("STUDY or FISHING")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="FISHING":
   print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or FISHING.{color_reset}")
   choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#loop for study
if choice=="STUDY":
   sp+=5
   print("Great! Let's do some quiz for English.",random.choice(emoji_happy))
   
   #use for loop to ask 5 questions
   questions=[
      "1) He drives quite ________, but his brother drives really ________.",
      "2) She ________ have short hair, but now it’s long.",
      "3) How long have they ________ there?",
      "4) I ________ to Germany last year.",
      "5) I ________ been hit by a car, but luckily I just managed to get out of the way."
   ]

   #multiple choice 4 options for each question
   options=[
      ["A. slowly...fast","B. slowly...fastly","C. slow...fast","D. slow...fastly"],
      ["A. used to","B. didn't","C. before","D. use to"],
      ["A. been waited","B. been waiting","C. waiting","D. waited"],
      ["A. gone","B. went","C. go","D. goed"],
      ["A. must have","B. could have","C. can have","D. should have"],
   ]

   #store for correct answer for each question
   answers=[
      "A","A","B","B","B"
   ]

   #explaination for each questions
   explainations=[
      "We want to say how he drives, so we need to use adverbs, ‘slow’ –> adverb = ‘slowly’, ‘fast’ –> adverb = ‘fast’ (it’s irregular). So the correct answer is A: slowly...fast",
      "‘Used to’ = something was true in the past, but it isn’t true anymore.",
      "We use the present perfect (‘have’…) to show that something started in the past and continues until now. We make it continuous (…’been’ + -ing) to show that the length of the action is important.",
      "Last year was in the past. We use the past simple for completed actions in the past. ‘Go’ is an irregular verb, and the past simple form is ‘went’.",
      "‘I could have…’ = there was a possibility, but in the end it didn’t happen."
   ]

   #initial score and question number
   score=0
   question_number=0
   #queation loop
   #use for loop to go through all questions
   for question_number in range(len(questions)):
      print("-"*100)
      print()
      print(questions[question_number])
      #print option for each question
      for option in options[question_number]: #INSIDE THE FOR LOOP
            print(option)
      print()
      #ask for answer
      answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      #check whether the input is valid or not
      while answers_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
      #check the correctness of the answer
      if answers_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}Keep going, you're doing great!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
      else:
            sl+=2
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}You're stronger than you think!! Try again.{color_reset}",random.choice(kaomoji_fighting))
      print()
      print(f"{color_skyblue}Explanation:{color_reset}",explainations[question_number])
      print()
      print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
      print()
      print("Stay positive!!!",random.choice(kaomoji_fighting))
      print()
      input(f"{color_red}Press Enter to continue...{color_reset}")
   question_number=question_number+1
   print()
   print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
   print("Your final score is:", score, "out of", len(questions), random.choice(emoji_happy))

#else user want to fishing
else:
   sl-=5
   ascii_art_fishing="""
         ,%&& %&& %
   ,%&%& %&%& %&
%& %&% &%&% % &%
% &%% %&% &% %&%&,
&%&% %&%& %& &%& %
%%& %&%& %&%&% %&%%&
&%&% %&% % %& &% %%&
&& %&% %&%& %&% %&%'
'%&% %&% %&&%&%%'%
% %& %& %&% &%%
   `\%%.'  /`%&'
      |    |            /`-._           _\\/
      |,   |_          /     `-._ ..--~`_
      |;   |_`\_      /  ,\\.~`  `-._ -  ^
      |;:  |/^}__..-,@   .~`    ~    `o ~
      |;:  |(____.-'     '.   ~   -    `    ~
      |;:  |  \ / `\       //.  -    ^   ~
      |;:  |\ /' /\_\_        ~. _ ~   -   //-
jgs\\/;:   \'--' `---`           `\\//-\\///
   """
   print("You chose to fish today. Enjoy your time!", random.choice(kaomoji_happy)) 
   print(ascii_art_fishing)
   print()
   print("See you tomorrow for more studying!", random.choice(emoji_happy))
   input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")

input()
print(f"""{Fore.BLUE}
      
┌──────────────────────────┐
│  DAY 5:                  │
│                          |
│  STUDY PROGRESS:{sp}     
│  STRESS LEVEL: {sl}      
│  MOOD STATE: {mood_state(ms)}      
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘

""")
input()
#Day5 End
#Day6 Start
print("Days 6...")
print("14Days left")
print("-"*100)
print("Today is the sixth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}JUNGLE ADVENTURE (Choose this you may have incredible journey){color_reset}","🤩🔥", "today?")
print("STUDY or JUNGLE ADVENTURE (A secret mysterious adventure...🤫)")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="JUNGLE ADVENTURE":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or JUNGLE ADVENTURE.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end
#loop for study
if choice=="STUDY":
    sp+=5
    print("📚📖✨ Let's get studying!!! 🚀🔥")
    questions=[
        "1) I drink coffee ________.",
        "2) She’s from ________, so she speaks ________.",
        "3) He ________ ever works as ________ as he should.",
        "4) That smells good! What ________.",
        "5) How did this ________ broken?"
    ]

    options=[
        ["A. two times for a day","B. two times day","C. twice in day","D. twice a day"],
        ["A. Spanish...Spanish","B. Spain...Spainese","C. Spain...Spanish","D. Spanish...Spain"],
        ["A. hard...hardly","B. hardly...hard","C. hardly...hardly","D. hard...hard"],
        ["A. are you cooking?","B. do you cooking?","C. do you cook?","D. are you cook?"],
        ["A. get","B. become","C. was","D. be"],
    ]

    answers=[
        "D","C","B","A","A"
    ]

    explainations=[
        "‘Two times’ is not wrong, but native speakers usually say ‘twice’. We use ‘a’ in phrases like this: ‘once an hour’, ‘twice a month’, ‘three times a week’, etc.",
        "Spain is the country and ‘Spanish’ is the adjective for the people or the language.",
        "‘Hardly’ = ‘almost not’, so ‘hardly ever’ = ‘almost never’‘Work hard’ = ‘work a lot’, ‘work well’, etc.‘Hard’ and ‘hardly’ are both adverbs, but with very different meanings. Don’t confuse them!",
        "We use the present continuous (‘be’ + -ing) to talk about something which is happening now.",
        "‘Get’ in this sentence has the meaning of ‘become’ but native speakers never use ‘become’ in this way. There are many similar phrases with ‘get’: get broken, get married, get wet, etc."
    ]

    #initial score and question number
    score=0
    question_number=0

    #queation loop
    #use for loop to go through all questions
    for question_number in range(len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        #print option for each question
        for option in options[question_number]:# inside the for loop
            print(option)
        print()
        #ask for answer
        answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answers_input not in ["A","B","C","D"]:
            #check whether the input is valid or not
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answers_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        #check the correctness of the answer
        if answers_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}You got it right!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        else:
            sl+=2
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Don't lose hope,you can do it!!! Try again.{color_reset}",random.choice(kaomoji_fighting))
        print()
        print(f"{color_skyblue}Explanation:",explainations[question_number],f"{color_reset}")
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Keep pushing forward!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score, "out of", len(questions), random.choice(emoji_happy))

#choice for jungle adventure    
else:
    sl-=5
    print("You chose to go for jungle adventure today. Enjoy your time!", random.choice(kaomoji_happy))
    print("😆🎉✨ LET’S GOOOOO!!! 🚀🔥") #hidden plot of the story game
    print()
    input()
    print("Siri send you to a mysterious mountain named 'Alien Mountain...⛰︎ '")
    print("While you are enjoying your time hiking mountain, you suddenly heard a sound ")
    sound=pyfiglet.figlet_format("Buzz~Buzz~Buzz~", font="standard")
    print(sound)
    print()
    input()
    print("You follow the sound and you hide behind a big tree and you saw a grey-two-meter tall creature, is an alien!")
    print()
    print(f"""{Fore.YELLOW}
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠶⠒⠒⠒⠒⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠉⠁⠀⠀⠀⠀⠁⠀⠐⠤⣄⠉⠓⢦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⣀⠀⠈⠳⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠈⠁⠀⠀⠉⠀⠀⠀⠁⠉⠉⠁⠀⠀⢀⡠⠀⣄⠀⠀⠘⢧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⢠⠀⠀⠀⠒⠀⠈⠒⠀⠀⠀⠠⠤⠆⠀⠁⠀⠀⠀⠁⠀⢆⠈⣇
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⠀⠈⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢸
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢀⣸
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⣼⡆⠀⠀⠀⠀⣀⡀⠠⠤⢄⣀⠤⠄⠀⠀⠀⠀⠀⠀⠀⡎⣞⡏                         ,--.  ,--.,--. 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢿⣇⣤⠄⠀⠀⢀⡉⠉⠓⠒⠒⠒⠋⠉⡁⠀⠀⠠⢤⣀⣿⢿⠀                        |  '--'  |`--' 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣉⡤⢤⢤⢤⣀⡉⠲⡀⠀⠀⠀⡴⠊⣁⡠⡤⡤⠤⣈⡻⡟⠀                        |  .--.  |,--.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⣿⣿⠛⠛⢻⢷⣯⡂⠘⠀⠀⠚⢐⣮⠿⠿⣟⣿⣿⣿⡎⣿⠀                        |  |  |  ||  | 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⡘⣿⣿⣷⣿⣿⣿⣿⡄⠀⠀⢀⣾⣷⣤⣶⣿⣿⣿⡏⣠⡏⠀                        `--'  `--'`--' 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣵⡙⢯⣻⢿⣿⣿⣿⣿⠀⠀⢸⢿⣿⣿⡿⣟⡿⢋⣼⠟⠀⠀
⢀⣠⣀⠀⠀⢠⠖⢲⡀⠀⠀⠈⢻⣄⠈⠉⠿⠿⠛⠋⠀⠀⠘⠛⠛⠿⠏⠉⢀⡽⠋⠀⠀⠀
⢸⡅⠹⡄⠀⢸⡄⢸⠇⠀⠀⠀⠀⢻⣑⡀⠀⠀⠀⠾⠖⠰⡾⡆⠀⠀⠀⣜⡽⠁⠀⠀⠀⠀
⠀⢳⡄⢷⠀⢰⠃⢻⠀⠀⠀⠀⠀⠀⠻⡷⣄⡀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠟⠁⠀⠀⠀⠀⠀
⠀⠈⢧⡈⣧⢸⡀⣼⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⠈⠉⠭⠭⠍⢁⢰⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣇⠈⡿⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠀⠁⢀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡴⢺⠯⠤⠤⠖⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡷⢶⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠻⡞⠳⢶⣾⡶⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⠁⠀⡝⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢦⠴⠃⠀⠀⣸⠀⠀⠀⢀⣀⣤⣠⠤⠾⢁⡀⣇⢠⠇⡅⠻⠦⣄⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠘⢷⣜⠒⠲⣏⠀⠀⡴⡿⠀⠀⠈⠁⠒⠋⠀⠈⠉⠀⠘⠒⠖⠁⠀⠀⠩⣳⡀⠀⠀
⠀⠀⠀⠀⠀⢹⡐⢧⢻⠀⠀⣷⠁⠀⢰⠀⠀⠀⠀⠀⠲⡶⠂⠀⠀⠀⠀⡇⠀⠀⢧⡇⠀⠀
⠀⠀⠀⠀⠀⠈⡇⠀⠈⣧⠀⣟⠀⠀⣨⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⣸⠀⠀⢩⡇⠀⠀
⠀⠀⠀⠀⠀⠀⢻⠀⠀⠘⡾⠁⠐⣾⡟⡷⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢾⣿⠁⠀⠉⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠸⡀⢰⣿⠁⢿⢄⡀⠀⠀⠴⠷⠄⠀⠀⢀⣾⡏⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣯⣆⠀⠀⢹⣟⡏⠀⢸⠦⠀⠀⠀⠀⡄⠀⠀⠀⠠⣧⣿⠀⠀⢸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣜⢦⣀⡜⡞⠀⠀⢸⡓⢀⡁⠀⠀⡇⠀⠀⡀⠐⣿⡇⠀⠀⠈⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣥⡽⠁⠀⠀⢸⣅⣤⣄⣀⣀⣀⣀⣀⣤⣈⡿⢷⡀⣀⣸⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀
         {Fore.RESET} """)
    input()
    print(f"You see him playing an strange gadget,You go up and talk to him.{Fore.BLUE}'Hi, what're you doing?'")
    input()
    print(f"{Fore.GREEN}'ffuyevfuf@hjsbf'{Fore.RESET}You don't understand him.")
    print()
    print(f"{Fore.GREEN}'Hi,I am studying this virtual world,right now.Who are you?'{Fore.RESET}He changes his language to english so you can understand him.")
    print()
    print(f"{Fore.BLUE}'My name is {name},I am trapped in this virtual world(You did not tell him more about this simulation),What's your name?'")
    input()
    print(f"{Fore.GREEN}'Oh,My name is XY-3026,you can call me'Mr Gray'Nice to meet you.'{Fore.RESET}He show you the gadget in his three fingers hands ")

    print(r"""
          
            /~~~\________/~~~\
           (  o  )      (  o  )
            \___/  ++++  \___/
             | \          / |
             |   \o____o/   |
             |%%   #### oooo|
             |______________|
   """)
    input()
    print("You started gain interested,you had a long chat with him...")
    print("You two go hiking and watch the sunset together .It was best day of your life...")
    print(f"""{Fore.YELLOW}
                                
                    \       /
                      .-"-.
                 --  /     \  --
`~~^~^~^~^~^~^~^~^~^-=======-~^~^~^~~^~^~^~^~^~^~^~`
`~^_~^~^~-~^_~^~^_~-=========- -~^~^~^-~^~^_~^~^~^~`
`~^~-~~^~^~-^~^_~^~~ -=====- ~^~^~-~^~_~^~^~~^~-~^~`
`~^~^~-~^~~^~-~^~~-~^~^~-~^~~^-~^~^~^-~^~
          """)
    print("Afterward, you got send back by Siri to your study room...")

    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
input()
print(f"""{Fore.BLUE}
      
┌──────────────────────────┐
│  DAY 6:                  │
│                          |
│  STUDY PROGRESS:{sp}     
│  STRESS LEVEL: {sl}      
│  MOOD STATE: {mood_state(ms)}      
│                          │
│  GOOD LUCK WITH YOUR     │
│  JOURNEY!                │
└──────────────────────────┘

""")
input()
#Day6 End
#Day7 Start
