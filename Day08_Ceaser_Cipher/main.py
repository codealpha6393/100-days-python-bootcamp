from fig import logo
print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Continue = True

while Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    
    
 
    def caesar(text, shift, direction):
        transformed_text = ""
        if shift > 26:
            shift = shift % 26
        if direction == 'encode':
            for letter in text:
                if letter in alphabet:
                    index = alphabet.index(letter)
                    if index + shift > 25:
                        transformed_text += alphabet[index + shift - 26]
                    else:
                        transformed_text += alphabet[index + shift]
                else:
                    transformed_text += letter
    
        if direction == 'decode':
            for letter in text:
                if letter in alphabet:
                    index = alphabet.index(letter)
                    if index-shift < 0:
                        transformed_text += alphabet[index - shift + 26]
                    else:
                        transformed_text += alphabet[index-shift]
                else:
                    transformed_text += letter
        print(f"{direction}d text is: {transformed_text}")
        
    caesar(text, shift, direction)

    game_status = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if game_status == 'no':
        Continue = False
        print("Goodbye")
    elif game_status == 'yes':
        Continue = True
    else:
        print("Invalid input")
        Continue = False

