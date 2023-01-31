import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names_ = names_string.split(", ")

random_num = random.randint(0,len(names_)-1)
print(f"{names_[random_num]} is going to buy the meal today!")

# Alternative using the random.choice() function
#print(f"{random.choice(names_)} is going to buy the meal today!")