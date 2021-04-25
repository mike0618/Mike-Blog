from art import logo, vs
from game_data import data
from random import choice
# from replit import clear  # works on replit

def format_data(instance):
    name = instance['name']
    descr = instance['description']
    country = instance['country']
    return f"{name}, a {descr}, from {country}"

print(logo)
score = 0
first = choice(data)

while True:
    count_a = first['follower_count']

    second = choice(data)
    while second == first:
        second = choice(data)
    count_b = second['follower_count']

    print("Compare A: " + format_data(first) + f", {count_a}M followers")
    print(vs)
    print(f"Against B: " + format_data(second))

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
