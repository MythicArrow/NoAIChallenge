# Day 1 no ai
import random
#n = int(input())
#x = int(input())
def RandGame(n, x):
    num = random.randint(n,x)
    attempts = 0
    while True:
        attempts += 1
        guess = int(input(f"Guess a number between {n} and {x}: "))
        if guess == num:
            print("Well guessed!")
            print(attempts)
            break
        elif guess < num:
            print("Try Higher")
        elif guess > num:
            print("Try Lower")
Game(9,20)
