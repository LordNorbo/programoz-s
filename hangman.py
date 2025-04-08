#hangman
hangman=(
    ("________"),
    ("|       |"),
    ("|       o"),
    ("|      /|\\"),
    ("|      /\\"),
    ("|"),
    ("___________")
)
word=input("Adj meg eg szót!").lower
guesses=""
turns=6
print("Welcome to hangman!")
print(hangman[0])

while turns>0:
    guess=input("Guess a letter: ")
    if guess in word:
        guesses+=guess
        print("Good job,"+ guess + " is in the word!")
        print(hangman[0])
        for letter in word:
            if letter in guesses:
                print(letter,end="")
            else:
                print("_",end="")
        print()
    else:
        turns-=1
        print("Sorry, " + guess + "is not in the word. You have " +str(turns)+ "turns left!")
        print(hangman[6-turns])
    if all(letter in guesses for letter in word):
        print("Congratulations, you guessed the word!")
        break
if turns == 0:
    print("Game over, the word was" + word)






