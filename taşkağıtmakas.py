from random import randint
from time import sleep 
                                     #TITLE
print("_"*20,"TAŞ KAĞIT MAKAS V2.0","_"*20,"Developed by Ali DOĞRAMACI")
print("ÇIKMAK İÇİN CTRL+C")
print("TAŞ İÇİN 1\nKAĞIT İÇİN 2\nMAKAS İÇİN 3")

win=lose=draw=0
dictWord={1:"TAŞ",2:"KAĞIT",3:"MAKAS"} 
def take():         #Taking userdecision
    while True:
        try:
            q=int(input("Seçiniz =>"))
            if 1<=q<=3:
                return q 
                break
            else:
                print("Geçerli Bir değer giriniz!")
                sleep(0.75)
        except ValueError:
            print("Geçerli Bir değer giriniz!")
            sleep(0.75)
try:      
    while True:        #main function
        userDec=take()
        pcDec=randint(1,3)
        print("(.....)")
        sleep(0.5)
        print("Sizin seçiminiz:{0}".format(dictWord.get(userDec)))
        sleep(0.25)
        print("Bilgisayarın seçimi:{0}".format(dictWord.get(pcDec)))
        if userDec==pcDec:
            sleep(0.25)
            print("BERABERE :|")
            draw+=1
            print(f"Galibiyet={win} Mağlubiyet={lose} Beraberlik={draw}")
            sleep(0.75)
        elif (userDec==1 and pcDec==3) or (userDec==2 and pcDec==1) or (userDec==3 and pcDec==2):        
            sleep(0.25)
            print("KAZANDIN :)")
            win+=1
            print(f"Galibiyet={win} Mağlubiyet={lose} Beraberlik={draw}")
            sleep(0.75)
        else:
            sleep(0.75)
            print("KAYBETTİN :(")
            lose+=1
            print(f"Galibiyet={win} Mağlubiyet={lose} Beraberlik={draw}")
            sleep(0.75)
except KeyboardInterrupt:
    print("\nOyundan çıkılıyor...") 
    sleep(1)
