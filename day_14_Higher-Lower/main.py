from art import logo, vs
from game_data import data
from random import choice
# from replit import clear  # works on replit

print(logo)
score = 0
first = choice(data)

while True:
    name_a = first['name']
    desc_a = first['description']
    country_a = first['country']
    count_a = first['follower_count']

    second = choice(data)
    name_b = second['name']
    desc_b = second['description']
    country_b = second['country']
    count_b = second['follower_count']

    print(f"Compare A: {name_a}, a {desc_a}, from {country_a}, {count_a} followers")
    print(vs)
    print(f"Against B: {name_b}, a {desc_b}, from {country_b}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # clear()
    # print(logo)

    if (answer == 'A' and count_a >= count_b) or (answer == 'B' and count_a <= count_b):
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    first = second
