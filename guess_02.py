import random
name = input("Hey! Waht Should i Call You? :_")
print("now mr/ms.",name,"Let's Get Started With the Game")

words = ["school","animal","planet","summer","travel"
         ,"little","yellow","friend","mother","father"
         ,"winter","garden","jungle","desert","people",
         "bright","circle","silver","castle","forest"]

word = random.choice(words)
guesses = " "
turns = 22
no = 0


while turns > 0:

    fail = 0

    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end=" ")
            fail +=1
            no +=1
    print()
    if fail == 0:

        print("\n🎉🎉 You Won This Time")
        print("the word is :",word)
        break
    print()
    guess = input("Guess A Character :")
    guesses += guess

    if guess not in word:
        turns -=1
        print("You Got It Wrong")
        if turns > 5:
            print("You Still have ", turns," Guessses left ^-^")
        else:
            print("Hey ⚠️  You Only Got ",turns," Guesses Left Careful Now *_*")
        
    if turns == 0:
        print()
        print("Hah! You Lost")
        print("The Word Is :",word)
        exit()
