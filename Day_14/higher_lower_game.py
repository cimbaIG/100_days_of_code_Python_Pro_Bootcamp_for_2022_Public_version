import random
import art, game_data
import os

# Lambda function to clear console screen
clear = lambda: os.system("clear")

def read_data():
    randInt1 = random.randint(0,len(game_data.data) - 1)
    randInt2 = random.randint(0,len(game_data.data) - 1)
    data1 = []
    data2 = []
    for key in game_data.data[randInt1]:
        data1.append(game_data.data[randInt1][key])
    for key in game_data.data[randInt2]:
        data2.append(game_data.data[randInt2][key])
    return data1, data2

def check_answer(answer, data1, data2):
    if answer > data2[1]:
        return True
    elif answer > data1[1]:
        return True
    else:
        return False

def play_game(data1, data2):
    print(f"Compare A: {data1[0]}, a {data1[2]}, from {data1[3]}.")
    print(f"Number of followers A: {data1[1]}")
    print(art.vs)
    print(f"Against B: {data2[0]}, a {data2[2]}, from {data2[3]}.")
    print(f"Number of followers B: {data2[1]}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == "A":
        return check_answer(data1[1], data1, data2) 
    elif answer == "B":
        return check_answer(data2[1], data1, data2)
    else:
        print("You've entered a wrong answer!")
        return False

score = 0
i = 0
guess = True
while guess == True:
    clear()
    print(art.logo)
    if guess:
        # At first step (i = 0) data1 and data2 are set randomly.
        if i == 0:
          data1 = read_data()[0]
          data2 = read_data()[1]
          """For every step after the beginning (i > 0), data1 becomes data2 from previous step 
          and data2 is set randomly!"""
        else:
            score += 1
            print(f"That's right! Current score: {score}")
            data1 = data2
            data2 = read_data()[1]
        guess = play_game(data1, data2)
        clear()
    if guess == False:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
    i += 1

# Udemy solution
""" from game_data import data
import random
from art import logo, vs

def get_random_account():
  #Get data from random account
  return random.choice(data)

def format_data(account):
  #Format account into printable format: name, description and country
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  #Checks followers against user's guess 
  #and returns True if they got it right.
  #Or False if they got it wrong.
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
 """
'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B -
Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent
comparison should be between Selena Gomez (the new A) and someone else. The reason is that
everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of
the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be
quite boring. By swapping choice B for A each round, we avoid a situation where the number of
followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''