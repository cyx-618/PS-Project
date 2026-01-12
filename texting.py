#Spm day 
#Day 1 spm bm paper 
import colorama
from colorama import Fore
import random

#------------------------------------------------------------------------------------------------------
#setting all  marks for subjects
bm_marks=0
bi_mars=0
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
bm_opt=["A. murah","B. tinggi","C. mahal","D. rendah",
        "A. cair","B. putih","C. pekat","D. merah",
        "A. rangup","B. lemau","C. rapuh","D. hangit",
        "A. dihentam","B. desebat","C. digasak","D. ditindas",
        "A. ketat","B. besar","C. singkat","D. longgar",
        "A. Kuih","B. Lauk","C. Sayur","D. Barang",
        "A. Gadis","B. Wanita","C. Pemudi","D. Pemuda",
        "A. asyik","B. tekun","C. sering","D. kurang",
        "A. murid","B. pelatih","C. pelajar","D. mahasiswa",
        "A. cair","B. putih","C. pekat","D. merah"
        ]

bm_ans=["A","D","A","B","A","C","D","A","B","D"]
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
#Day 2  bi paper
        
    
    