import art
import random

EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5

def check_for_difficulty(difficulty):
    if difficulty == "easy":
        return EASY_DIFFICULTY_ATTEMPTS
    elif difficulty == "hard":
        return HARD_DIFFICULTY_ATTEMPTS
    else: 
        return False

def make_a_guess():
    guess = int(input("Make a guess: "))
    if guess < number_to_guess:
        print("Too low.\nGuess again.")
        return True
    elif guess > number_to_guess:
        print("Too high.\nGuess again.")
        return True
    else: 
        print(f"You've got it. The answer was {number_to_guess}.")
        return False

def play_game():
    if check_for_difficulty(difficulty) == False:
        return print("You've entered wrong difficulty!")
    else:
        attempts = check_for_difficulty(difficulty)
        print(f"You have {attempts} attempts remaining to guess the number.")
        i = 0
        while i < attempts:
            if make_a_guess() == False:
                break
            i += 1
            if i == attempts:
                print("You've run out of guesses, you lose.")
            else:
                print(f"You have {attempts - i} attempts remaining to guess the number.")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(0,100)
print(f"Psst, the current number is {number_to_guess}.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

play_game()

# Udemy solution
""" from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  #checks answer against guess. Returns the number of turns remaining.
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game() """