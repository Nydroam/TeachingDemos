#Rock Paper Scissors

#random
import random

#scorekeeping
your_score = 0
ai_score = 0
ties = 0
round_num = 1

#variable to keep the program running
running = True

#intro prompt
print("Rock Paper Scissors! Would you like to try against this super amazing AI?\n")
print("To choose your hand, type:\n")
print("""1 or "Rock" for Rock""")
print("""2 or "Paper" for Paper""")
print("""3 or "Scissor" for Scissors\n""")
print(""""Quit" to quit the game\n\n""")

    
#game loop
while running:
    print("You have won " + str(your_score) + " times\n")
    print("The AI has won " + str(ai_score) + " times\n")
    print("There were " + str(ties) + " ties\n\n")
    print("Round " + str(round_num) + "\n")
    choice = input("Rock, Paper, or Scissors? (Input your choice)\n")
    if (choice.lower() == "quit"):
        print("Goodbye, thanks for playing!")
        break
    ai_num = random.randint(1,4)
    if choice.lower() == "rock":
        your_num = 1
    elif choice.lower() == "paper":
        your_num = 2
    elif choice.lower() == "scissors":
        your_num = 3
    elif choice == "1" or choice == "2" or choice == "3":
        your_num = int(choice)
    else:
        continue
    #chooses winner based on number arguments
    #1 is rock, 2 is paper, 3 is scissors
    if your_num == ai_num:
        print("The ai chose the same. Tie!")
        ties += 1
    if your_num == 1 and ai_num == 3:
        print("The ai chose scissors. You Win!")
        your_score += 1
    if your_num == 1 and ai_num == 2:
        print("The ai chose paper. You Lose!")
        ai_score += 1
    if your_num == 2 and ai_num == 1:
        print("The ai chose rock. You Win!")
        your_score += 1
    if your_num == 2 and ai_num == 3:
        print("The ai chose scissors. You Lose!")
        ai_score += 1
    if your_num == 3 and ai_num == 1:
        print("The ai chose rock. You Lose!")
        ai_score += 1
    if your_num == 3 and ai_num == 2:
        print("The ai chose paper. You Win!")
        your_score += 1
    round_num += 1
    
        
