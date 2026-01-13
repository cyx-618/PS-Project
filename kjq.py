<<<<<<< HEAD
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

#color (ANSI color formatting)(ANSI ascape codes)
color_red="\033[31m"
color_green="\033[32m"
color_yellow="\033[33m"
color_blue="\033[34m"
color_reset="\033[0m"
color_pink="\033[35m"
color_skyblue="\033[36m"
#color end

#taskbar
print("Day 1...")
print("19Days left")
print("-"*100)
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
    #use for loop to ask 5 questions
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
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
#End for the first day

#taskbar for second day
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
#End for the second day

#Third day satart
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
#End for the third day

#start of fourth day
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
#End for the fourth day

#start of fifth day
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
#End for the fifth day
print(f"{color_pink}~"*125,f"{color_reset}")

print("Days 6...")
print("14Days left")
print("-"*100)
print("Today is the sixth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}jungle adventure (Choose this you may have incredible journey){color_reset}","🤩🔥", "today?")
print("STUDY or JUNGLE ADVENTURE")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="JUNGLE ADVENTURE":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or JUNGLE ADVENTURE.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end
#loop for study
if choice=="STUDY":
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
    print("You chose to go for jungle adventure today. Enjoy your time!", random.choice(kaomoji_happy))
    print("😆🎉✨ LET’S GOOOOO!!! 🚀🔥")
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
#End for the sixth day

#start of seventh day
print("Day 7...")
print("13Days left")
print("-"*100)
print("Today is the seventh day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}read story book (Little Prince){color_reset}", random.choice(emoji_rest), "today?")
print("STUDY or READ STORY BOOK")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="READ STORY BOOK":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or READ STORY BOOK.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end
#loop for study
if choice=="STUDY":
    print("📚📖✨ Let's get studying!!! 🚀🔥")
    questions=[
        "1) Take a sandwich with you ________ you get hungry later.",
        "2) Do you think it’s ________ rain tomorrow?",
        "3) I’m busy on Friday, so I ________ come.",
        "4) I was ________ exhausted by the end of the day.",
        "5) Winters here ________ be really cold sometimes, so make sure you bring warm clothes!",
    ]

    options=[
        ["A. if","B. in case","C. when","D. so as not to"],
        ["A. going","B. to","C. will","D. going to"],
        ["A. don't","B. not can","C. am not","D. can't"],
        ["A. incredilble","B. extremely","C. completely","D. very"],
        ["A. might","B. may","C. could","D. can"],
    ]

    answers=[
        "B","D","D","C","D"
    ]

    explainations=[
        "‘In case’ = you do something to be prepared, because you aren’t sure what will happen. In this situation, you don’t know if you will get hungry or not. But you take a sandwich anyway, just to be prepared.",
        "‘Going to’ and ‘will’ can both be used to make predictions, but in this sentence, we already have ‘it’s’, which means we can’t use ‘will’. Otherwise, you could say ‘Do you think it will rain tomorrow?’ with no difference in meaning.",
        "‘I don’t come’ would mean regularly, many times, so it doesn’t fit here, because we’re talking about one time (this Friday). We use ‘can’ + ‘not’ = ‘can’t’/’cannot’ (‘can’t’ is more common in spoken English).",
        "‘Exhausted’ has a strong meaning, so we can only use certain adverbs. In the same way, you can’t say “I was completely tired”, because ‘completely’ can only be used with adjectives which have a strong meaning.",
        "‘Can’ is used here because we are talking about a general possibility. ‘Could’. ‘may’ and ‘might’ are used for specific possibilities, at one moment in time. In addition, ‘could’ refers to general possibility in the past, e.g. “When I was a child, winters here could be really cold sometimes.”",
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
            print(f"{color_green}Great Job!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Don't worry! Success starts with practice!{color_reset}",random.choice(kaomoji_fighting))
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

#choice for reading story book
else:
    print("You chose to read story book today. Enjoy your time!", random.choice(kaomoji_happy))
    print("📚✨ LET’S START READING!!! 🚀🔥")
    ascii_art_book="""
      _.--._  _.--._
,-=.-":;:;:;\':;:;:;"-._
\\\:;:;:;:;:;\:;:;:;:;:;\
 \\\:;:;:;:;:;\:;:;:;:;:;\
  \\\:;:;:;:;:;\:;:;:;:;:;\
   \\\:;:;:;:;:;\:;::;:;:;:\
    \\\;:;::;:;:;\:;:;:;::;:\
     \\\;;:;:_:--:\:_:--:_;:;\
      \\\_.-"      :      "-._\
       \`_..--""--.;.--""--.._=>
        "
    """
    print(ascii_art_book)
    print()
    print("Chapter 1: We are introduced to the narrator, a pilot, and his ideas about grown-ups")
    print()
    print("Once when i was six years old i saw a magnificent picture in a book, called True Stories from Nature,")
    print("about the primeval forest. It was a picture of a boa constictor in the act of swallowing a wild beast.")
    print("Here is a copy of the drawing.")
    input(f"{color_red}Press Enter to see the drawing...{color_reset}")
    print()
    print("In the book it said: 'Boa constrictors swallow their prey whole, without chewing. Afterward they are no")
    print("longer able to move, and they sleep for six months they need for digestion.'")
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("In those days i thought a lot about jungle adventure, and eventuallymanaged to make my first drawing......")
    print()
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
#End for the seventh day

#start of eighth day
print("Day 8...")
print("12Days left")
print("-"*100)
print("Today is the eighth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}go for cycling (Healthy and fun){color_reset}", random.choice(emoji_rest), "today?")
print("STUDY or GO FOR CYCLING")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="GO FOR CYCLING":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or GO FOR CYCLING.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#loop for study
if choice=="STUDY":
    print("📚✨ LET'S START STUDYING!!! 🚀🔥")
    questions=[
        "1) _______ spent time abroad when I was a student, I found it easier to get used to ________ in another country.",
        "2) Let’s go to the cinema." 
        "   Great idea! What film ________ we watch?",
        "3) If I had more time, I ________ do more exercise.",
        "4) For each of the following, choose the sentence in which the subjects and verbs have been correctly identified and in which the subjects and verbs agree. The subjects are in bold and the verbs are underlined."
        "5) For each of the following, choose the sentence in which the subjects and verbs have been correctly identified and in which the subjects and verbs agree. The subjects are in bold and the verbs are underlined."
    ]

    options=[
        ["A. Have...live","B. Having...live","C. Having...living","D. To have...living"],
        ["A. are we going to","B. will","C. shall","D. do"],
        ["A. would","B. will","C. 'm going to","D. want to"],
        ["A. There's three strawberries left","B. There's three strawberry left","C. There are three strawberries left","D. There are three strawberry left."],
        ["A. Some of my goals have yet to be met.","B. Some of my goal have yet to be met.","C. Some of my goals is yet to be met.","D. Some of my goals have yet been met."],
    ]

    answers=[
        "C","C","A","C","A"
    ]

    explainations=[
        "‘Having spent…’ = ‘Because I spent…’ ‘Get used to’ + -ing = ‘adapt to a new situation’",
        "We use ‘shall’ for offers and suggestions when we ask a question. It’s only used in questions with ‘I’ and ‘we’ – not ‘you’, ‘they’ or ‘he’/’she’/’it’.",
        "We use this form to talk about a situation which is imaginary or unreal: ‘if’ + past simple –> ‘would’ + infinitive. In this case, the situation is unreal because I don’t have time, so I can’t do more exercise.",
        "There is/ There's → singular(one item); There are → plural (more than one item)",
        "Goals = plural, so we need the plural verb have. Also, some of needs a plural noun after it."
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
            print(f"{color_green}Excellent, keep it up!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Keep trying! Practice makes perfect!{color_reset}",random.choice(kaomoji_fighting))
        print()
        print(f"{color_skyblue}Explanation:",explainations[question_number],f"{color_reset}")
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("You can do it!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score, "out of", len(questions), random.choice(emoji_happy))

#choice for going cycling
else:
    ascii_art_cycling="""
 o__  
 ,>/_       
(*)`(*).....

    """
    print("You chose to go for cycling today. Enjoy your time!", random.choice(kaomoji_happy)) 
    print(ascii_art_cycling)
    print()
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")

#End for the eighth days

#Start Day 9
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
        "3) Perang Dunia Pertama berlaku pada tahun 1914 hingga 1918." 
        "Apakah faktor yang mencetuskan perang tersebut?"
        "4) Bagaimanakah Perjanjian Persekutuan Tanah Melayu 1948 membela nasib penduduk asal di Tanah Melayu",
        "5) Bagaimanakah Britiah menumpaskan kegiatan Min Yuen?"
    ]

    options=[
        ["A. Menjatuhkan hukuman mati","B. Mengetuai rombongan diplomatik","C. Mengawai keamanan dqalam negeri","D. Melicinkan kutipan cukai di pelabuhan","","Hint: Tingkatan 4 M/s 9"],
        ["A. Membentuk Katipunan","B. Menubuhkan Persatuan Belia Buddha","C. Menerbitkan akhbar Tribune Indige","D. Melancarkan pemberontakan Saya San","","Hint: Tingkatan 4 M/s 29"],
        ["A. Pengeboman Pearl Harbour","B. Perbezaan ideologi antara negara","C. Persengketaan Rusia dengan Britian","D. Pembunuhan pewaris takhta Austria-hungary","","Hint: Tingkatan 4 m/s 54"],
        ["A. Melindungi hak peribumi","B. Memonopoli pentadbiran negara","C. Memansuhkan kerakyatan imigran","D. Membentuk parti politik mengikut kaum","","Hint: Tingkatan 4 m/s 127"],
        ["A. Memeterai perjanjian damai","B. Membuka penempatan baru","C. Melancarkan serangan gerila","D. Menangkap pemimpin radikal","","Hint: Tingkatan 4 m/s 157"],
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
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁
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
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to the MUSIC FESTIVAL?{color_reset}",random.choice(emoji_rest))
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
        "1) Apakah ciri negara berdaulat?"
        ""
        "I Pentadbiran yang sistematik"
        "II Sempadan yang jelas"
        "III Rakyat berbilang kaum"
        "IV Naungan kerajaan lain",
        "2) Mengapakah konsep pengasingan kuasa penting dalam amalan demokrasi berparlimen",
        "3) Kerajaan Persekutuan dan Kerajaan Negeri berusaha untuk membolehkan golongan pertengahan memiliki rumah kediaman."
        ""
        "Bagaimanakah kedua-dua kerajaan mencapai matlamat tersebut?",
        "4) Pada tahun1962, satu referendum telah diadakan di Singapura."
        ""
        "Mengapakah referendum tersebut diadakan?",
        "5) Dasar Kebudayaan Kebangsaan telah digubal pada tahun1971."
        ""
        "Mengapakah dasar tersebut diperkenalkan?",
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
    for queation_number in range (len(questions)):
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
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}go to the FOOD FESTIVAL?{color_reset}",random.choice(emoji_rest))
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
        "2) Dasar pembangunan Nasional (DPN) bermatlamat untuk mencapai perpaduan melalui pengagihan kekayaan negara."
        ""
        "Bagaimanakah hasrat tersebut dapat dicapai?",
        "3) Setelah mencapai kemerdekaan, Mlaysia telah menjadi anggota Pertubuhan Bangsa-Bangsa Bersatu (PBB)."
        ""
        "Mengapakah Malaysia menganggotai pertubuhan tersebut?",
        "4) Malaysia menjadikan ASEAN sebagai platform mengisytiharkan perubahan dasar luar negara pada peringkat serantau dan global."
        ""
        "Bagaimanakah Malaysia merealisasikan komitmen tersebut?",
        "5) Komuniti ASEAN ditubuhkan pada tahun 2015 melalui Deklaras Kuala Lumpur sewaktu Sidang Kemuncak ASEAN ke-27."
        ""
        "Apakah matlamat penubuhan komuniti tersebut?"
        ""
        "I Menjana pertumbuhan ekonomi"
        "II Meningkatkan kemahiran tenaga kerja"
        "III Menetapkan nilai mata wang tunggal"
        "IV Menjamin keselamatan serantau",
    ]

    options=[
        ["A. Membasmi buta huruf","B. Meningkatkan infrastruktur","C. Menyusun semula masyarakat","Menambah jumlah penduduk","",f"{color_skyblue}Hint: Tingkatan 5 m/s 167{color_reset}"],
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
    for queation_number in range (len(questions)):
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
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}WALK AROUND THE PARK? (System suggest)(You may meet a person that help you to cheer up){color_reset}",random.choice(emoji_rest))
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
        "4) Rancangan Integrasi Murid untuk Perpaduan (RIMUP) telah dilaksanakan di peringkat sekolah"
        ""
        "Apakah tujuan dasar tersebut?",
        "5) Apakah strategi yang digunakan dalam melaksanakan Dasar Ekonomi Baru?",
    ]

    options=[
        ["A. Berpengetahuan bahasa inggeris","Mampu berbahasa Melayu","C. Merupakan warganegara","D. Berumur 18 tahun ke atas","",f"{color_skyblue}Hint: Tingkatan 4 m/s 200{color_reset}"],
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
    for queation_number in range (len(questions)):
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
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("Feeling low and sad, you decide to go far a walk in the park today. You hope the fresh air might calm your mind...")
    print("Just then, your phone suddenly light up. A notification pops up, showing a nearby park called 'Sunway park'.")
    print("You don't know why but the sense of loss fills your heart, so you decide to go...")
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("The park is quiet, with only the sound of leaves rustling and birds calling in the diatance.")
    print("You're feeling too sad because you miss your family more tha usual.")
    print("As you walk along the path, you notice that a man dressed entirely in black and sitting alone on a bench.")
    print("You hesitate for a moment, then sit down beside him...")
    print(ascii_art_chair)
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("The man turns to you and ask, 'Why do you look so sad?'")
    print("You take a deep breath and answer him, 'I am trap in this world, I really miss my family.'")
    print("You don't tell the truth...")
    print("He looks deeply into your eyes and says to you, 'My name is Marcus.'")
    print("I left my family many years ago to work in another city. At first, I told myself it was only temporary. I wanted to give them a better life, but days turned into years.")
    print("He paused and looking down at the floor.")
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("As time slowly passes, I suddenly realize what i have lost.")
    print("You listen quietly and seriously")
    print("'That's why i come this park every evening...'Marcus continue saying.")
    print("This park reminds me time are still moving, whether we are ready or not.")
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("Two of you sit in silence,talking about the life, regret moment, hope, and the people you love and take care about.")
    print("Without realizing, you both welcome the sunset of the day together.")
    print("You stand up with the sunset at your back.")
    print("'It was nice meeting you, I should go now', you says.")
    print("He smiles and says, 'Take care. Don't make the people you love and the people who love you, wait too long.'")
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("You walk away, feeling better than before.")
    print("When you suddenly turn back, the bench is empty but the warmth stays in your heart...")
    print("'What a warm person he is ,' you think to yourself.")
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
print(f"Do you want to {color_red}STUDY{color_reset}",random.choice(emoji_study),"or", f"{color_red}WATCH ANIME ?{color_reset}",random.choice(emoji_rest))
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
    for queation_number in range (len(questions)):
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
    print("You choose to go to the music festival today~ Enjoy your time~",random.choice(kaomoji_happy))
    print(ascii_art_music)
    print()
    print("See you tomorrow for more pratices!!",random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
#End for today
print(f"{color_pink}~"*125,f"{color_reset}")









=======
#import random module for emoji, can ask emoji randomly no need to insert emoji one by one
import random
emoji_happy=['😀', '😁', '😆', '😄', '😃', '😊', '😇', '🤗', '😎', '🥳','😀','😁','😆','😄','😃','😊','😇','🤗','😎','🥳', '🤗', '😌', '😏', '😙', '😚', '😛', '😜', '😝', '🤪', '😍', '😆', '😄', '😃', '😁']
emoji_study=['📚','📖','📝','🖊️','🖋️','✏️','📒','📓','📔','📕','📗','📘','📙','📑','🔖','🏷️','🗂️','🗒️','🗓️','📅']
emoji_correct=['✅','✔️','👍','👏','🙌','💪','🌟','🏆','🎉','🥳']
emoji_wrong=['❌','✖️','👎','😞','😔','😕','🙁','☹️','💤','🛌']
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
#taskbar
print("Day 1...")
print("19Days left")
print("-"*100)
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
    #use for loop to ask 5 questions
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
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
#End for the first day

#taskbar for second day
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
#End for the second day

#Third day satart
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
#End for the third day

#start of fourth day
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
#End for the fourth day

#start of fifth day
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
#End for the fifth day
print(f"{color_pink}~"*125,f"{color_reset}")

print("Days 6...")
print("14Days left")
print("-"*100)
print("Today is the sixth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}jungle adventure (Choose this you may have incredible journey){color_reset}","🤩🔥", "today?")
print("STUDY or JUNGLE ADVENTURE")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="JUNGLE ADVENTURE":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or JUNGLE ADVENTURE.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end
#loop for study
if choice=="STUDY":
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
    print("You chose to go for jungle adventure today. Enjoy your time!", random.choice(kaomoji_happy))
    print("😆🎉✨ LET’S GOOOOO!!! 🚀🔥")
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
#End for the sixth day

#start of seventh day
print("Day 7...")
print("13Days left")
print("-"*100)
print("Today is the seventh day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}read story book (Little Prince){color_reset}", random.choice(emoji_rest), "today?")
print("STUDY or READ STORY BOOK")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="READ STORY BOOK":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or READ STORY BOOK.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end
#loop for study
if choice=="STUDY":
    print("📚📖✨ Let's get studying!!! 🚀🔥")
    questions=[
        "1) Take a sandwich with you ________ you get hungry later.",
        "2) Do you think it’s ________ rain tomorrow?",
        "3) I’m busy on Friday, so I ________ come.",
        "4) I was ________ exhausted by the end of the day.",
        "5) Winters here ________ be really cold sometimes, so make sure you bring warm clothes!",
    ]

    options=[
        ["A. if","B. in case","C. when","D. so as not to"],
        ["A. going","B. to","C. will","D. going to"],
        ["A. don't","B. not can","C. am not","D. can't"],
        ["A. incredilble","B. extremely","C. completely","D. very"],
        ["A. might","B. may","C. could","D. can"],
    ]

    answers=[
        "B","D","D","C","D"
    ]

    explainations=[
        "‘In case’ = you do something to be prepared, because you aren’t sure what will happen. In this situation, you don’t know if you will get hungry or not. But you take a sandwich anyway, just to be prepared.",
        "‘Going to’ and ‘will’ can both be used to make predictions, but in this sentence, we already have ‘it’s’, which means we can’t use ‘will’. Otherwise, you could say ‘Do you think it will rain tomorrow?’ with no difference in meaning.",
        "‘I don’t come’ would mean regularly, many times, so it doesn’t fit here, because we’re talking about one time (this Friday). We use ‘can’ + ‘not’ = ‘can’t’/’cannot’ (‘can’t’ is more common in spoken English).",
        "‘Exhausted’ has a strong meaning, so we can only use certain adverbs. In the same way, you can’t say “I was completely tired”, because ‘completely’ can only be used with adjectives which have a strong meaning.",
        "‘Can’ is used here because we are talking about a general possibility. ‘Could’. ‘may’ and ‘might’ are used for specific possibilities, at one moment in time. In addition, ‘could’ refers to general possibility in the past, e.g. “When I was a child, winters here could be really cold sometimes.”",
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
            print(f"{color_green}Great Job!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Don't worry! Success starts with practice!{color_reset}",random.choice(kaomoji_fighting))
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

#choice for reading story book
else:
    print("You chose to read story book today. Enjoy your time!", random.choice(kaomoji_happy))
    print("📚✨ LET’S START READING!!! 🚀🔥")
    ascii_art_book="""
      _.--._  _.--._
,-=.-":;:;:;\':;:;:;"-._
\\\:;:;:;:;:;\:;:;:;:;:;\
 \\\:;:;:;:;:;\:;:;:;:;:;\
  \\\:;:;:;:;:;\:;:;:;:;:;\
   \\\:;:;:;:;:;\:;::;:;:;:\
    \\\;:;::;:;:;\:;:;:;::;:\
     \\\;;:;:_:--:\:_:--:_;:;\
      \\\_.-"      :      "-._\
       \`_..--""--.;.--""--.._=>
        "
    """
    print(ascii_art_book)
    print()
    print("Chapter 1: We are introduced to the narrator, a pilot, and his ideas about grown-ups")
    print()
    print("Once when i was six years old i saw a magnificent picture in a book, called True Stories from Nature,")
    print("about the primeval forest. It was a picture of a boa constictor in the act of swallowing a wild beast.")
    print("Here is a copy of the drawing.")
    input(f"{color_red}Press Enter to see the drawing...{color_reset}")
    print()
    print("In the book it said: 'Boa constrictors swallow their prey whole, without chewing. Afterward they are no")
    print("longer able to move, and they sleep for six months they need for digestion.'")
    input(f"{color_red}Press Enter to continue...{color_reset}")
    print()
    print("In those days i thought a lot about jungle adventure, and eventuallymanaged to make my first drawing......")
    print()
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")
print(f"{color_pink}~"*125,f"{color_reset}")
#End for the seventh day

#start of eighth day
print("Day 8...")
print("12Days left")
print("-"*100)
print("Today is the eighth day of your SPM exam preparation journey.")
print(f"Your main mission for today is study {color_blue}English{color_reset}!")
print(f"{color_green}(⚠️ Remember: This subject is very helful for your SPM success!){color_reset}")
print("Stay possitive and keep moving forward! Don't give up!", random.choice(kaomoji_fighting))
print()
print(f"Do you want to {color_red}STUDY{color_reset}", random.choice(emoji_study), "or", f"{color_red}go for cycling (Healthy and fun){color_reset}", random.choice(emoji_rest), "today?")
print("STUDY or GO FOR CYCLING")
choice=str(input("Please enter your choice:")).upper()
#check validity of input
while choice!="STUDY" and choice!="GO FOR CYCLING":
    print("⚠️",f"{color_yellow}Invalid choice! Please enter STUDY or GO FOR CYCLING.{color_reset}")
    choice=str(input("Please enter your choice:")).upper()
print("-"*100)
#taskbar end

#loop for study
if choice=="STUDY":
    print("📚✨ LET'S START STUDYING!!! 🚀🔥")
    questions=[
        "1) _______ spent time abroad when I was a student, I found it easier to get used to ________ in another country.",
        "2) Let’s go to the cinema." 
        "   Great idea! What film ________ we watch?",
        "3) If I had more time, I ________ do more exercise.",
        "4) For each of the following, choose the sentence in which the subjects and verbs have been correctly identified and in which the subjects and verbs agree. The subjects are in bold and the verbs are underlined."
        "5) For each of the following, choose the sentence in which the subjects and verbs have been correctly identified and in which the subjects and verbs agree. The subjects are in bold and the verbs are underlined."
    ]

    options=[
        ["A. Have...live","B. Having...live","C. Having...living","D. To have...living"],
        ["A. are we going to","B. will","C. shall","D. do"],
        ["A. would","B. will","C. 'm going to","D. want to"],
        ["A. There's three strawberries left","B. There's three strawberry left","C. There are three strawberries left","D. There are three strawberry left."],
        ["A. Some of my goals have yet to be met.","B. Some of my goal have yet to be met.","C. Some of my goals is yet to be met.","D. Some of my goals have yet been met."],
    ]

    answers=[
        "C","C","A","C","A"
    ]

    explainations=[
        "‘Having spent…’ = ‘Because I spent…’ ‘Get used to’ + -ing = ‘adapt to a new situation’",
        "We use ‘shall’ for offers and suggestions when we ask a question. It’s only used in questions with ‘I’ and ‘we’ – not ‘you’, ‘they’ or ‘he’/’she’/’it’.",
        "We use this form to talk about a situation which is imaginary or unreal: ‘if’ + past simple –> ‘would’ + infinitive. In this case, the situation is unreal because I don’t have time, so I can’t do more exercise.",
        "There is/ There's → singular(one item); There are → plural (more than one item)",
        "Goals = plural, so we need the plural verb have. Also, some of needs a plural noun after it."
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
            print(f"{color_green}Excellent, keep it up!!!{color_reset}",random.choice(kaomoji_fighting))
            score=score+1
        else:
            print()
            print(random.choice(emoji_wrong),"Wrong Answer!")
            print(f"{color_yellow}Keep trying! Practice makes perfect!{color_reset}",random.choice(kaomoji_fighting))
        print()
        print(f"{color_skyblue}Explanation:",explainations[question_number],f"{color_reset}")
        print()
        print("Your current score is :", score,"out of",len(questions),random.choice(emoji_happy))
        print()
        print("You can do it!",random.choice(kaomoji_fighting))
        print()
        input(f"{color_red}Press Enter to continue...{color_reset}")
    question_number=question_number+1
    print()
    print(random.choice(emoji_fighting),f"{color_pink}Quiz Ended!!!{color_reset}")
    print("Your final score is:", score, "out of", len(questions), random.choice(emoji_happy))

#choice for going cycling
else:
    ascii_art_cycling="""
 o__  
 ,>/_       
(*)`(*).....

    """
    print("You chose to go for cycling today. Enjoy your time!", random.choice(kaomoji_happy)) 
    print(ascii_art_cycling)
    print()
    print("See you tomorrow for more studying!", random.choice(emoji_happy))
    input(f"{color_red}Press Enter to continue...{color_reset}")

#End for the eighth days
>>>>>>> a41d27ee0869b17a1be4be3ff818b7fcd7a43e63
