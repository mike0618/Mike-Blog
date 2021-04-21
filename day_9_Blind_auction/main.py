# from replit import clear  # !works in replit only!
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the Secret Auction Program.")
bidders = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    new = input("Are there any other bidders? (y/n): ")
    # clear()  # !works in replit only!
    print('\n' * 100)
    if new == '' or new[0].lower() == 'n':
        break

winner = ''
maxbid = 0
for bidder in bidders:
    bid = bidders[bidder]
    if bid > maxbid:
        maxbid = bid
        winner = bidder

print(f"The winner is {winner} with a bid of ${maxbid}.")
