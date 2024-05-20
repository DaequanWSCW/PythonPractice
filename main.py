score = 0
play = "yes"
# Ask the user their name
name = input("What is your name? ")

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

        

    question_attempts= tries
    while question_attempts > 0:
        score= 0
        answer = input("What is Batmans Real name?").upper().lower()
        # Congratulates them for getting the correct answer
        if answer == "Bruce Wayne" .upper().lower():
            print("Correct!")
            score +=5
            print("You have been awarded 5 points")
            break
            # Questions the user (If they left the question blank)
        elif answer == "":
            print("Not anwering cuh?")
            print ("You have been awarded 0 points")
            # Tells the user that they are INCORRECT LOLLL
        else:
            print("INCORECT HAHAH")
        
            print ("You have been awarded 0 points")

            question_attempts -=1
    print("The Answer is Bruce Wayne")

   

    question_attempts= tries
    while question_attempts > 0:
        answer = input("What is the name of the creator of this quiz?").upper().lower()
        # Congratulates them for getting the correct answer
        if answer == "Daequan".upper().lower() :
            print("Correct")
            score+=5
            print("You have been awarded 5 points")
            break
        # Questions the user (If they left the question blank)
        elif answer == "":
            print("Not anwering cuh?")
            print ("You have been awarded 0 points")
        # Tells the user that they are INCORRECT LOLLL
        else: 
            print ("INCORRECT YOU ARE TERRIBLEE!!!")
            
            print ("You have been awarded 0 points")
            question_attempts -=1
    print("The answer was Daequan")


    question_attempts= tries
    while question_attempts > 0:
        answer = input ("What is the Capital of Australia?").upper().lower()
        # Congratulates them for getting the correct answer
        if answer == "Canberra".upper().lower() :
            print("Correct")
            score+=5
            print("You have been awarded 5 points")
            break
        # Questions the user (If they left the question blank)
        elif answer == "":
            print("Not anwering cuh?")
            print ("You have been awarded 0 points")
        # Tells the user that they are INCORRECT LOLLL
        else: 
            print ("INCORRECT YOU ARE TERRIBLEE!!!")
            print ("You have been awarded 0 points")
            question_attempts -=1
    print("The answer is Canberra")


    question_attempts= tries
    while question_attempts > 0:
        question = "How many stripes are in the USA Flag?"
        a = "8"
        b = "16"
        c = "13"
        d = "10"
        # Tells user they are correct
        answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).upper().lower()
        if answer == c or answer == "c" :
            print("Correct")
            score+=5
            print("You have been awarded 5 points")
            break
        elif answer == "":
            print("Not anwering cuh?")
            print ("You have been awarded 0 points")
        elif answer !=a and answer != "a" and answer !=b and answer != "b" and answer !=c and answer != "c" and answer !=d and answer != "d":
            print("That isn't a option")
            print("You have been awarded 5 points")
        else:
            print("INCORRECT YOU ARE TERRIBLE")
            print("You have been awarded 0 points")
            question_attempts -=1
    print("The answer is {}".format (c))
    
    input("We are halfway and you currently have {} points press enter when ready".format (score))




    # Tells the user the next question
    question = "What is the biggest city by Land??"
    a = "Tokyo"
    b = "Los Angeles"
    c = "New York"
    d = "Auckland"
    # Tell user they are correct
    answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).upper().lower()
    if answer == c or answer == "c" :
        print("Correct")
        score+=5
        print("The answer is {}".format (c))
        print("You have been awarded 5 points")
        # Questions the user
    elif answer == "":
        print("Not anwering cuh?")
        print("The answer was {}".format (c))
        print ("You have been awarded 0 points")
    elif answer !=a and answer != "a" and answer !=b and answer != "b" and answer !=c and answer != "c" and answer !=d and answer != "d":
        print("That isn't a option")
        print("The answer is {}".format (c))
        print("You have been awarded 5 points")
    # Tells the user they are wrong
    else:
        print("INCORRECT YOU ARE TERRIBLE")
        print("The answer is {}".format (c))
        print("You have been awarded 0 points")


    # Tells the user the next question
    question = "What is the biggest city by POPULATION??"
    a = "Tokyo"
    b = "Shanghai"
    c = "New York"
    d = "Wellington"
    # Tell user they are correct
    answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).upper().lower()
    if answer == a or answer == "a" :
        print("Correct")
        score+=5
        print("The answer is {}".format (a))
        print("You have been awarded 5 points")
        # Questions the user
    elif answer == "":
        print("Not anwering cuh?")
        print("The answer was {}".format (a))
        print ("You have been awarded 0 points")
    elif answer !=a and answer != "a" and answer !=b and answer != "b" and answer !=c and answer != "c" and answer !=d and answer != "d":
        print("That isn't a option")
        print("The answer is {}".format (a))
        print("You have been awarded 5 points")
    # Tells the user they are wrong
    else:
        print("INCORRECT YOU ARE TERRIBLE")
        print("The answer is {}".format (a))
        print("You have been awarded 0 points")

        
    #Tells the user it is the end of the quiz
    print("You have completed the quiz!")
    print("Congratulations, {}".format (name))
    print("You have gotten a score of {} out of 30".format (score))

    play = input("Do you want to try this quiz again?").lower()