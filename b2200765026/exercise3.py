import random
number = random.randint(0, 100)
while True:
    g = int(input("number"))
    if g < number:
        print("increase your number")
    elif g > number:
        print("decrease your number")
    else:
        print("you found the number")
        break