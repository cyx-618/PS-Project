#Spm day 
#Day 1 spm bm paper 
import colorama
from colorama import Fore
import random

#------------------------------------------------------------------------------------------------------
#setting all  marks for subjects
bm_marks=0
bi_marks=0
sej_marks=0
mm_marks=0
sc_marks=0
#-------------------------------------------------------------------------------------------------------
bm_q=[
    " Selepas mandi, dia mengenakan __________ pada badannya agar harum.",
    "Kamus dwibahasa edisi baharu yang __________ itu berharga RM45.00 sahaja.",
    " Biskut coklat yang dibeli oleh emak sungguh enak dan ________ .",
    " Budak itu _________oleh ayahnya sebanyak dua kali kerana berbohong.",
    " Semua seluarnya sudah menjadi __________ kerana badannya sudah berisi.",
    " __________ yang dijual di kedai Kak Som itu segar-segar belaka kerana baru dipetik.",
    "__________ itu terlalu kacak jika dibandingkan dengan adik-beradiknya yang lain.",
    "Janganlah __________ bermain, banyak lagi kerja rumah yang perlu kamu selesaikan.",
    "Cikgu Rozita merupakan bekas __________ di Maktab Perguruan Perempuan Melayu, Melaka.",
    "Kaki Pak Senin digigit pacat, darah __________ meleleh di kakinya."

]
bm_opt=["A. kuat","B. kasar","C. tinggi","D. kesat",
        "A. nipis","B. tebal","C. berkilat","D. berwarna",
        "A. rangup","B. lemau","C. rapuh","D. hangit",
        "A. dihentam","B. desebat","C. digasak","D. ditindas",
        "A. ketat","B. besar","C. singkat","D. longgar",
        "A. Kuih","B. Lauk","C. Sayur","D. Barang",
        "A. Gadis","B. Wanita","C. Pemudi","D. Pemuda",
        "A. asyik","B. tekun","C. sering","D. kurang",
        "A. murid","B. pelatih","C. pelajar","D. mahasiswa",
        "A. cair","B. putih","C. pekat","D. merah"
        ]

bm_ans=["D","B","A","B","A","C","D","A","B","D"]
indices=list(range(len(bm_q)))
random.shuffle(indices)


for count,i in enumerate(indices):
    print()
    print("-"*100)
    print(count+1,bm_q[i])
    print()
    print(Fore.GREEN,bm_opt[i*4:(i+1)*4],Fore.RESET)
    print()
    user=input("Your answer: ").upper()
    while user not in ["A","B","C","D"]:
        user=input(f"{Fore.RED}Invalid Answer!Please enter A,B,C or D: {Fore.RESET}").upper()
    if user==bm_ans[i]:
        bm_marks+=2
    
print(f"{Fore.RED}End of BM Paper,See you tommorrow for BI Paper{Fore.RESET}")
#Day 1 end
#----------------------------------------------------------------------------------------------------
#Day 2  bi paper
      
bi_q=[
    " She ________ have short hair, but now it’s long.",
    "How long have they ________ there?",
    " I ________ to Germany last year. ",
    "I drink coffee ________. ",
    "That smells good! What ________.",
    " How did this ________ broken?",
    " Do you think it’s ________ rain tomorrow? ",
    "I’m busy on Friday, so I ________ come.",
    "I was ________ exhausted by the end of the day.",
    "If I had more time, I ________ do more exercise."

]
bi_opt=["A. used to","B. didn't","C. before","D. use to",
        "A. been waited","B. been waiting","C. waiting","D. waited",
        "A. gone","B. went","C. go","D. goes",
        "A. two times for a day","B. two times day","C. twice in day","D. twice a day",
       "A. are you cooking?","B. do you cooking?","C. do you cook?","D. are you cook?" ,
      "A. get","B. become","C. was","D. be",
       "A. going","B. to","C. will","D. going to" ,
      "A. don't","B. not can","C. am not","D. can't"  ,
      "A. incredilble","B. extremely","C. completely","D. very" ,
     "A. would","B. will","C. 'm going to","D. want to"
        ]

bi_ans=["A","B","B","D","A","A","D","D","C","A"]
indices=list(range(len(bi_q)))
random.shuffle(indices)


for count,i in enumerate(indices):
    print()
    print("-"*100)
    print(count+1,bi_q[i])
    print()
    print(Fore.GREEN,bi_opt[i*4:(i+1)*4],Fore.RESET)
    print()
    user=input("Your answer: ").upper()
    while user not in ["A","B","C","D"]:
        user=input(f"{Fore.RED}Invalid Answer!Please enter A,B,C or D: {Fore.RESET}").upper()
    if user==bi_ans[i]:
        bi_marks+=2 
    
print(f"{Fore.RED}End of BI Paper,See you tommorrow for Sejarah Paper{Fore.RESET}")   
#spm day 2 end 
# ---------------------------------------------------------------------------------------------------
# spm day 3 start

sej_q=[
    "Apakah tugas Temenggung dalam Kerajaan Kesultanan Melayu Melaka? ",
    "Bagaimanakah Perjanjian Persekutuan Tanah Melayu 1948 membela nasib penduduk asal di Tanah Melayu",
    "  Bagaimanakah Britiah menumpaskan kegiatan Min Yuen?",
    "Mengapakah konsep pengasingan kuasa penting dalam amalan demokrasi berparlimen?",
    " Bagaimanakah Dasr Ekonomi Baru (DEB) dapat memberi keadilan kepada semua kaum? ",
    "Apakah syarat untuk menjadi pengundi dalam Pilihan Raya Umum Pertama di Tanah Melayu? ",
    " Kedaulatan tradisional merujuk kepada",
    " Apakah strategi yang digunakan dalam melaksanakan Dasar Ekonomi Baru?",
    " Mengapakah Tunku Abdul Rahman dan rombongan kemerdekaan menggunakan kapal laut dari Singapura ke Keranchi pada 1 januari 1956?",
    "Apakah peranan Malayisa dalam Pertubuhan Bangsa-Bangsa Bersatu(PBB)?"
        ]
sej_opt=[
    "A. Menjatuhkan hukuman mati","B. Mengetuai rombongan diplomatik","C. Mengawai keamanan dqalam negeri","D. Melicinkan kutipan cukai di pelabuhan",
    "A. Melindungi hak peribumi","B. Memonopoli pentadbiran negara","C. Memansuhkan kerakyatan imigran","D. Membentuk parti politik mengikut kaum"  ,
    "A. Memeterai perjanjian damai","B. Membuka penempatan baru","C. Melancarkan serangan gerila","D. Menangkap pemimpin radikal"  ,
    "A. Mengelakkan campur tangan luar","B. Meningkatkan mobiliti penduduk","C. Mewujudkan pemerintahan yang adil","D. Mendapat pengiktirafan antarabangsa",
    "A. Membasmi buta huruf","B. Meningkatkan infrastruktur","C. Menyusun semula masyarakat","Menambah jumlah penduduk"  ,
    "A. Berpengetahuan bahasa inggeris","Mampu berbahasa Melayu","C. Merupakan warganegara","D. Berumur 18 tahun ke atas"  ,
    "A. Pematuhan terhadap perundangan","B. Pemerintahan berkuasa mutlak","C. Pengiktirafan peringkat dunia","D. Persamaan rumun bangsa"   ,
     "A. Mewujudkan masyarakat perdagangan","B. Pengenalan perindustrian berat","C. Progrm penanaman semula","D. Menyusun semula masyarakat"   ,
      "A. Menjimatkan kos perjalanan","B. Mengadakan perbincangan","C. Menjelaskan misi rundingan","D. Mendapatkan sokongan luar"  ,
        "A. Mengetahui mesyuarat CHOGM","B. Mengerakkan dasar ZOPFAN","C. Menyertai aktiviti UNESCO","D. Menganggotai Rancangan Colombo"
        ]

sej_ans=[ "C","A","B","C", "C","C","B","D","B","C"]
indices=list(range(len(sej_q)))
random.shuffle(indices)


for count,i in enumerate(indices):
    print()
    print("-"*100)
    print(count+1,sej_q[i])
    print()
    print(Fore.GREEN,sej_opt[i*4:(i+1)*4],Fore.RESET)
    print()
    user=input("Your answer: ").upper()
    while user not in ["A","B","C","D"]:
        user=input(f"{Fore.RED}Invalid Answer!Please enter A,B,C or D: {Fore.RESET}").upper()
    if user==sej_ans[i]:
        sej_marks+=2
    
print(f"{Fore.RED}End of Sejarah Paper,See you tommorrow for MM Paper{Fore.RESET}")
#end of day 3 spm
#--------------------------------------------------------------------------------------------------
#Day 4 Start
mm_q=[
    " Jasseem drove at a speed of 110km/h. He decreased his speed to 80km/h in 5 minutes. Calculate the deceleration in km/h per second.",
    "If k is an integer, then the values of k that statisfy both the inequalities k+8>=3 and k+7<6 are",
    " ",
    " ",
    " ",
    " ",
    "",
    "",
    "",
    ""

]
mm_opt=["A. 10.00%","B. 12.50%","C. 13.75%","D. 27.27%",
        "A. -4, -3, -2","B. -5, -4, -3, -2, -1","C. -4, -3, -2, -1","D. -5, -4, -3, -2",
        ,
       ,
        ,
        ,
        ,
        ,
        ,
        
        ]

mm_ans=["C","D",]
indices=list(range(len(mm_q)))
random.shuffle(indices)


for count,i in enumerate(indices):
    print()
    print("-"*100)
    print(count+1,mm_q[i])
    print()
    print(Fore.GREEN,mm_opt[i*4:(i+1)*4],Fore.RESET)
    print()
    user=input("Your answer: ").upper()
    while user not in ["A","B","C","D"]:
        user=input(f"{Fore.RED}Invalid Answer!Please enter A,B,C or D: {Fore.RESET}").upper()
    if user==mm_ans[i]:
        mm_marks+=2
    
print(f"{Fore.RED}End of BM Paper,See you tommorrow for BI Paper{Fore.RESET}")

  