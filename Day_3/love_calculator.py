print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Make all letters in the strings lowercase
name1_ = name1.lower()
name2_ = name2.lower()
name_ = name1_ + name2_

#Calculate love score
total1 = str(name_.count("t") + name_.count("r") + name_.count("u") + name_.count("e"))
total2 = str(name_.count("l") + name_.count("o") + name_.count("v") + name_.count("e"))
love_score = int(total1 + total2)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")