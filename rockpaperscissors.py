from random import randint
from time import sleep 
                                     #TITLE
print("_"*20,"ROCK PAPER SCISSORS","_"*20,"Developed by alidgrmc")
print("CTRL+C FOR EXIT")
print("Enter '1' for Rock\nEnter '2' for Paper\nEnter '3' for Scissors")

win=lose=draw=0
dictWord={1:"Rock",2:"Paper",3:"Scissors"} 
def take():         #Taking userdecision
    while True:
        try:
            choice=int(input("Your Choice =>"))
            if 1<=choice<=3:
                return choice
                break
            else:
                print("Enter a valid value!")
                sleep(0.75)
        except ValueError:
            print("Enter a valid value!")
            sleep(0.75)
try:      
    while True:        #main function
        userDec=take()
        pcDec=randint(1,3)
        print("(.....)")
        sleep(0.5)
        print("Your choice:{0}".format(dictWord.get(userDec)))
        sleep(0.25)
        print("Computer's choice:{0}".format(dictWord.get(pcDec)))
        if userDec==pcDec:
            sleep(0.25)
            print("Draw :|")
            draw+=1
            print(f"Win={win} Lose={lose} Tie={draw}")
            sleep(0.75)
        elif (userDec==1 and pcDec==3) or (userDec==2 and pcDec==1) or (userDec==3 and pcDec==2):        
            sleep(0.25)
            print("You Win :)")
            win+=1
            print(f"Win={win} Lose={lose} Tie={draw}")
            sleep(0.75)
        else:
            sleep(0.75)
            print("You lose :(")
            lose+=1
            print(f"Win={win} Lose={lose} Tie={draw}")
            sleep(0.75)
except KeyboardInterrupt:
    print("\nThanks for playing...") 
    sleep(1)
