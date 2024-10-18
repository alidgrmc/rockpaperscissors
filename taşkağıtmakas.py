import random,time
print("_"*20,"TAŞ KAĞIT MAKAS V2.0","_"*20,"Developed by Ali DOĞRAMACI")
print("ÇIKMAK İÇİN CTRL+C")
print("TAŞ İÇİN 1\nKAĞIT İÇİN 2\nMAKAS İÇİN 3")
sozluk={1:"TAŞ",2:"KAĞIT",3:"MAKAS"}
def al():
    while True:
        try:
            q=int(input("Kararınızı giriniz:"))
            if 1<=q<=3:
                return q 
                break
            else:
                print("Geçerli Bir değer giriniz!")
                time.sleep(0.75)
        except ValueError:
            print("Geçerli Bir değer giriniz!")
            time.sleep(0.75)
            continue
try:
    while True:
        userDec=al()
        pcDec=random.randint(1,3)
        print("(...)")
        time.sleep(1)
        print("Sizin kararınız:{0}".format(sozluk.get(userDec)))
        time.sleep(0.25)
        print("Bilgisayarın kararı:{0}".format(sozluk.get(pcDec)))
        if userDec==pcDec:
            time.sleep(0.25)
            print("BERABERE!")
            time.sleep(0.75)
        elif (userDec==1 and pcDec==3) or (userDec==2 and pcDec==1) or (userDec==3 and pcDec==2):#kazanma koşulları
            time.sleep(0.25)
            print("KAZANDIN!")
            time.sleep(0.75)
        else:
            time.sleep(0.75)
            print("KAYBETTİN")
            time.sleep(0.75)
except KeyboardInterrupt:
    print("\nOyundan çıkılıyor...") 
    time.sleep(1)