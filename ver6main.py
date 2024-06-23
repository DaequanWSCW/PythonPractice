guesses = []
BIGGEST_CITIES_ANSWERS = ["tokyo", "delhi", "shanghai", "dhaka", "sao paulo", "cairo", "mexico city", "beijing", "mumbai", "osaka"]

# ------ FUNCTIONS ------

# Welcomes user and introduces the quiz
def intro():
    # Ask the user their name
    name= input("What's your name?")

    # Greet the user and introduce the quiz
    print("Welcome to this quiz,", name)
    print("This quiz is on the Top 10 Biggest cities in the world")

# Asks user for lives and confirms is valid
def getLives():
    while True:
        lives = input("How many chances do you want?")
        try:
            # Checking if valid number
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

# Checks if answer already exists in list. Used for checking both correct answers, and previous guesses
def inlist(answer, list):
    if answer in list:
        return True
    else:
        return False

# ------- MAIN CODE -------

intro()
lives = getLives()
score = 0

# Begin quiz
while lives > 0:
    answer = input("Name one of the top 10 Largest cities in the world:\n").lower()

    # Checks if correct or incorrect
    if inlist(answer, BIGGEST_CITIES_ANSWERS):
        # Checks if already guessed or not
        if inlist(answer, guesses):
            print("You've guessed that already")
        else:
            print("Correct")
            score +=5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses), score, lives))
    else:
        print("Wrong!")
        lives -= 1
        print(" You have guessed {} Your score is {}. You have {} chances remaining".format(len(guesses), score, lives))

    if score == 50:
        print("Congrats, you have correctly guessed all the answers. You are indeed, skibidi.")
        break

# End the game
print("Game Over. Your final score was {}".format (score))  