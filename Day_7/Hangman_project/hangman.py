import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
lives = len(hangman_art.stages) - 1

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

""" checkIfEmpty = False
while not checkIfEmpty:
    guess = input("Guess a letter: ").lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)
    checkIfEmpty = True
    for letter in display:
        if letter == "_":
            checkIfEmpty = False
 """
end_of_game = False
guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print(f"You've already guessed {guess}.")
    else:
        # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        if guess not in display:
            lives -= 1
            print(f"You've guessed {guess}. That's not in the word. You lose life.\nYou've got {lives} lives remained.")
            if lives == 0:
                end_of_game = True
                print("You lose.")
        print(hangman_art.stages[lives])
        print(f"{' '.join(display)}")
        #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
        if "_" not in display:
            end_of_game = True
            print("You win.")    
    guesses.append(guess)