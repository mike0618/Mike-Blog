from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = randint(1, 100)
# print(f"Pssst, the correct answer is {number}")
attempts = 5
if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    attempts += 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("Too HIGH.")
    elif guess < number:
        print("Too LOW.")
    attempts -= 1
    if attempts > 0:
        print("Guess again.")
        
if attempts == 0:
    print("You've run out of guesses, you lose.")
