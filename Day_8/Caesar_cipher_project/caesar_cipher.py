import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift, direction):
    if direction == "encode":
        encrypted_text = ""
        for i in range(len(text)):
            if text[i] not in alphabet:
                encrypted_text += text[i]
            else:
                if (alphabet.index(text[i]) + shift) > (len(alphabet) - 1):
                    encrypted_text += alphabet[alphabet.index(text[i]) + shift - len(alphabet)]
                else:
                    encrypted_text += alphabet[alphabet.index(text[i]) + shift]
        print(f"The encoded text is '{encrypted_text}'.")
    elif direction == "decode":
        decrypted_text = ""
        for i in range(len(text)):
            if text[i] not in alphabet:
                decrypted_text += text[i]
            else:
                if (alphabet.index(text[i]) - shift) < 0:
                    decrypted_text += alphabet[len(alphabet) + alphabet.index(text[i]) - shift]
                else:
                    decrypted_text += alphabet[alphabet.index(text[i]) - shift]
        print(f"The decrypted text is '{decrypted_text}'.")
    else:
        print(f"You should pick 'encode' or 'decode', not a '{direction}'.")

end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart_ = input("Do you want to restart the cipher program? ").lower()
    if restart_ == "no":
        end_program = True
    elif restart_ == "yes":
        end_program == True
    else:
        print("You've entered a wrong value!")
        break

# Solution with two functions
""" def encrypt(text, shift):
    encrypted_text = ""
    for i in range(len(text)):
        if (alphabet.index(text[i]) + shift) > (len(alphabet) - 1):
            encrypted_text += alphabet[alphabet.index(text[i]) + shift - len(alphabet)]
        else:
            encrypted_text += alphabet[alphabet.index(text[i]) + shift]
    print(f"The encoded text is '{encrypted_text}'.")

def decrypt(text, shift):
    decrypted_text = ""
    for i in range(len(text)):
        if (alphabet.index(text[i]) - shift) < 0:
            decrypted_text += alphabet[len(alphabet) + alphabet.index(text[i]) - shift]
        else:
            decrypted_text += alphabet[alphabet.index(text[i]) - shift]
    print(f"The decrypted text is '{decrypted_text}'.")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print(f"You should pick 'encode' or 'decode', not a '{direction}'.") """

#Their solution
""" alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye") """