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
    print("You have been awarded 5 points")
   
    # Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The Answer is Bruce Wayne")
    print ("You have been awarded 0 points")
    # Tells the user that they are INCORRECT LOLLL
else:
    print("INCORECT HAHAH")
    print("The Answer is Bruce Wayne")
    print ("You have been awarded 0 points")

# Ask the user another question
answer = input("What is the name of the creator of this quiz?").upper().lower()
# Congratulates them for getting the correct answer
if answer == "Daequan".upper().lower() :
    print("Correct")
    score+=5
    print("The answer is Daequan")
    print("You have been awarded 5 points")
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was Daequan")
    print ("You have been awarded 0 points")
# Tells the user that they are INCORRECT LOLLL
else: 
    print ("INCORRECT YOU ARE TERRIBLEE!!!")
    print("The answer was Daequan")
    print ("You have been awarded 0 points")
# Ask the user another question
answer = input ("What is the Capital of Australia?").upper().lower()
# Congratulates them for getting the correct answer
if answer == "Canberra".upper().lower() :
    print("Correct")
    score+=5
    print("The answer is Canberra")
    print("You have been awarded 5 points")
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was Canberra")
    print ("You have been awarded 0 points")
# Tells the user that they are INCORRECT LOLLL
else: 
    print ("INCORRECT YOU ARE TERRIBLEE!!!")
    print("The answer was Canberra")
    print ("You have been awarded 0 points")
# Ask the user another question
answer = input ("What type of fish is Nemo in Finding Nemo").upper().lower()
if answer == "Clownfish".upper().lower() :
    print("Correct")
    score+=5
    print("The answer is Clownfish")
    print ("Congratulations {}. You have completed the quiz. You got {}/20 points in the end. Well done" .format(name, score))
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was Clownfish")
    print ("You have been awarded 0 points")
# Tells the user that they are INCORRECT LOLLL
else: 
    print ("INCORRECT YOU ARE TERRIBLEE!!!")
    print("The answer was Clownfish")
    print ("You have been awarded 0 points")
# Ask the user another question
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
    print("The answer is {}".format (c))
    print("You have been awarded 5 points")
# Questions the user (If they left the question blank)
elif answer == "":
    print("Not anwering cuh?")
    print("The answer was {}".format (c))
    print ("You have been awarded 0 points")
elif answer !=a and answer != "a" and answer !=b and answer != "b" and answer !=c and answer != "c" and answer !=d and answer != "d":
    print("That isn't a option")
    print("The answer is {}".format (c))
    print("You have been awarded 5 points")

else:
    print("INCORRECT YOU ARE TERRIBLE")
    print("The answer is {}".format (c))
    print("You have been awarded 0 points")

print("We are halfway and you currently have {} points".format (score))
