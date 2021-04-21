from random import choice
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

chosen_word = choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
# print(f'Pssst, the solution is {chosen_word}.')

display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess not in chosen_word:
        print(f'The letter "{guess}" is not in the word')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(chosen_word)
    elif guess in display:
        print(f'The letter "{guess}" is already guessed')
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
          
