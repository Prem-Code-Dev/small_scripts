import random

def score(num, per):
    if per:
        try:
            num = int(input("Enter max score: "))
            print("Done!")
            if num > 100:
                print("its too much!")
                score()
            bot(num)
        except ValueError:
            print("please Enter Number Only!")
            score()
    elif per == False:
        bot(num)

def retry(valu):
    print("")
    print("1.Want to [play] again?")
    print("2.Back to [Home]?")
    print("3.[q] to quit")
    attetmps = 0
    while True:
        rtry = input("-->").lower()
        if rtry == 1 or rtry == "yes" or rtry == "play":
            bot(valu)
        elif rtry == 2 or rtry == "home" or rtry == "back":
            manu()
           
        elif rtry == 3 or rtry == "q" or rtry == "quit":
            print("Thanks for playing")
            break
        else:
            attetmps += 1
            print("Please select valid options!")
            if attetmps == 3:
                retry(valu)
                
def bot(value): 
    c_score = value
    print(f"Who get {value} score fisrt he win")
    print("press ENTER to roll dice")
    my_score = 0
    bot_score = 0
    while True:
        input("Your turn:")
        ydice = random.randint(1,6)
        print(f"You got {ydice}")
        my_score += ydice
        print(f"Your score: {my_score}")
        if my_score >= c_score:
            print("------WIN------")
            print("YOU WIN!")
            print("Bot Lose")
            print(f"Total score: You:{my_score} Bot:{bot_score}")
            compare = (my_score - bot_score)
            if compare >= 10:
                print("You: Not Even Close Baby !!")
            elif compare >= 5:
                print("You: Close Baby!")
            elif compare < 5:
                print("You: GG")
            print("----------------")
            retry(value)
            
        input("Bot turn:")
        bdice = random.randint(1,6)
        print(f"Bot got {bdice}")
        bot_score += bdice
        print(f"Bot score: {bot_score}")
        if bot_score >= c_score:
            print("------LOSE------")
            print("BOT WIN!")
            print("You Lose")
            print(f"Total score: You:{my_score} Bot:{bot_score}")
            compare = (bot_score - my_score)
            if compare >= 10:
                print("Bot: Not Even Close !!")
            elif compare >= 5:
                print("Bot: Too Close!")
            elif compare < 5:
                print("Bot: GG")
            print("----------------")
            retry(value)
            

def manu():
    print("")
    print("1.Play with bot [B]")
    print("2.Play with freinds [F]")
    print("3.Change max score [C]")
    play = input("-->").lower()
    if play == "b":
        bot(score(50, False))
    elif play == "c":
        score(50, True)
    elif play == "f" :
        print("Coming Soon")
    else:
        print("Invaild Option!")

print("Welcome to Dice Roll Game")
print("Enter [S] to Start the game")
start = input("-->").lower()
if start == "s":
    manu()