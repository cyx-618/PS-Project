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

#color (ANSI color formatting)(ANSI ascape codes)
color_red="\033[31m"
color_green="\033[32m"
color_yellow="\033[33m"
color_blue="\033[34m"
color_reset="\033[0m"
color_pink="\033[35m"
color_skyblue="\033[36m"
#color end

print("Day 9...")
print("11Days left")
print("-"*100)
print("Today is the ninth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}Sejarah{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very important in your SPM exam!){color_reset}")
print("Keep moving forward!!! Believe in yourself!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}go to the ANIME FEAST ?{color_reset}", random.choice(emoji_rest), "today?")
print("STUDY or ANIME FEAST")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="ANIME FEAST":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or ANIME FEAST.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
    print("-"*100)
#taskbar end

#start the study loop
if choice=="STUDY":
    print("Nice!!! Let's begin our study journey for today~~~",random.choice(emoji_happy))

    #use for loop to ask 5 question
    questions=[
        "1) Apakah tugas Temenggung dalam Kerajaan Kesultanan Melayu Melak?" ,
        "2) Bagaimanakah golongan kelas pertengahan berpendidikan Barat menentang Britiah di Burma?",
        """3) Perang Dunia Pertama berlaku pada tahun 1914 hingga 1918.
Apakah faktor yang mencetuskan perang tersebut?""",
        "4) Bagaimanakah Perjanjian Persekutuan Tanah Melayu 1948 membela nasib penduduk asal di Tanah Melayu",
        "5) Bagaimanakah Britiah menumpaskan kegiatan Min Yuen?"
    ]

    options=[
        ["A. Menjatuhkan hukuman mati","B. Mengetuai rombongan diplomatik","C. Mengawai keamanan dqalam negeri","D. Melicinkan kutipan cukai di pelabuhan","",f"{color_skyblue}Hint: Tingkatan 4 M/s 9{color_reset}"],
        ["A. Membentuk Katipunan","B. Menubuhkan Persatuan Belia Buddha","C. Menerbitkan akhbar Tribune Indige","D. Melancarkan pemberontakan Saya San","",f"{color_skyblue}Hint: Tingkatan 4 M/s 29{color_reset}"],
        ["A. Pengeboman Pearl Harbour","B. Perbezaan ideologi antara negara","C. Persengketaan Rusia dengan Britian","D. Pembunuhan pewaris takhta Austria-hungary","",f"{color_skyblue}Hint: Tingkatan 4 m/s 54{color_reset}"],
        ["A. Melindungi hak peribumi","B. Memonopoli pentadbiran negara","C. Memansuhkan kerakyatan imigran","D. Membentuk parti politik mengikut kaum","",f"{color_skyblue}Hint: Tingkatan 4 m/s 127{color_reset}"],
        ["A. Memeterai perjanjian damai","B. Membuka penempatan baru","C. Melancarkan serangan gerila","D. Menangkap pemimpin radikal","",f"{color_skyblue}Hint: Tingkatan 4 m/s 157{color_reset}"],
    ]

    answers=[
        "C","B","D","A","B"
    ]

    #Initial score and question number
    score=0
    question_number=0
    #question loop
    #use for loop to go through and print every question
    for question_number in range(len(questions)):
        print("-"*100)
        print()
        print(questions[question_number]) #print question follow the flow index0-4
        #print ooption for every question
        for option in options[question_number]: #example if question_number=0 print the first option for the first question
            print(option)
        print()
        #ask for the answer
        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        #check whether the answer enter is valid or not
        while answer_input not in ["A","B","C","D"]:
            print("⚠️",f"{color_yellow}Invalid  answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        #check the correctness of the answer
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answer!")
            print(f"{color_green}Focus and fight! Your effort today shape your future!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Keep moving forward, never give up!!{color_reset}",random.choice(kaomoji_fighting))
        print()
        print("Your current score is :", score, "out of",len(questions),random.choice(emoji_happy))
        print()
        print("You are strong than you think!!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is :", score, "our of", len(questions),random.choice(emoji_happy))

#if user choose the other choice
else:
    ascii_art_animefeast="""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠟⠋⠉⠉⠉⠉⠛⢿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠇⢀⣾⡄⠀⠀⠀⠀⠀⠀⣷⡄⠈⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡇⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠉⠁⠀⢸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡇⠰⣿⣿⠆⠀⠀⠀⠀⠀⠰⠿⠿⠗⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠠⠤⠀⠀⠀⠀⠀⠀⠀⠒⠒⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⢰⣿⡆⠀⠀⠀⠀⠀⠀⢸⣿⡆⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⢸⡿⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡆⠀⢹⠁⠀⠀⠀⠀⠀⠀⠸⠁⠀⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠺⠿⠿⠿⠿⠟⠀⢀⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠤⠤⠄⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀


"""
    print("You choose to go to the anime feast today. Enjoy your time!", random.choice(kaomoji_happy))
    print(ascii_art_animefeast)
    print()
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for the ninth day
print(f"{color_pink}~"*125,f"{color_reset}")


#start for the tenth day
print("Day 10...")
print("10Days left")
print("-"*100)
print("Today is the tenth day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Sejarah{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very important in your SPM exam!){color_reset}")
print("Fast and focused---that's how winner do it!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to the MUSIC FESTIVAL{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or MUSIC FESTIVAL")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="MUSIC FESTIVAL":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or MUSIC FESTIVAL.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Is is time to level up your brain!!",random.choice(emoji_happy))

    questions=[
        """1) Apakah ciri negara berdaulat?
      
I Pentadbiran yang sistematik
II Sempadan yang jelas
III Rakyat berbilang kaum
IV Naungan kerajaan lain
""", 
#triple " is to create multiple line string and allowing the texxt written on several line without the \n 
        "2) Mengapakah konsep pengasingan kuasa penting dalam amalan demokrasi berparlimen",
        """3) Kerajaan Persekutuan dan Kerajaan Negeri berusaha untuk membolehkan golongan pertengahan memiliki rumah kediaman.
Bagaimanakah kedua-dua kerajaan mencapai matlamat tersebut?""",
        """4) Pada tahun1962, satu referendum telah diadakan di Singapura.
Mengapakah referendum tersebut diadakan?""",
        """5) Dasar Kebudayaan Kebangsaan telah digubal pada tahun1971.
Mengapakah dasar tersebut diperkenalkan?""",
    ]

    options=[
        ["A. I dan II","B. I dan IV","C. II dan III","D. III dan IV","",f"{color_skyblue}Hint: Tingkatan 5 m/s 8-9{color_reset}"],
        ["A. Mengelakkan campur tangan luar","B. Meningkatkan mobiliti penduduk","C. Mewujudkan pemerintahan yang adil","D. Mendapat pengiktirafan antarabangsa","",f"{color_skyblue}Hint: Tingkatan 5 m/s 55{color_reset}"],
        ["A. Menyekat pembinaan rumah mewah","B. Melarang warga asing membeli rumah","C. Memperbanyakkan rumah mampu milik","D. Membeli pinjaman perumahan tanpa faedah","",f"{color_skyblue}Hint: Tingkatan 5 m/s 77{color_reset}"],
        ["A. Mengukuhkan kesetiaan rakyat","B. Mengekalkan pemerintahan British","C. Menilai pengaruh parti pembangkang","D. Menentukan sokongan gagasan Malaysia","",f"{color_skyblue}Hint: Tingkatan 5 m/s 100{color_reset}"],
        ["A. Memupuk semangat kenegerian","B. Memperkukuh integrasi nasional","C. Menghalang kemasukan pengaruh luar","D. Mengawal penggunaan bahasa asing","",f"{color_skyblue}Hint: Tingkatan 5 m/s 150{color_reset}"],
    ]

    answers=[
        "A","C","C","D","B"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}You're on fire!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Keep going---practice makes perfect!!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Nice! Your effort today=your success tomorrow!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_music="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⡀⠀⠀⠀⠀⣤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣀⣸⠏⠘⣧⠀⠀⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⡀⠈⠀⠀⠙⢛⣿⡿⠂⠀⠀⠠⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠀⠀⠀⣰⡏⠀⣀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡶⠟⠙⢷⣄⣇⠀⠀⠰⣶⣿⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠈⠛⠀⠀⠚⠛⠿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⢀⣿⠛⠛⠻⠿⣿⣿⣷⡄⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢸⡏⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠁⠀⢀⣀⠀⢠⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠿⠿⠿⣿⣶⣶⡆⠀⠘⠿⠿⠋⠀⠀⢻⣿⣿⣿⡏⠀⠀⠀⠘⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⢀⡄⠀⠀
⠀⠀⠀⠀⠀⣴⣶⣾⡏⠀⠀⠀⣀⡀⢠⡿⠀⠀⠀⠀⠀⢿⡲⠋⣇⣀⡀⠀⠸⡗⠋⣇⡀⠀
⠀⠀⠀⠀⠀⠻⣿⡿⠃⠀⠀⢺⣿⣿⣿⠃⠀⠀⡄⠀⢀⣜⣥⣄⡖⠋⠁⠀⠛⠒⣾⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠀⢰⣿⡄⠀⠀⠀⠈⠛⠀⠀⡀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⢿⡄⠀⠀⠀⠀⠐⣶⣷⠤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠘⠀⢀⣀⣠⣤⡤⠿⠀⠈⠿⠛⢛⣿⠟⠀⠁⠉⠀⠀⠀⠀⠀⠀
⠀⠈⠁⠀⠀⢦⣤⣿⣀⡀⠀⠀⠀⠉⠳⢦⣤⡀⠀⠀⠀⢰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⡀⠀⠀⠀⣰⠿⢿⡏⠁⠀⢀⡀⠀⠀⠀⣸⠃⢀⣤⣄⡈⣷⡀⠀⠐⠓⠀⠀⠀⠀⠀⠀⠀
⠚⠏⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠁⠀⠀⠀⣿⡴⠛⠁⠉⠛⠾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    print("You choose to go to the music festival today~ Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_music)
    print()
    print("See you tomorrow for more pratices!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")


#start for the eleventh day
print("Day 11...")
print("9Days left")
print("-"*100)
print("Today is the eleventh day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Sejarah{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very important in your SPM exam!){color_reset}")
print("Saty sharp, saty confident!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to the FOOD FESTIVAL{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or FOOD FESTIVAL")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="FOOD FESTIVAL":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or FOOD FESTIVAL.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Let's begin our study journey for today~",random.choice(emoji_happy))

    questions=[
        "1) Bagaimanakah Dasr Ekonomi Baru (DEB) dapat memberi keadilan kepada semua kaum?",
        """2) Dasar pembangunan Nasional (DPN) bermatlamat untuk mencapai perpaduan melalui pengagihan kekayaan negara.
Bagaimanakah hasrat tersebut dapat dicapai?""",
        """3) Setelah mencapai kemerdekaan, Mlaysia telah menjadi anggota Pertubuhan Bangsa-Bangsa Bersatu (PBB).
Mengapakah Malaysia menganggotai pertubuhan tersebut?""",
        """4) Malaysia menjadikan ASEAN sebagai platform mengisytiharkan perubahan dasar luar negara pada peringkat serantau dan global.
Bagaimanakah Malaysia merealisasikan komitmen tersebut?""",
        """5) Komuniti ASEAN ditubuhkan pada tahun 2015 melalui Deklaras Kuala Lumpur sewaktu Sidang Kemuncak ASEAN ke-27.
Apakah matlamat penubuhan komuniti tersebut?

I Menjana pertumbuhan ekonomi
II Meningkatkan kemahiran tenaga kerja
III Menetapkan nilai mata wang tunggal
IV Menjamin keselamatan serantau
""",
    ]

    options=[
        ["A. Membasmi buta huruf","B. Meningkatkan infrastruktur","C. Menyusun semula masyarakat","D. Menambah jumlah penduduk","",f"{color_skyblue}Hint: Tingkatan 5 m/s 167{color_reset}"],
        ["A. Melaksanakan ekonomi kawalan","B. Memantau pengurusan kewangan negara","C. Mengimbangi pembangunan antara negeri","D. Mengawal peningkatan golongan pertengahan","",f"{color_skyblue}Hint: Tingkatan 5 m/s 174{color_reset}"],
        ["A. Menamatkan ancaman luar","B. Memelihara kedaulatan negara","C. Mendapatkan bantuan ketenteraan","D. Menyertai perdagangan antarabangsa","",f"{color_skyblue}Hint: Tingkatan 5 m/s 198{color_reset}"],
        ["A. Mengadakan perjanjian Pertahanan Lima Negara (FPDA)","B. Menandatangani Prejanjian Umum Tarif dan Perdagangan (GATT)","C. Membina Pusat Serantau untuk Sains da Matematiik (RECSAM)","D. Mengumumkan Deklarasi Zon Aman, Bebas dan Berkecuali(ZOPFAN)","",f"{color_skyblue}Hint: Tingkatan 5 m/s 210{color_reset}"],
        ["A. I dan II","B. I dan IV","C. II dan III","D. III dan IV","",f"{color_skyblue}Hint: Tingkatan 5 m/s 242{color_reset}"],
    ]

    answers=[
        "C","C","B","D","B"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Well done!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Mistakes are just practice runs. Try again!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Push foward, even when tired.",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_food="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠖⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⣰⠟⠁⣀⣀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⡡⠊⡡⢖⡦⠀⢸⡇⠀⡞⠀⠈⢱⠀⠀⢹⡆⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⢋⠴⣫⠔⣫⠔⠋⠀⠀⢸⣇⠀⠑⠦⠤⠞⠀⠀⣰⠇⠀⠀⢀⡴⠛⠉⠀⠉⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡤⠾⣫⣼⠵⣋⠥⠋⠀⠀⠀⠀⠀⠈⠛⠷⠶⠦⣤⣀⣀⣴⠟⠀⠀⢠⡏⠂⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠖⠺⠋⠁⠘⠗⠹⣧⡚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠈⢷⣷⡄⢀⣴⠟⠁⠀⠀⣀⣠⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⢄⡄⠘⢵⣀⣤⣞⠛⠲⢦⣤⡀⠀⢀⣴⠟⠛⠫⣖⢄⣠⣀⣀⠀⠀⠈⠉⠉⠉⠀⠀⠀⢰⣟⣁⠘⢞⡌⢳⡄⠀⠀⠀
⠀⠀⢀⡴⣪⣿⡷⡆⠀⠀⠀⠀⠀⠀⠈⣿⠁⠉⠻⢦⣄⠈⢽⣷⣼⠼⠞⠁⠀⡈⢣⢟⠛⠛⠿⠷⣶⣶⣤⣀⠀⠀⠀⠘⡏⢯⣆⠈⢻⣦⠙⣦⠀⠀
⢠⢔⣿⡾⣿⢻⡇⢾⣤⠀⠀⠀⠀⠀⠀⠸⣶⣤⡀⠀⠉⠻⣦⡙⢿⣷⡄⢀⡞⠃⠀⢻⡶⠶⠶⢤⣤⣈⠙⠛⢿⣦⣄⡀⠙⣆⠻⣧⡀⠹⣷⡘⣦⡀
⠈⠛⠗⠉⠀⢣⣛⣈⣿⠀⠀⠀⠀⠀⠀⠀⢧⣈⡙⢶⣄⡀⢈⡿⠚⠛⠻⣦⠀⠀⠒⣶⠇⠀⢀⣠⡴⠿⠿⣦⣄⠈⠻⢿⣦⡘⢧⡘⢿⠶⠋⠉⠹⡇
⠀⠀⠀⠀⢀⣴⣿⠟⢳⠀⠀⠀⠀⠀⠀⠀⠘⣏⠛⢶⣌⠙⠏⠀⠀⠀⠀⣿⢿⣳⡖⠁⠀⣴⠟⠁⠀⠀⠀⠀⠱⢷⡄⠀⠻⣿⡌⢳⣼⡀⠀⢀⣴⠇
⠀⠀⠀⢀⣾⡟⢁⣰⡿⡆⠀⠀⠀⠀⠀⠀⠀⠪⣠⣞⡿⠳⣵⣤⣤⡶⢾⢿⠯⣓⣺⣧⣾⢁⠞⠉⠑⡄⠀⠀⠀⠘⣝⣆⠀⠙⣿⡄⠈⠙⠛⠛⠁⠀
⠀⠀⠀⣸⣿⢠⠋⢻⢀⢸⠀⠀⠀⠀⠀⡄⡄⠀⠁⣠⡀⢉⡬⠞⠛⠛⠋⠙⡏⢶⣾⣟⡏⡏⠀⠀⠀⡀⠀⠀⠀⢠⣏⣽⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⢰⡀⢸⣮⠸⡆⠀⠀⣀⠤⢌⣁⣠⠴⣿⠑⣁⠀⠪⣣⣾⡿⠃⠀⠀⠀⠸⣧⠓⢤⡤⠜⠁⠀⠀⠀⣸⡿⠋⠀⡴⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣧⡱⣄⠙⠻⢿⣄⣻⣋⣉⡟⠀⠀⠀⠉⠻⠊⠀⠘⠋⠁⢰⣲⠀⠀⠀⠀⠈⣦⠀⢀⣀⣠⣤⠶⠟⠋⣀⠤⠊⣴⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣷⣤⡑⠂⢤⣈⠉⠛⠛⠓⠶⠶⢤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⠶⠿⠛⠛⠉⣉⡠⠄⠒⢊⣠⣴⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⣦⣤⣉⣁⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⣀⣀⣤⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣾⣿⡿⠻⣿⣿⣿⡿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣀⠀⠉⠋⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣟⣟⣿⣿⣯⣿⣿⢿⣿⣿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⠉⠑⣴⠒⢆⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⢫⡽⡿⠿⠿⣿⢿⠿⢿⣷⣿⣾⣽⣿⣿⣿⢿⢿⣿⡇⠀⢀⣼⣤⣤⣶⢶⣼⠈⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣹⣾⢻⠐⣯⣇⣏⡳⢼⣿⣾⡏⣽⣿⠋⣾⣿⣿⣼⣿⣇⢸⢹⣿⣼⣿⣿⣾⣿⣦⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡿⢷⣤⣼⠃⣽⣿⢾⡇⣤⣿⣿⠤⣾⣿⢶⣿⣤⣬⣼⡟⠛⠘⣿⣿⣺⣿⣻⣟⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣏⣞⣛⣿⡤⣻⣿⣽⣵⣷⣯⣿⣵⣿⣿⣿⣿⣿⣿⣿⣷⢰⠉⠙⢿⣿⣿⣿⣿⣿⢻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣶⣿⣿⡟⣙⣒⡉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢆⠀⠸⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣷⣶⣦⣾⣿⣿⣿⣿⣿⣾⣿⣷⣿⣿⣿⣿⣿⣦⣳⣤⣬⣭⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    print("You choose to go to the food festival today. Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_food)
    print()
    print("See you tomorrow for more pratices!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#start for the twelfth day
print("Day 12...")
print("8Days left")
print("-"*100)
print("Today is the twelfth day of your SPM exam preparation journey")
print(f"Your main mission for today is to study {color_blue}Sejarah{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very important in your SPM exam!){color_reset}")
print("Slow progress is still progress!! Keep answering, keep learning!!!", random.choice(kaomoji_happy))
print()
print("Today your mission is do a revision for SEJARAH but you're very sad today because you sudden miss your family...")
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}WALK AROUND THE PARK (System suggest)(You may meet a person that help you to cheer up){color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or WALK AROUND THE PARK")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="WALK AROUND THE PARK":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or WALK AROUND THE PARK.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Let's do some quiz for sejarah!",random.choice(emoji_happy))

    questions=[
        "1) Apakah syarat untuk menjadi pengundi dalam Pilihan Raya Umum Pertama di Tanah Melayu?",
        "2) Mengapakah Tunku Abdul Rahman dan rombongan kemerdekaan menggunakan kapal laut dari Singapura ke Keranchi pada 1 januari 1956?",
        "3) Kedaulatan tradisional merujuk kepada",
        """4) Rancangan Integrasi Murid untuk Perpaduan (RIMUP) telah dilaksanakan di peringkat sekolah
Apakah tujuan dasar tersebut?""",
        "5) Apakah strategi yang digunakan dalam melaksanakan Dasar Ekonomi Baru?",
    ]

    options=[
        ["A. Berpengetahuan bahasa inggeris","B. Mampu berbahasa Melayu","C. Merupakan warganegara","D. Berumur 18 tahun ke atas","",f"{color_skyblue}Hint: Tingkatan 4 m/s 200{color_reset}"],
        ["A. Menjimatkan kos perjalanan","B. Mengadakan perbincangan","C. Menjelaskan misi rundingan","D. Mendapatkan sokongan luar","",f"{color_skyblue}Hint: Tingkatan 4 m/s 217{color_reset}"],
        ["A. Pematuhan terhadap perundangan","B. Pemerintahan berkuasa mutlak","C. Pengiktirafan peringkat dunia","D. Persamaan rumun bangsa","",f"{color_skyblue}Hint: Tingkatan 5 m/s 6{color_reset}"],
        ["A. Mewujudkan minat dalam pelajaran","B. Melahirkan generasi yang kreatif","C. Memupuk semangat setia kawan","D. Menonjolkan identiti kebangsaan","",f"{color_skyblue}Hint: Tingkatan 5 m/s 152{color_reset}"],
        ["A. Mewujudkan masyarakat perdagangan","B. Pengenalan perindustrian berat","C. Progrm penanaman semula","D. Menyusun semula masyarakat","",f"{color_skyblue}Hint: Tingkatan 5 m/s 167{color_reset}"],
    ]

    answers=[
        "C","B","B","C","D"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Correct! Nice focus!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}You’re improving!!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Every question you practice here builds confidence for the real SPM exam!!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_chair="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠴⡀⠖⡖⠠⠤⠤⢄⠶⢢⠤⡠⠄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠐⠌⡌⢢⡑⠬⠰⣃⢜⠴⣬⠂⣅⢢⠡⣉⠲⢡⢒⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⢀⠀⡌⠌⢇⠀⡤⢱⠀⡧⠈⠀⠼⢈⠁⢨⢁⡃⢱⠆⢢⠔⡩⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⡌⢦⡸⠊⠘⠜⣈⠆⢘⠀⡄⢓⠸⠀⡜⠸⢀⡅⡜⠀⢢⢘⠔⡎⣱⠰⡄
⠀⠀⠀⠀⠀⠀⠀⢀⢠⡖⣭⡶⠂⠀⠀⢘⡄⢋⠸⡂⠇⢌⠘⠀⡅⡖⠴⣠⢁⡘⠤⠊⠀⠈⡖⡭⡃
⠀⠀⠀⠀⠀⠀⣰⣴⣿⣿⡿⠀⠀⠀⠀⠀⡌⠬⡄⡆⢂⠜⢸⠸⡐⠧⡗⣤⡋⣔⠊⠀⠀⢰⣟⣶⡃
⠀⠀⠀⢠⣴⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⢸⠀⡅⡇⢬⠋⢸⣸⢀⢳⢃⡶⢡⠆⠀⢀⣴⣯⡿⠋⠀
⠀⢀⡸⢉⣿⡟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠆⡏⢸⣌⠰⣏⠸⡼⢠⡟⢢⣆⡴⣿⠷⠃⠀⠀⠀
⠀⢸⠄⡃⣾⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠃⡣⢸⡇⣻⡤⡘⡧⢩⣏⢳⠃⠌⠇⠀⠀⠀⠀⠀
⠀⢸⠘⡄⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣧⠆⣹⠇⣸⡅⣿⡃⣿⠠⣏⡘⢜⠂⠀⠀⠀⠀⠀
⠀⠈⡔⡌⣽⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡁⠆⠤⡐⢠⡐⠄⢦⡑⢌⠡⢃⡧⢘⡈⠀⠀⠀⠀⠀⠀
⠀⢠⠑⡤⢻⡷⠀⠀⠀⠀⢀⣀⣀⠀⠀⣴⡸⣌⠳⣌⢣⡜⣸⢣⡞⣬⢣⣹⡄⢣⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠸⣀⠁⠿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣷⣏⣿⣹⢾⣇⣿⢱⡿⣾⣷⢿⡿⢀⠇⠆⠀⠀⠀⠀⠀⠀
⠀⢈⠱⢌⢺⡜⠣⢍⡛⢭⠛⡽⢫⠟⡻⢾⡹⠶⢯⠟⡾⡹⢏⠿⣳⣏⠋⡜⠠⢎⢢⠀⠀⠀⠀⠀⠀
⠀⡈⡜⣌⢳⣎⠑⠦⠘⣀⣣⢄⣣⣌⣑⢂⠡⣉⢂⡉⡐⣁⠊⡔⢣⢿⡡⢌⠱⡈⢼⠀⠀⠀⠀⠀⠀
⠀⠓⠴⡨⣿⡀⠀⠀⠀⠀⠁⣿⣿⣿⣿⡎⠁⠀⠀⠀⠁⠀⠀⠀⠈⣻⡆⢌⠢⡑⢼⡆⠀⠀⠀⠀⠀
⠀⡘⡔⣣⡟⠇⠀⠀⠀⠀⠀⢾⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣯⢀⠣⡘⢸⡇⠀⠀⠀⠀⠀
⢀⡴⢨⡱⣟⠀⠀⠀⠀⠀⠀⣿⡿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣳⠌⢢⢁⢻⣿⠀⠀⠀⠀⠀
⠈⡑⢦⢹⡆⠀⠀⠀⠀⠀⠀⠷⣙⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠄⠣⢌⢺⣿⡀⠀⠀⠀⠀
⠀⡘⡔⣻⡀⠀⠀⠀⠀⠀⠀⢸⢡⢾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⡎⡑⠢⢜⣻⡃⠀⠀⠀⠀
⢰⢠⢏⡏⠀⠀⠀⠀⠀⠀⠀⢈⠖⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⡇⢌⡱⢸⣳⢧⠀⠀⠀⠀
⠀⡳⢪⠟⠀⠀⠀⠀⠀⠀⠀⠊⠼⠍⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⡄⢢⢹⣎⣯⠀⠀⠀⠀
⠀⢇⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢹⡄⠣⠜⠂⠈⠀⠀⠀⠀
⣧⢎⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⡄⡙⣜⠀⠀⠀⠀⠀⠀
⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⣖⡸⠀⠀⠀⠀⠀⠀
"""
    print("You choose to go for a walk in the park today...",random.choice(kaomoji_happy))
    print("˚˖𓍢ִ໋🍃✧˚.💚⋆...")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("Feeling low and sad, you decide to go far a walk in the park today. You hope the fresh air might calm your mind...")
    print("Just then, your phone suddenly light up. A notification pops up, showing a nearby park called 'Sunway park'.")
    print("You don't know why but the sense of loss fills your heart, so you decide to go...")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("The park is quiet, with only the sound of leaves rustling and birds calling in the diatance.")
    print("You're feeling too sad because you miss your family more tha usual.")
    print("As you walk along the path, you notice that a man dressed entirely in black and sitting alone on a bench.")
    print("You hesitate for a moment, then sit down beside him...")
    print(ascii_art_chair)
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("The man turns to you and ask, 'Why do you look so sad?'")
    print("You take a deep breath and answer him, 'I am trap in this world, I really miss my family.'")
    print("You don't tell the truth...")
    print("He looks deeply into your eyes and says to you, 'My name is Marcus.'")
    print("I left my family many years ago to work in another city. At first, I told myself it was only temporary. I wanted to give them a better life, but days turned into years.")
    print("He paused and looking down at the floor.")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("As time slowly passes, I suddenly realize what i have lost.")
    print("You listen quietly and seriously")
    print("'That's why i come this park every evening...'Marcus continue saying.")
    print("This park reminds me time are still moving, whether we are ready or not.")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("Two of you sit in silence,talking about the life, regret moment, hope, and the people you love and take care about.")
    print("Without realizing, you both welcome the sunset of the day together.")
    print("You stand up with the sunset at your back.")
    print("'It was nice meeting you, I should go now', you says.")
    print("He smiles and says, 'Take care. Don't make the people you love and the people who love you, wait too long.'")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("You walk away, feeling better than before.")
    print("When you suddenly turn back, the bench is empty but the warmth stays in your heart...")
    print("'What a warm person he is ,' you think to yourself.")
    print()
    print(f"{color_green}The End{color_reset}")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("See you tomorrow for more pratices!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#Start for the thirteenth day
print("Day 13...")
print("7Days left")
print("-"*100)
print("Today is the thirteenth day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Mathematics{color_reset}!")
print(f"{color_green}(⚠️ Caution: This subject is crucial part in your SPM exam!){color_reset}")
print("Keep moving forward, never give up!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}WATCH ANIME {color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or WATCH ANIME")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="WATCH ANIME":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or WATCH ANIME.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Nice! Knowledge battle begins!!!",random.choice(emoji_happy))

    questions=[
        "1) Shakir invested RM8000 in Premium Unit Trusts and recieved a dividend of RM 300 at the end of the year. Then, he sold all the shares at a price of RM 8000. Calculate the return on investment (ROI) of Shakir.",
        "2) Jasseem drove at a speed of 110km/h. He decreased his speed to 80km/h in 5 minutes. Calculate the deceleration in km/h per second.",
        f"3) The probability that Lim answered a History quiz question correctly is 4/5. If the quiz has 50 questions, calculate the number of questions that Lim {color_red}did not{color_reset} answer correctly.",
        "4) Lyssa owns a plot of land measuring 7.9m x 34.5m and intends to build a house for her mother. The house was complete in January 2024 and the state government has set a land tax rate in the area of RM 0.60 per square meter. Calculate the amount of land tax that Lyssa has to pay until December 2028.",
        "5) If k is an integer, then the values of k that statisfy both the inequalities k+8>=3 and k+7<6 are"
    ]

    options=[
        ["A. 10.00%","B. 12.50%","C. 13.75%","D. 27.27%"],
        ["A. -6.0","B. -0.1","C. 0.1","D. 6.0"],
        ["A. 40","B. 30","C. 20","D. 10"],
        ["A. 163.53","B. 272.55","C. 654.12","D. 817.65"],
        ["A. -4, -3, -2","B. -5, -4, -3, -2, -1","C. -4, -3, -2, -1","D. -5, -4, -3, -2"],
    ]

    answers=[
        "C","C","D","D","D"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Well played!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Oops! Try again.{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Well done! Your understanding is getting stronger with every question.",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_anime="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⡀⠀⠀⠀⢀⣶⠀⠀⢀⠄⣼⣿⣧⠀⠀⠀⠀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣦⡀⢀⣼⡿⠀⣀⣾⣾⣿⣿⣿⠀⠀⣠⣾⣿⡄⠀⠀⣠⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⡀⠀⣤⣀⠀⠀⣿⣿⣶⠸⣿⣿⣿⣧⣴⡿⠟⡐⣿⣿⡏⠠⢊⣿⣿⡿⠁⣰⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⡀⢹⣿⣿⣦⣿⣿⢿⣷⣬⠙⣿⣿⣿⣶⣶⣶⣿⡿⠠⢀⣾⣿⢁⣶⣸⣿⣿⣤⡤⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⢸⣿⣿⣿⣄⣿⣿⡇⣿⣿⡎⣿⣿⣇⣸⣿⣿⡿⣿⣿⣿⣶⣶⣿⡿⢃⣾⣿⣿⣿⣿⣿⣿⡿⠛⢀⣠⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⣿⣿⣿⣿⢿⣿⣇⠹⣿⣿⣽⣾⣿⣿⣿⣿⡆⣿⣿⣿⣿⣿⡏⣰⣿⣿⡿⢿⣿⣿⣿⣯⣶⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢸⣆⠀⣈⣿⣿⣿⡇⢻⣿⣿⣿⡟⢻⣿⣯⠨⣿⣿⠁⣿⣿⣿⣿⣿⣿⠿⠋⣡⣶⣟⣩⣿⣟⣿⠿⢿⣿⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡈⣿⣷⡿⣿⣯⡙⠿⡌⢻⣿⣿⣷⡌⢿⣿⣬⣿⡿⠀⡿⠋⡹⠟⠋⠁⠀⢠⣿⣿⣿⣿⡍⠟⣭⣼⣶⣼⣿⣿⣿⣶⣶⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⡉⢀⠘⡍⣿⣿⣷⣾⣿⣾⡛⠿⠷⠌⠻⠿⠟⠁⣀⡴⢀⣀⣀⠀⠼⠶⠿⠟⠛⠋⢉⣀⣴⠿⠿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣶⣾⠛⣿⣿⣦⣟⠛⠿⢿⣿⠿⠏⠋⣩⣤⣤⣴⠒⣾⡗⠸⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣷⡄⡈⢃⣠⣶⣿⠿⣿⣿⣿⣔⣊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣧⣄⣉⣽⣿⣿⣿⣦⣈⠁⣠⣿⣿⣿⣿⣿⡟⢰⡿⠇⠀⣿⠙⡆⠹⣿⣿⣿⣿⣿⣿⣿⣷⣦⣈⠻⣿⣿⣇⠜⢿⣿⡙⠿⠿⠶⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢄⡐⣺⣿⣯⣙⡛⠛⠚⣛⣋⣭⠋⣰⣿⣿⣿⣿⣿⣿⠇⠘⠇⢀⣤⡏⠀⣁⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⢸⣿⣜⠘⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⣉⣿⣿⡿⣿⣿⠟⢁⣾⣿⣿⣿⣿⣿⣿⣿⠂⢠⣶⠀⣿⡇⢰⣿⣿⣦⣽⠿⠿⠛⠛⣉⣹⣿⣿⣿⡆⠘⢿⡛⠿⣿⣿⡿⠷⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡀⣀⣀⣀⣤⣴⣾⡿⢉⣤⣶⡿⠋⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⢸⣿⡿⠋⣀⣴⠻⠛⣛⣛⣿⣿⣿⣿⣿⡄⠀⠈⠑⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣿⣿⠟⣿⣿⣿⡟⠉⠄⠀⣸⣿⣿⣿⣯⣥⣶⣶⣶⣤⣄⢉⠛⢿⣿⣿⣿⣿⠀⡶⠋⣠⠶⠚⠛⣉⣉⣉⡉⢿⣿⡆⠀⠀⠈⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⠿⠿⠋⣴⣿⠿⠋⡀⢀⡔⢀⣿⣿⣿⣿⣿⡟⠉⠁⠤⠤⠤⠀⠀⠄⠹⣿⣿⣿⣄⣀⣎⢀⣴⠇⠈⠛⢿⣿⠟⠸⣿⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢴⡾⠛⠁⠀⣨⡷⠋⠀⠈⣿⣿⡿⢉⣥⣶⣶⡿⠛⠻⣦⡐⢷⣤⡦⠙⠿⢿⣿⣿⣿⡘⠛⠆⠀⠠⠿⠋⠐⢰⠉⢉⣿⠀⢀⣴⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠹⠇⠀⠀⠀⢿⣿⡷⢄⠻⣿⣿⣄⠁⡀⠿⢓⣾⠏⠀⠀⣀⣀⠈⠙⠻⠿⠿⢿⣿⣿⣿⠖⠈⠁⠀⢘⣿⠀⡟⢡⠌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⡙⢦⠀⠈⠙⣁⣥⣴⣾⠿⠃⢀⣴⣶⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⣏⣄⢀⡀⠈⡋⡞⠠⡌⢲⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣷⣄⠸⠇⠈⢀⠠⣉⣹⣿⣿⣿⣷⣶⣶⣿⣿⢿⣿⣿⡟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡏⡷⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣀⣤⠙⢷⠄⠀⢠⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⢟⣁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⡇⠃⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⠀⠸⣶⣄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⠿⠿⠿⠿⠏⠙⢿⣿⣿⠁⠘⢁⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣆⡀⠘⠻⣦⠀⢻⣿⣿⣿⣿⣿⣿⣿⠿⠛⣋⣩⣥⣤⣴⠶⠿⠿⠿⠛⠛⢠⣾⣿⡏⠀⡀⠘⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶⣶⡈⠃⠀⢹⣿⣿⡟⠉⣩⡔⠶⠿⠛⠉⠉⠀⠐⠀⢀⣠⠖⣃⣴⣿⣿⣿⠁⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠀⢇⠀⠻⣿⣷⣦⣌⣉⣛⣲⣲⣶⣾⣿⣛⣛⠩⢰⣿⣿⣿⣿⡟⠁⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⢆⠀⠈⠻⣿⣿⣿⣿⣿⣿⣭⣭⣭⣤⣤⣶⣿⡿⠿⠿⠋⠀⡴⠁⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣄⡙⢦⡀⠈⠻⠿⣿⠟⠉⠛⠻⢿⣿⣿⠋⡀⠀⣀⣀⣠⠊⣠⠎⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣦⣌⠒⠤⣀⣀⣤⣤⠈⠂⢹⣿⡿⠐⢃⣼⣿⠟⢁⣼⠋⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣤⣙⠛⠿⣷⣄⣤⣿⣿⣿⣿⠟⢁⣴⠿⠋⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠿⠻⣿⣿⣿⣿⣿⣶⣤⣬⣭⣭⣭⣭⣤⣾⠟⢡⡆⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢡⡄⠆⣿⣿⣿⣿⣿⣏⢻⣿⣿⣿⣿⣿⡟⢁⣶⣿⡇⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⢀⠘⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠋⣰⣿⣿⣿⠇⢰⣿⣿⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⢸⣿⣿⡆⠂⢿⣿⣿⣿⣿⣷⡌⠙⠿⢁⣼⣿⣿⣿⣿⠀⣼⣿⣿⡇⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠿⠇⢸⣿⣿⣷⡀⠸⣿⣿⣿⣿⣿⣿⣇⡀⣾⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣄⠀⣿⣿⣿⣧⠀⢹⡇⢤⣌⠛⢿⣿⣇⢸⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⢻⣿⣿⣿⡄⠸⡇⢸⣿⣿⣦⣄⣁⣼⣿⣿⣿⣿⡏⢸⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⣧⡀⣀⣀⣀⣀⣸⣷⣤⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡞⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⡄⢙⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣾⣿⣿⣿⡇⠹⣿⣿⣿⣿⣿⣿⣧⠛⠛⠛⠛⠛⠻⣿⣿⣿
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣁⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⡆⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⡇⠀⠙⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢿⣿⣿
⣀⣤⣴⣿⣿⣿⠿⠛⣿⣿⠟⠛⠛⠉⠉⠀⣸⣿⣿⣿⣿⠏⠀⠀⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁⣾⣿⣿⣿⣿⡇⡀⣧⣈⠻⠿⠿⠿⠿⠗⠀⢀⣀⣠⣤⠤⠿⣿
⣿⣿⣿⣿⣿⣁⠐⠻⢿⡟⠀⠀⠀⠀⠀⢠⣿⣿⣿⠟⢁⠀⣰⠀⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⢿⣿⣿⣿⣿⣿⡟⣸⣿⠿⠿⠛⠛⣁⣡⣬⣵⣶⣶⣶⣶⣿⣿⣿⡈⠉⠀⠀⠀⠀⢹
⣿⣿⣿⣿⣿⣿⣿⣿⣶⡶⠦⠤⣄⣀⣀⣘⣛⣋⡀⠐⠀⣼⣿⠀⠿⠿⠿⠿⣿⣿⣿⣿⣿⡄⠈⠙⠿⣿⡿⠋⠀⢫⣴⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
"""
    print("You choose to watch anime today~ Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_anime)
    print()
    print("See you tomorrow for more study!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")


#start for the fourteenth day
print("Day 14...")
print("6Days left")
print("-"*100)
print("Today is the fourteenth day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Mathematics{color_reset}!")
print(f"{color_green}(⚠️ Caution: This subject is a crucial part in your SPM exam!){color_reset}")
print("You don’t need to be perfect---you just need to keep going!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to SWIMMING POOL{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or SWIMMING")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="SWIMMING":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or SWIMMING.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Let's begin our study journey for today!!",random.choice(emoji_happy))

    questions=[
        "1) Round off 0.03232 correct to one significant figure.",
        "2) Bernard borrowed RMX from Bank ABC with an interest rate of 8.5% per annum. The repayment period is 5 years. If Bernard pays monthly installment of RM 831.25 per month, how much money does Bernard borrow?",
        "3) Given that the annual value of Dewi's house is RM 14400 and the rate of tassessment tax is 4.8%. Calculate the property accessment tax of Dewi's house for each half year.",
        "4) Round off 396.4 correct to two significant figures.",
        f"5) Which of the following is {color_red}not{color_reset} an investment. "
    ]

    options=[
        ["A. 0.03","B. 0.04","C. 0.030","D. 0.003"],
        ["A. RM 30000","B. RM 32000","C. RM 35000","D. RM 40000"],
        ["A. RM 691.20","B. RM 345.60","C. RM 172.80","D. RM 1382.40"],
        ["A. 40","B. 400","C. 400.0","D. 400.4"],
        ["A. Shares","B. Unit Trust","C. Inheritance","D. Real Estate"],
    ]
        

    answers=[
        "A","C","B","B","C"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Your understanding is getting stronger with every question!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Don't let one mistake affect the next question! You can do it!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Nice!! You're stronger than yesterday!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_swimmingpool="""
                                _   _
                               |\\ |\\
           ____________________|||_|||__________________
          /.--------------------||--||----------------./
         // ~_~^_ ^- ^_^ ^^~_  ^^^ ^^ ~^^^ ~^ ~^ ^^~^//
  ______//____________^   ~   ~^   ~  ^  -  ~^^   ~ //
 /                   /  ^~  ^^  ~^^ ~^ ^.---.  ^~  //
/___________________/    ~ ~  ^^   ~^  | (_) ) ^  //
U   U //   ~-   -  ~  ^   ^~ ^_  ~  ~^ \.___./ ~ //
     //  ^  ~^   ~^  -  ~^^~  -  ~^ ~  ^^ ~  ~  //
jgs // ^ ^~ ^~^ ~_  ~ ~  ~_ ~  ~ ~ ^  ~_ ~_ ^ _//
   /'------------------------------------------/
   `""""""""""""""""""""""""""""""""""""""""""'
"""

    print("You choose to go to swimming pool today. Enjoy your time!",random.choice(kaomoji_happy))
    print(ascii_art_swimmingpool)
    print()
    print("See you tomorrow for next study journey!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#start for the fifteenth day day
print("Day 15...")
print("5Days left")
print("-"*100)
print("Today is the fifteenth day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Mathematics{color_reset}!")
print(f"{color_green}(⚠️ Caution: This subject is a crucial part in your SPM exam!){color_reset}")
print("You’re one step closer to acing SPM!!! Keep going!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}CALL YOUR FAMILY{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or CALL FAMILY")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="CALL FAMILY":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or CALL FAMILY.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Let's leveling up your brain with quiz!!",random.choice(emoji_happy))

    questions=[
       """1) Zainal makes a personal loan of RM 30000 from Bank Cemerlang with an interest rate of 4.5% on the balance. The repayment period is 9 years while the montly instalment is RM 245. 

What is the total amount of interest, in RM, payable by Zainal for the first two months?""",
       """2) Firdaus is a data analyst with a monthly income of RM 7000 and plans to get married in three years. The wedding expenses are estimated to be RM 50000. Therefore, he wants to save RM 1500 a month for a period of three years.

Based on the situation above, which one fulfills the realistic component in SMART concept to achieve his financial goals?""",
       """3) Syazreel has a medical policy with a deductible RM 1000 and a 75/25 co-insurance percentage inhis policy.

Calculate the amount of compensation that can be claimed by Syazreel for medical costs of RM 60000.""",
       """4) Suhaini owns a terrace house in Kangar. The property assessment tax rate is 3%. It is estimated that the house rental is RM 850 per month.

Calculate the property assessment tax payable by Suhaini for each half-year.""",
       "5) It is given that 5(2r-3) = 7r+3. Calculate the value of r.",
    ]

    options=[
       ["A. 112.00","B. 112.50","C. 224.50","D. 224.00"],
       ["A. Wedding expenses is RM 50000","B. Saving period is three years.","C. Save RM 1500 monthly.","D. Monthly saving of RM 1500 from the total income of RM 7000."],
       ["A. RM 14750.00","B. RM 15750.00","C. RM 44250.00","D. RM 45000.00"],
       ["A. RM 25.50","B. RM51.00","C. RM 127.50","D. RM 153.00"],
       ["A. -6","B. -4","C. 4","D. 6"],
    ]

    answers=[
        "C","D","C","D","D"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Every correct answer is proof you’re ready!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Mistakes are proof you’re trying---keep it up!!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Word hard in silence, let success be your noice!!!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_family="""
⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡞⠉⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀
⠀⠀⢸⡇⣀⣀⣠⣤⣤⠶⠖⠀⡇⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀
⠀⠀⣼⠷⠟⢀⠀⠀⠀⡀⠀⠶⣧⠀⠀⢀⡟⠀⠀⣄⡀⠀⠀⠀⠀⠘⣇⠀⠀
⠀⠀⠻⣆⠀⠛⠀⠀⠀⠛⠀⢰⠟⠀⠀⢸⡇⣤⡾⠋⠙⠛⠶⠶⣤⡀⣿⠀⠀
⠀⠀⠀⢻⣄⠀⠻⠶⠟⠀⢠⣿⣤⣀⠀⣸⣧⣶⠀⠗⠀⠀⠰⠇⠈⣷⣿⠀⠀
⠀⠀⠀⠀⢹⡷⢦⣤⡤⢾⣏⣼⣤⠿⠛⠿⣤⣿⡀⠀⢦⣴⠆⠀⢠⡟⢻⠀⠀
⢀⣤⠴⣶⠛⣧⠀⠀⠀⣼⣿⠉⠀⠀⠀⣀⣤⡍⢻⣤⣀⣀⣠⡴⠋⢀⣸⠆⠀
⣿⠀⣄⠙⣦⡈⠛⠒⠛⢡⡟⠒⠛⡛⠋⠉⠀⠀⠸⣇⠀⠀⠘⢿⣟⡉⠁⠀⠀
⣿⠀⠹⡆⠀⠙⠛⠛⠛⠋⠛⣇⠈⢁⠀⢈⠁⢰⣟⠃⠀⠀⠀⢀⡾⠙⠳⣦⠀
⣿⣤⣤⡇⠀⠀⠀⠀⠀⠀⠀⠻⣄⡙⠛⠋⣠⡾⠙⠳⠶⠶⠶⠛⠁⣤⠀⢸⠁
⢸⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⣀⣸⡟⠛⠻⣏⣀⠀⠀⠀⠀⠀⠀⠀⣿⠛⣿⠀
⢸⡇⠀⡇⠀⠀⠀⠀⠀⠀⣾⠉⠻⢦⣤⡴⠞⠉⢻⡄⠀⠀⠀⠀⠀⣿⠀⡟⠀
⠸⠃⠀⠇⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠸⠃⠀⠀⠀⠀⠀⠛⠀⠇⠀
"""
    print(f"{color_green}You choose to to have an short call with your familly today...{color_reset}")
    print()
    input(f"{color_red}Press Enter to continue{color_reset}")
    print("Sedddenly a virtual taskbar appear in front of you...")
    print(f"{color_blue}-{color_reset}"*100)
    print(f"{color_skyblue}Today you choose to call your family in the actual world.{color_reset}")
    print(f"{color_skyblue}But you cannot tell them where you really are!{color_reset}")
    print(f"{color_skyblue}Let's call your family now!{color_reset}")
    print(f"{color_blue}-{color_reset}")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("The virtual taskbar show the delling number of your mother...")
    print(f"{color_yellow}(((☎))){color_reset}")
    print("'Do....Do....Do'")
    print("Rendering in your ears...")
    print()
    print("Maybe it was because you were about to meet your family after a long time, or because you couldn't really tell them what you were going through.")
    print("You felt a slight, unexplained nervousness.")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("After a short wait, you see your parents face.")
    print("Their face looked haggard because they has been searching you since last two weeks...")
    print()
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("After a brief shock, you see your parents start crying.")
    print("In voice close to tears, they  asked where you had been, why you hadn't come home for two weeks, and where you were now.")
    print(f"{color_blue}-{color_reset}"*100)
    print()
    print(f"{color_skyblue}You are given two choice...{color_reset}")
    print(f"{color_skyblue}A. Concealing the truth (System suggest){color_reset}")
    print(f"{color_skyblue}B. Tell the whole truth to your parents{color_reset}")
    print()
    print(f"{color_blue}-{color_reset}"*100)
    print()
    choice=str(input("Please Enter your choice (A/B)")).upper()
    while choice!="A" and choice!="B":
        print("⚠️",f"{color_yellow}Invalid choice! Please enter A/B.{color_reset}")
        choice=str(input("Please Enter your choice (A/B)")).upper()
    
    if choice=="A":
        print("Your heart aches. You really want to tell them the whole truth")
        print("But you can't...")
        print("After struggling, you say you suddenly go to a emergency trip with your friends")
        print("'But I will come back home after one month I promise!', you say to your parents.")
        print()
        input(f"{color_red}Press Enter to continue...{color_red}")
        print()
        print("After a brief silence...")
        print("You can't hold it in anymore.")
        print("Through tears, you say, 'Dad, Mom, I'm so sorry. Please believe me I will come back later. When that time comes, I'll tell you the whole truth. I miss you so much...'")
        print("."*20)
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
        print()
        print("The call ended...")
        print(ascii_art_family)
        print()
        print("See you tomorrow for more pratices.",random.choice(emoji_happy))
        input(f"{color_red}Press Enter to continue...{color_reset}")



#End for today
print(f"{color_pink}~"*125,f"{color_reset}")


#start for the sixteenth day day
print("Day 16...")
print("4Days left")
print("-"*100)
print("Today is the sixteenth day of your SPM exam preparation journey")
print(f"Your main mission for today is to study {color_blue}Mathematics{color_reset}!")
print(f"{color_green}(⚠️ Caution: This subject is a crucial part in your SPM exam!){color_reset}")
print("Every great result begins with practice. You're already winning by starting!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to SCAPE PARK (You used to go with your family){color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or SCAPE PARK")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="SCAPE PARK":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or SCAPE PARK.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! It is time for study now!!!",random.choice(emoji_happy))

    questions=[
        """1) Syarikat Aman Jaya found that the number of ballls sold, J, varies directly as their  advertising cost, H, and inversely as the price of a ball, P. If RM 18000 was spent on advertising and the price of a ball was RM 30, then 3200 balls have been sold.

Calculate the number of balls sold if the total cost of advertising and the price of a ball are increased to RM 48000 and RM 40 respectively.""",
        """2) Which of the following is the correct order of problem solving process through mathematical modeling?

I Verify and interpret solutions
II Make assumptions and identity variables
III Identify and define problem
IV Apply mathematics to solve a problem
""",
        """3) Given the probability of Henry passes in physical and fitness tests are 0.3 and 0.6 respectively.

Calculate the probability that Henry fails both his tests.""",
        """4) Nabil has 7 shirts and 3 of them are blue. Meanwhile 50% of the shirt that Irsyad has are blue. Each of them choose a shirt randomly to attend a dinner event.

Calculate the probability that only one of them wear blue shirt.""",
        f"""5) A network is a graph that formed by a series of dots that connected to each other through line.
Which of the following is {color_red}not{color_reset} a network in our daily situation?""",
    ]

    options=[
        ["A. 1200","B. 1600","C. 3200","D. 6400"],
        ["A. II → III → IV → I","B. II → III → I → IV","C. III → II → I → IV","D. III → II → I → IV"],
        ["A. 0.18","B. 0.28","C. 0.72","D. 0.82"],
        ["A. 3/14","B. 2/7","C. 1/2","D. 13/14"],
        ["A. Arrangement of cars in the parking lot.","B. Roads connecting cities.","C. Food chain.","D. School organizational structure."],
    ]

    answers=[
        "D","D","B","C","A"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Yes! You're leveling up your knowledge!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Don't fear mistakes, they're just stepping stones to success. Try again!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Keep pushing, success is still loading…",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_views=r"""
     .-.                                    ,-.
  .-(   )-.                              ,-(   )-.
 (     __) )-.                        ,-(_      __)
  `-(       __)                      (_    )  __)-'
    `(____)-',                        `-(____)-'
  - -  :   :  - -
      / `-' \
    ,    |   .
         .                         _
                                  >')
               _   /              (\\         (W)
              =') //               = \     -. `|'
               ))////)             = ,-      \(| ,-
              ( (///))           ( |/  _______\|/____
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
            _                 ,----':::::::::::::::::
         {><_'c   _      _.--':MJP:::::::::::::::::::
__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
........................................
"""

    print("You choose to go to the scape park that you used to go with your family today~ Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_views)
    print()
    print("Looking forward for more practices tomorrow~",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#start for the seventeenth day
print("Day 17...")
print("3Days left")
print("-"*100)
print("Today is the seventeenth day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Sciences{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is helpful in your SPM exam!){color_reset}")
print("Keep pushing, success is loading!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to ARCADE (You used to go with your best friend Jason){color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or ARCADE")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="ARCADE":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter ARCADE.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Let's do some science quiz!",random.choice(emoji_happy))

    questions=[
        "1) Which of the following personal protective equipment in the laboratory suitable to carry out experiments that use substances which are volatile and poisonous?",
        f"2) Which of the following statements is {color_red}true{color_reset} about pulse rate?",
        "3)Which of the following statements is true about an object that experience free fall?",
        f"4) Which of the following statements is {color_red}true{color_reset} about nuclear energy?",
        """5) Some students in a hostel suffered from an infections skin disease that caused the skin to become red and scaly.

What is the action should be taken to treat the disease?"""
    ]

    options=[
       ["A. Fume chamber","B. Eyewash station","C. Laminar flow cabinet","D. Safety shower"],
       ["A. Male has higher pulse rate compared to female","B. The older the person, the higher the pulse rate.","C. The more vigorous the physical activity, the higher the pulse rate.","D. At rest, the pulse rate of an athlete is higher than non-athletes."],
       ["A. Have different value of gravitational accelaration","B. Only happens in a vacuum","C. Affected by air resistance.","D. Have same velocity."],
       ["A. Renewable energy source.","B. The usage is limited to generate eletricity","C. Radioactive waste from nuclear energy does not threatened life","D. Alternative energy that can be used to replace petroleum and coal in producing energy"],
       ["A. Intake antibiotic","B. Apply antifungal","C. Use antiviral","D. Treat with antiseptic"],
    ]

    answers=[
        "A","C","B","D","C"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Good Job!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Keep moving forward, every wrong answer sharpens your path to the right one!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Your brain is leveling up with every quiz!!!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_arcade="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣾⣿⣿⣿⣶⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣿⣭⣿⣓⡶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠟⠓⠒⠒⠒⠶⠬⢍⣓⡒⠶⠤⠤⠤⠤⣄⣀⣀⣀⣀⣠⠤⠤⠤⠤⠶⢖⣛⡭⠥⠖⠒⠒⠒⠚⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠟⢁⣠⠤⠶⠶⠦⢤⣄⠀⢤⣈⠉⠙⠛⠛⠓⠒⠒⠲⠲⠶⠖⠒⠒⠛⠛⠛⠉⠉⣀⡤⠀⣀⡤⠴⠶⠶⠤⣄⡈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢃⡴⠋⠀⢠⡶⠤⢦⠀⠈⠳⣆⠈⠳⢄⠀⠀⠀⠀⠀⣠⠴⠦⣄⠀⠀⠀⠀⠀⡠⠚⠁⣴⠛⠁⠀⡴⠒⢶⡀⠀⠙⢦⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢣⡏⠀⣀⠀⣸⣤⢤⣸⡀⢀⡀⠈⣆⠀⠀⠳⡄⠀⠀⣾⠁⠀⠀⠈⡇⠀⠀⣠⠎⠀⠀⡼⠁⠀⠀⠀⠷⣤⠼⠃⠀⠀⠀⢳⡹⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⢸⠀⢸⠋⢹⡏⠀⠀⠘⣏⠉⢻⠀⢸⠀⠀⠀⠙⣦⠀⠹⣄⡀⢀⣰⠏⠀⡴⠋⠀⠀⢰⡇⢰⠛⠛⣦⠀⠀⠀⢰⠞⠙⢧⠈⡇⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⢸⠀⠸⠶⠬⢧⣀⣀⣠⠯⠤⠼⠀⢸⠀⠀⠀⠀⠈⠛⢦⣀⣉⣉⣠⡴⠋⠀⠀⠀⠀⢸⡇⠘⠶⠶⠋⠀⣀⡀⠘⠷⠶⠋⢀⡇⠀⢻⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠈⢧⡀⠀⠀⢸⡈⠉⢸⠀⠀⠀⠀⠈⢷⡀⠀⠀⣴⣖⣲⡄⠀⠀⢠⣶⣤⣄⠀⠀⣠⠞⠁⠀⠀⠀⠀⡏⠉⢹⡆⠀⠀⢀⡾⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠱⢤⣀⠈⠉⠉⠉⠀⠀⠀⢀⣠⣤⣍⡓⢦⡈⠉⠉⠁⠀⠀⠈⠉⠀⣠⠴⢋⣥⣤⣄⡀⠀⠀⠀⠙⠒⠛⠁⣀⡴⠋⠀⠀⠀⠀⡿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡟⢻⠀⠀⠀⠀⠀⠀⠈⠙⠛⠳⣆⠀⠀⡴⠋⠀⠀⠀⠙⣆⠹⡄⠀⠀⠀⠀⠀⠀⣰⠏⡴⠋⠀⠀⠀⠙⣦⠀⠀⣴⠞⠛⠋⠁⠀⠀⠀⠀⠀⠀⡇⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⡇⠀⠀⠀⠀⠀⢸⠀⡧⠀⠀⠀⠀⠀⠀⣿⢸⡇⠀⠀⠀⠀⠀⢸⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⢳⣄⠀⠀⠀⣠⠞⣠⠇⠀⠀⠀⠀⠀⠀⠻⡄⢳⣀⠀⠀⠀⣠⠟⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣍⣛⣒⣛⣡⠜⠁⠀⠀⢀⣀⣀⣀⠀⠀⠙⠦⣍⣓⣒⣋⣥⠖⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⢻⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠃⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⢀⡞⠉⠉⠉⠉⢷⡀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢠⡞⠲⣄⠀⠀⠀⠀⠀⢀⣠⠞⠀⠀⠀⠀⠀⠈⠻⣄⡀⠀⠀⠀⠀⢀⣠⠖⢳⡀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠈⡇⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠈⠙⠒⠒⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠒⠒⠉⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⢸⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠘⢷⣄⢠⡇⠀⠀⠀
⠀⠀⠀⠀⢸⡞⠁⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠈⢻⠇⠀⠀⠀
⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢦⣄⡀⠀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⠀⣀⣠⠾⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀

"""

    print("You choose to go to play arcade today~ Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_arcade)
    print()
    print("See you tomorrow for new study journey!!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#start for the eighteenth day
print("Day 18...")
print("2Days left")
print("-"*100)
print("Today is the eighteenth day of your SPM exam preparation journey")
print(f"Your main mission for today is study {color_blue}Sejarah{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helpful in your SPM exam!){color_reset}")
print("Work hard in silence, let success be your noice!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}play MOBILE LEGENDS{color_reset}",random.choice(emoji_rest),"(This is a game that you often play with your friend Charlie)","today?")
print("STUDY or MOBILE LEGENDS")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="MOBILE LEGENDS":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or MOBILE LEGENDS.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Mission accepted, stay focused!!",random.choice(emoji_happy))

    questions=[
        "1) Which of the following is an example of fast rection?",
        """2) Abu plans to replant maize plant in his farm.
   
Which of the following ways is the best to produce high quality of maize?""",
        """3) Battery is an example of chemical cell.
        

What is the energy change that occur in the battery?""",
        "4) What is the gland that maintains the muscle mass and bone of an adult in the human endocrine system?",
        "5) What are examples of drugs that cause sleepy and less anxious?"
    ]

    options=[
        ["A. Photosynthesis","B. Fruit decay","C. Rusting of iron","D. Explosion of firework"],
        ["A. Use organic fertiliser","B. Use quality breed","C. Plant seedings using modern machines","D. Rear owls ass biological control method"],
        ["A. Chemical energy to heat energy","B. Heat energy to chemical energy","C. Chemical energy to electrical energy","D. Electrical energy to heat energy"],
        ["A. Thyroid gland","B. Adrenal gland","C. Pituitary glannd","D. Pancreatic gland"],
        ["A. LSD and ketamine","B. Barbiturates and alcohol","C. Solvent and gas substance","D. Amphetamine and methamphetamine"],
    ]

    answers=[
        "D","D","C","C","B"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Hit! Correct choice!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Miss! Wrong choice! Try again.{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Discipline today, freedom tomorrow.",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_computer="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣍⣉⠙⠒⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡉⠙⠛⠷⢦⣤⣄⣉⠙⠒⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠡⠀⢂⠈⠉⡙⠻⠷⢶⣤⣄⣈⠙⠒⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⠃⢈⠀⢂⠠⠀⡁⠠⠀⠄⠂⠈⠉⠛⠻⠷⣶⣤⣄⣈⠙⠒⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⡁⢀⠂⠀⠄⠂⠀⠄⢁⠠⠈⠠⠁⡐⠀⠄⡀⠈⠉⠛⠻⠷⣶⣤⣄⣈⠙⠒⠢⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢀⠀⢃⠀⡘⠠⠘⠀⡀⠄⠃⠠⠀⡘⠀⡀⠃⡘⠠⠀⡀⠀⠘⠛⠿⢿⣤⣤⣀⠀⠛⠣⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠄⠂⢀⠂⠀⠄⠐⡀⠁⠠⠐⠈⡀⠐⡀⠐⡀⠐⡀⠄⠡⢀⠡⠈⠄⠠⠀⠄⠉⡙⠛⠷⢶⣤⣄⣈⠉⠒⠢⠤⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠂⡈⠀⠄⠁⡐⠠⠀⠌⢀⠂⢁⠀⢂⠀⡁⢀⠂⠄⠠⠁⠄⠠⠁⠌⠠⢁⠈⡐⠀⠌⡐⠂⢌⠩⢙⠛⠷⣶⡄⢀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠌⢀⠂⠠⠐⠀⢂⠠⠐⠀⡈⠀⠄⠐⡀⠄⠈⠄⠂⡈⠐⢈⠠⠁⣀⠢⠐⡉⠔⡠⠉⢄⢂⠂⠌⠂⣿⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⢈⠠⠀⠄⢁⠠⠁⠠⠀⠂⢁⠠⠈⢀⠂⠠⢀⠁⢂⠐⠀⢡⠀⠢⠡⠄⠢⠡⠌⡐⠄⡉⠄⢊⠐⡈⠁⣿⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡃⠀⠄⠂⢈⠀⠄⠂⠁⠄⠡⠀⠄⡈⠀⠄⡁⢀⠂⠄⠢⠉⠤⢈⠡⢂⠡⠁⠆⠡⠐⡈⠐⡈⠄⡡⢀⠁⣿⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠈⠠⠈⡀⠄⠂⠈⠄⠂⠐⠈⡀⠄⠁⢄⠰⢀⠩⠠⠡⢈⠰⠈⡐⠠⠈⠌⡠⠡⠁⠄⠡⠐⡀⠆⡀⠂⣿⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠆⠀⠡⠐⠀⡐⠈⡀⠂⠌⢀⠁⠠⢂⠉⡀⠢⠈⠄⡁⠢⠈⠄⠡⠠⠡⠈⠔⠠⠁⠌⠠⢁⠡⠐⠠⢀⠁⣾⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⣈⠀⠂⢁⠠⠐⢀⡐⠠⠈⠄⡁⢂⠐⠠⠁⠌⡐⠠⠁⠌⠠⢁⠂⠡⠈⠄⠡⠈⠄⠡⢀⠂⢁⠂⠄⠂⣽⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣿⣶⣦⣤⣆⣠⠀⠑⡈⠰⢀⠂⠌⠠⢁⠂⠄⠡⠈⠄⠡⠀⠌⡀⠡⢈⠀⠡⢈⠠⠀⠂⠄⢂⠐⡀⢿⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢿⣿⣷⣶⣤⣄⣈⠄⠁⢂⠐⡈⠐⡈⠐⠠⢁⠂⠐⡀⠂⠈⠄⡀⠂⠁⠌⠐⠠⠀⠄⣻⡇⢀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⢿⣿⣷⣦⣴⣀⡁⠄⡁⠂⠄⠂⡁⠄⢈⠐⠠⢀⠡⠈⡀⢁⠂⠁⠄⣻⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⡻⣿⣿⣿⣿⢶⣮⣤⣂⡄⢈⠠⠐⢀⠂⢀⠂⠐⠠⢀⠁⠂⣽⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠒⠊⠉⠉⠁⠀⠈⠙⠁⠀⠉⠙⣿⣿⣶⣦⣦⣀⡂⠠⠁⢂⠠⠈⠀⣿⡇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠒⠓⡒⠒⠲⠤⣄⣀⠀⠀⠀⣞⣛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠉⠙⠛⠿⢿⣿⣶⣦⣤⣈⡐⣺⡇⠀⡇
⠀⠀⠀⢀⣀⠤⡴⠒⢛⡉⠀⣀⣠⠦⠲⢋⣀⡤⠆⠁⡈⠉⠑⠲⠿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠁⠉⢻⠛⠿⠿⣿⣇⣰⡧
⣶⣾⠛⠉⢠⡄⢨⣶⢠⣤⠉⣧⣴⠚⠉⢹⣤⣶⠊⠉⣤⣴⠃⠀⢠⠀⠈⠉⡟⢻⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⣾⣿⠀⠀⠀⠀⠀⠈⠀
⠻⠷⣶⣤⣀⡉⠉⠒⠒⠛⣉⣵⠴⠚⢉⣉⡦⠔⢓⣉⡧⠤⢖⢊⣡⠤⠴⡂⣈⡄⠀⣉⠙⠛⠿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣴⣾⣿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠛⠻⠶⣦⣤⣄⡀⠉⠒⠢⠤⣀⡘⠋⠡⠴⣒⣋⡥⠼⡖⢚⣍⡤⠗⠒⣏⣠⠴⠀⢀⡄⠩⠙⠛⠿⢭⣟⡛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⣦⣤⣀⡈⠉⠒⠢⠬⣁⡀⠒⣏⣩⠤⠒⢛⣉⡥⠤⠒⣏⣉⠦⠔⢇⣀⡴⠀⢀⠉⠑⠒⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⣶⣤⣀⣈⠉⠑⠲⠒⢋⣩⠦⠖⣇⣉⠓⠤⢄⣈⣩⠤⠔⠒⣉⣠⣤⣶⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⣶⣤⣄⣀⠁⠋⠋⠤⠕⠒⣉⣠⣦⣶⠾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⠶⠶⠾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    print("You choose to play Mobile Legends today. Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_computer)
    print()
    print("Looking forward for more study tomorrow!!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#start for the nineteenth day
print("Day 19...")
print("1Days left")
print("-"*100)
print("Today is the nineteenth day of your SPM exam preparation journey")
print(f"Your main mission for today is to study {color_blue}Science{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helpful in your SPM exam!){color_reset}")
print("Your effort today builds your success tomorrow!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}ATTENDING CONCERT (This is your favorite KPOP group---BlackPink){color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or ATTEND CONCERT")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="ATTEND CONCERT":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or ATTEND CONCERT.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! It is time to level up your brain!!!",random.choice(emoji_happy))

    questions=[
        """1) The Heimlich Manoeuvre is an emergency procedure that is carried out to save an individual.

What is the victim's situation that requires this method.""",
        "2) Why the pulse rate of an athlete is lower than non-athlete when resting?",
        "3) Which of the following is the normal blood pressure reading?",
        "4) Which of the following is an ecample of discontinuous variation?",
        "5) What is the characteristic of an individual with a healthy mind?" 
    ]

    options=[
       ["A. Holding the neck with both hands","B. Severely injured in an accident","C. Has not heartbeat","D. Hit by lightning strike"],
       ["A. Athlete's heart muscles are less active when resting","B. Athlete's heart muscles are weak when they are not exercising","C. Athlete's heart muscles are weak because of excessive use of steroid","D. Athlete's heart muscles are stronger to pump more blood throughout the body"],
       ["A. 120/80 mmHg","B. 110/90 mmHg","C. 130/80 mmHg","D. 100/70 mmHg"],
       ["A. Height","B. Skin colour","C. Body mass","D. Hair colour"],
       ["A. Emotional","B. Able to reason","C. Negative prejudice","D. Unwilling to accept a challenge"],
    ]

    answers=[
        "A","D","A","D","B"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Awesome job! Keep shining!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}No worries! Mistakes help you grow stronger!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Nice! You're stronger than you think!!!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_concert="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⢀⣀⣀⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⠁⣠⠖⠉⢀⣀⣧⣈⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣷⣄⠀⠀⠀⠀⠀⠀⣠⢾⠛⣿⡁⣠⠞⠉⢀⣯⣀⣈⣇⠀
⠀⠀⠀⠀⠀⢀⣼⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⣀⣘⣏⠛⣷⢤⣀⣀⡤⠞⠁⣸⠟⠀⡷⠃⣠⣶⣟⣏⣀⣀⣘⣆
⠀⠀⠀⠀⠀⣾⡿⠛⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⣠⠖⠉⠉⠉⣏⠙⡿⢾⣄⣀⣀⣠⣼⣽⣠⠞⠀⡰⠃⢨⠟⠋⠀⠀⠀⠉
⠀⠀⠀⠀⢰⣿⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⢠⠞⠁⣠⣴⣾⣿⠏⠉⠓⢾⣦⣀⡀⢻⡿⠟⠁⢀⠞⠁⡴⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡇⠀⢀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣆⠀⡸⢀⠏⢠⠞⠁⣨⠟⠋⠉⠉⠉⢻⡧⢤⣈⣁⣀⣠⠖⠋⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣤⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠛⢳⡇⡸⢠⠏⢠⠞⠁⣠⠔⠊⠉⠉⢻⠗⠦⣄⣀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣀⣀⣤⠀⠀⠀⠀⠀⠀⢸⣀⡞⣷⠇⡜⢠⠏⢀⡞⠁⠀⠀⣰⢞⣻⠇⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⡿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡐⠦⠤⢤⡈⣻⢿⡖⠦⠤⣀⣠⣴⠏⢘⡟⢀⠃⡜⢠⠏⠀⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⣿⡿⠋⠀⢻⡉⠀⠀⠀⠀⠀⠀⠀⠀⠑⠒⠢⠄⢤⣀⣏⠙⢻⠲⠤⢿⣿⣋⠤⠊⢀⣾⣠⠃⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⡟⠀⢀⣴⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠒⠒⠲⠤⣤⡀⣯⣉⠛⠒⠦⠤⣀⣀⣀⡤⠚⢹⣿⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡿⠀⠀⣿⠟⠛⣿⠟⠛⣿⣧⠀⠀⠀⠐⠐⠒⠒⠰⣹⠷⣯⣈⡉⠑⠒⠦⠤⣀⣀⣀⡤⢿⢀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⡀⠀⢿⡀⠀⢻⣤⠖⢻⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠲⠤⢄⣀⣀⣀⣼⠟⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣄⠈⠙⠦⠸⡇⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠛⠶⠤⠶⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⣿⣆⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣿⣿⡿⠃⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣙⠓⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    print("You choose to attending music concert today~ Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_concert)
    print()
    print("See you tomorrow, let's keep practicing!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")

#start for the twentieth day
print("Day 20...")
print("0Days left, tomorrow is the day!!!")
print("-"*100)
print("Today is the tenth day of your SPM exam preparation journey")
print(f"Your main mission for today is to study {color_blue}Science{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helpful in your SPM exam!){color_reset}")
print("Get ready to shine!!! Your journey starts now!!!", random.choice(kaomoji_happy))
print()
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}WATCH YOUR FAVOURITE GAME STREAMER STREAM{color_reset}",random.choice(emoji_rest),"today?")
print("STUDY or STREAM")
choice=str(input("Please enter your choice:")).upper()
#check validity 
while choice!="STUDY" and choice!="STREAM":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or STREAM.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#start loop
if choice=="STUDY":
    print("Great! Let's study now!!",random.choice(emoji_happy))

    questions=[
        "1) Which of the following is alloy?",
        "2) Which of the following is increases the number of free radicals in the human body?",
        """3) A man's body leans to the right when the car he is in turns to the left with high velocity.

What is the science concept that is related to the situation?""",
        "4) What is the process that releases heat energy to heat up gas flowing through the reator core in the nuclear reactor?",
        "5) Which of the following microorganisms is found in the nodules of the root of a legume plant?"
    ]

    options=[
        ["A. Copper","B. Duralumin","C. Alumonium","D. Magnesium"],
        ["A. Misuse of medicine","B. Exposure to cigarette smoke","C. Excessive intake of salt","D. Doing extreme exercise"],
        ["A. Stability","B. Pressure","C. Inerita","D. Force"],
        ["A. Nuclear fusion","B. Nuclear fission","C. Chain reaction","D. Neutralisation reaction"],
        ["A. Nitrogen-fixing bacteria","B. Denitrifying bacteria","C. Nitrifying bacteria","D. Decomposing bacteria"],
    ]

    answers=[
        "B","B","C","B","A"
    ]

    #initial score and question_number
    score=0
    question_number=0
    for question_number in range (len(questions)):
        print("-"*100)
        print()
        print(questions[question_number])
        for option in options[question_number]:
            print(option)
        print()

        answer_input=str(input("Please enter your answer (A/B/C/D): ")).upper()
        while answer_input not in ['A','B','C','D']:
            print("⚠️",f"{color_yellow}Invalid answer! Please enter A, B, C, or D.{color_reset}")
            answer_input=str(input("Please enter your answer(A/B/C/D): ")).upper()
        
        if answer_input==answers[question_number]:
            print()
            print(random.choice(emoji_correct),"Correct Answers!")
            print(f"{color_green}Perfect answer! Future success unlocked!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answers!")
            print(f"{color_yellow}Almost there! Keep pushing forward!!!{color_reset}",random.choice(kaomoji_fighting))
        
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("Nice! It is your time to shine!!!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score,"out of", len(questions), random.choice(emoji_happy))

#for the second choice
else:
    ascii_art_stream="""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
______▒_______________▒▒▒▒▒▒▒▒
_____▒________________▒▒▒▒▒▒▒▒
____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
___▒
__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒
"""

    print("You choose to watch your favorite game streamer stream today! Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_stream)
    print()
    print("Stay calm, stay focused, success is within reach!!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")









