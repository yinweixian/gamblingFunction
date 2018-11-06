#guess my number game
#gambaling function
#matthew walker
#11/2
def gamble():
    bankAccount = 500
    print("welcome to the gambaling function")
    print("in this menu you can gamble your money")
    print("and if you win the game you win big!!")
    print("right now you have",bankAccount,"in your account")
    gambled = getintinput("how much do you want to bet that you will win?")
    while gambled > bankAccount:
        print("that was more than you have")
        gambled = getintinput("how much do you want to bet that you will win?")
    bankAccount = bankAccount-gambled
    if winner == True:
        if attempt == 5:
            print("you got your money back!")
            bankAccount = bankAccount+gambled
            print("you now have",bankAccount)
        elif attempt == 4:
            print("you got your money plus 1.5x itself!")
            gambled = gambled*1.5
            bankAccount = bankAccount+gambled
            print("you now have",bankAccount)
        elif attempt == 3:
            print("you got your money plus 2x itself!")
            gambled = gambled*2
            bankAccount = bankAccount+gambled
            print("you now have",bankAccount)
        elif attempt == 2:
            print("you got your money plus 5x itself!")
            gambled = gambled*5
            bankAccount = bankAccount+gambled
            print("you now have",bankAccount)
        elif attempt == 1:
            print("no way! how you do that? you multiplied your bet by 10!!!")
            gambled = gambled*10
            bankAccount = bankAccount+gambled
            print("you now have",bankAccount)
        else:
            print("you done messed up")
    else:
        ("you lost all your money!")
def getintinput(question):
    z = True
    while z == True:
        x = input(question)
        if x.isdigit():
            x = int(x)
            z = False
            return x
        else:
            print("that wasnt a digit")
        
    
gamble()
