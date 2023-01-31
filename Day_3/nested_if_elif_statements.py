print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 18 and age <= 45:
        print("Please pay $12.")
    elif age > 12 and age < 18:
        print("Please pay $7.")
    elif age > 45 and age <= 55:
        print("You are in a midlife crisis! Free ride for you!")
    else:
        print("Please pay $5.")
else:
    print("Sorry, you have to grow taller before you can ride!")