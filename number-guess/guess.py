import random

n = random.randrange(0,20)  # change the range as per your requirements

guess = int(input("Enter Any number between 0 to 20 \n"))


while n!= guess:
    if guess < n:
        print("too less")
        guess = int(input("Enter any number between 0,20  \n"))
    
    elif guess > n:
        print("too high")
        guess = int(input("Enter any number between 0,20  \n"))
    else:
        break
print("Awesome you did it, it was a right guess")


# code by Sadashiv Mirta
