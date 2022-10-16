#First we import random and sys
import sys
import random

ans = True
Answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it",
           " As I see it, yes", "Most likely", "Outlook good", "Yes", " Signs point to yes", "Reply hazy, try again",
           "Ask again later", "Ask again later", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
           "My reply is no", "My sources say no", "Outlook not so good", " Very doubtful"]

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")



    if question == "":
        sys.exit()
    else:
        Answer = random.choice(Answers)