#Hangman
answer = ""
while len(answer) == 0 or not answer.isalpha():
    answer = input("Type in your secret word to begin!\n")
    if(not answer.isalpha()):
        print("The letters used must be in the English alphabet.")
print ("\n" * 1000)

#formatting the string
answer = answer.upper()
answer = answer.strip()
progress = answer

#setting string length
ans_len = len(answer)

str_displayed = ""
for x in range(0,ans_len):
    str_displayed += "_"

#list of letters that were guessed already
used_letters = []

playing = True

#ascii images to be used in each stage
images = [["________\n","|      |","|      |","|      |","|","|","|","|"],
          ["________\n","|      |","|      |","|      |","|      O","|","|","|"],
          ["________\n","|      |","|      |","|      |","|      O","|      |","|","|"],
          ["________\n","|      |","|      |","|      |","|      O","|     /|","|","|"],
          ["________\n","|      |","|      |","|      |","|      O","|     /|\\","|","|"],
          ["________\n","|      |","|      |","|      |","|      O","|     /|\\","|     /","|"],
          
          ["________\n","|      |","|      |","|      |","|      O","|     /|\\","|     / \\","|"]]

def printGallows():
    index = len(used_letters)
    image = images[index]
    for line in image:
        print(line)
          
while playing:
    print(str_displayed + "\n")
    printGallows()
    print("Guessed Wrong: " + str(len(used_letters)))
    temp = ""
    for letter in used_letters:
        temp += letter + " "
    print(temp)
    guess = ""
    #checking if the guess is a valid letter
    difference = 0
    while len(guess) != 1 or difference < 0 or difference >= 26:
        
        guess = input("Guess a letter!\n")
        difference = ord(guess[0].lower())-ord('a')
        if(len(guess) != 1):
            print("You can only guess one letter at a time!\n")
        if(difference < 0 or difference >= 26):
            print("You must guess a letter from a-z!\n")

    guess = guess.upper()    
    index = progress.find(guess)
    if str_displayed.find(guess)!=-1 or guess in used_letters:
        print("already guessed")
    elif index == -1:
        used_letters.append(guess)
        if(len(used_letters)==6):
            printGallows()
            print("You Lose! The correct word was " + answer)
            break
    else:
        while(progress.find(guess) != -1):
            progress = progress.replace(guess,"*",1)
            if index+1 != len(answer):
                str_displayed = str_displayed[0:index] + guess + str_displayed[index+1:]
            else:
                str_displayed = str_displayed[0:index] + guess
            if(str_displayed.find("_")==-1):
                print(str_displayed + "\n")
                print("You Win! Thanks for playing!")
                playing = False
                break
