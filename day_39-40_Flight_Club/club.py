import os
import requests

print("Welcome to Mike's Flight Club!\nWe find the best deals and email you.")
name = input("What is your first name?\n")
lname = input("What is your last name?\n")
while True:
    email = input("What is your email?\n")
    if email == input("Type your email again.\n"):
        break
    print("Emails don't match.")

if name and lname and email:
    prm = {'user': {'firstName': name,
                    'lastName': lname,
                    'email': email, }}
    headers = {'Authorization': os.environ.get('TOKEN')}
    resp = requests.post(os.environ.get('ENDP'), json=prm, headers=headers)
    print(resp.json())
    print(f"{name} you're in the club!")