#Magic 8 Ball

import random

#responses to yes or no questions
responses = [
    "Yes",
    "No",
    "Obviously not",
    "The answer is 42",
    "OF COURSE WHY WOULD YOU EVEN NEED TO THINK ABOUT IT?",
    "How am I supposed to know?",
    "No....... why...... just no...",
]

print("Welcome to this mysterious magic 8 ball app.")
while True:
    ans = input("What is your question? (yes or no questions only)\n")
    if ans.lower() == "quit":
        print("Goodbye... for now...")
        break
    print (random.choice(responses))
