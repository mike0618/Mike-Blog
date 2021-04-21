from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lenabc = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    ready_text = ""
    if direction == 'decode':
        shift_amount *= -1
    elif direction != 'encode':
        print("Direction incorrect!")
        return
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position < lenabc:
                ready_text += alphabet[new_position]
            else:
                ready_text += alphabet[new_position - lenabc]
        else:
            ready_text += char
    print(f"The {direction}d text is {ready_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
answer = 'Yes'
while answer != 'n':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % lenabc
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction) 
    answer = input("Would you like to restart? (yes/no): ")[0].lower()
