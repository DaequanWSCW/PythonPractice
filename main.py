score = 0
# Ask the user their name
name = input("What is your name? ")
# Greet the user and introduce the quiz
print("Welcome to this quiz,", name)
print("This quiz is on General Knowledge")
# Ask the user a question
answer = input("What is Batmans Real name?").upper().lower()
# Congratulates them for getting the correct answer
if answer == "Bruce Wayne".upper().lower():
    print("Correct!")
    score +=5
    print("The Answer is Bruce Wayne")
    print ("You score is currently", score)
    # Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The Answer is Bruce Wayne")
    print("Your score is currently at", score)
    # Tells the user that they are INCORRECT LOLLL
else:
    print("INCORECT HAHAH")
    print("The Answer is Bruce Wayne")
    print("Your score is currently", score)

# Ask the user another question
answer = input("What is the name of the creator of this quiz?").upper().lower()
# Congratulates them for getting the correct answer
if answer == "Daequan".upper().lower() :
    print("Correct")
    score+=5
    print("The answer is Daequan")
    print("Your score is currently", score)
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was Daequan")
    print("Your score is currently at", score)
# Tells the user that they are INCORRECT LOLLL
else: 
    print ("INCORRECT YOU ARE TERRIBLEE!!!")
    print("The answer was Daequan")
    print ("Your score is currently", score)
# Ask the user another question
answer = input ("What is the Capital of Australia?").upper().lower()
# Congratulates them for getting the correct answer
if answer == "Canberra".upper().lower() :
    print("Correct")
    score+=5
    print("The answer is Canberra")
    print("Your score is currently", score)
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was Canberra")
    print("Your score is currently at", score)
# Tells the user that they are INCORRECT LOLLL
else: 
    print ("INCORRECT YOU ARE TERRIBLEE!!!")
    print("The answer was Canberra")
    print ("Your score is currently", score)
# Ask the user another question
answer = input ("What is the fish type of the main fish in finding nemo").upper().lower()
if answer == "Clownfish?".upper().lower() :
    print("Correct")
    score+=5
    print("The answer is Clownfish")
    print("Your score is currently", score)
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was Clownfish")
    print("Your score is currently at", score)
# Tells the user that they are INCORRECT LOLLL
else: 
    print ("INCORRECT YOU ARE TERRIBLEE!!!")
    print("The answer was Clownfish")
    print ("Your score is currently", score)




