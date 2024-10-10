import random

word_bank = ["coding temple", "lakers", "cheesecake", "peanut butter"]

word = random.choice(word_bank)

name = input("What is your name?\n").title()
print(f"Hello {name}, lets play some Hangman!")

# Player guesses
guesses = ' ' #This keeps track of the letters the player has guessed

turns = 6 #This is how many wrong guesses the player can make

#Creating the game loop
while turns > 0:

    letters_left_to_guess = False # A flag to check if the player has guessed the word or not

    # check the player's progress (Displaying the word to the user)
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            letters_left_to_guess = True

    
    # check if the player has guessed the word
    if not letters_left_to_guess:
        print(f"Congrats, you guessed the word: {word}!")
        break
    
    # user guess character
    guess = input("\nGuess a letter:")

    guesses += guess

    #if the guess is not found in the word
    if guess not in word:
        #decrease turns
        turns -= 1
        #print you lose, if turns is equal to zero
        if turns > 0:
            #print wrong guess message
            print(f"Wrong guess, try again! You have {turns} turns left!")
        else:
            print(f'Your out of turns! You loseee. The chosen word was: "{word}"')