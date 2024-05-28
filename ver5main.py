import random

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Not bad!", "Good job skibidi","The City needs you Batman"]
BAD_COMMENTS = ["You suck", "Why are you still here? Quit already.", "Get out of my quiz, you are terrible"]
QUESTIONS = ["What is Batmans real name?",
             "Who is the creator of this quiz?",
             "What is the capital of Australia?"]
OPTIONS =[["Peter Parker", "Medhansh Anthwal", "Bruce Wayne", "Tony Stank"],
          ["Daequan Su", "Medhansh Anthwal", "Floyd Morgan", "Oscar White"],
          ["Sydney", "Melbourne", "Perth", "Canberra"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [2,0,3]


score = 0
play = "yes"
# Ask the user their name

name = input("What is your name? ")
if name == "Daequan":
    print("I LOVE YOU MY ALMIGHTY SIGMA LORD YOU ARE SO SKIBIDY")
    print("You have been awarded 100000 points!")


# Greet the user and introduce the quiz
print("Welcome to this quiz,", name)
print("This quiz is on General Knowledge")

#Check Number of attempts
while True:
    try:
        tries = input("How many attempts do you want for each question  1-3")
        tries = int(tries)
        break
    except:
        print("That's not a number")

while play == "yes":
    score = 0
        
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
        
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                 OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("Correct, you have been awarded 5 points")
                score+=5
                print(random.choice(GOOD_COMMENTS))
                break
            elif answer == "":
                print("Not anwering cuh?")
                print ("You have been awarded 0 points")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Incorrect!")
                print(random.choice(BAD_COMMENTS))
            else:
                print("That wasn't an option")
                print("You have been awarded 0 points")

            question_attempts -= 1
    
    #Tells the user it is the end of the quiz
    print("You have completed the quiz!")
    print("Congratulations, {}".format (name))
    print("You have gotten a score of {} out of 15".format (score))

    # Replay Quiz
    play = input("Do you want to try this quiz again?").lower()