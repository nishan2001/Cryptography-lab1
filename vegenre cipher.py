alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plain_text, key_text):
    cipher_text = ""
    key_length = len(key_text)    
    for i, letter in enumerate(plain_text):
        position_text = alphabet.index(letter)
        position_key = alphabet.index(key_text[i % key_length])
        new_position = (position_text + position_key) % 26
        new_letter = alphabet[new_position]

        cipher_text += new_letter    
    print(f"The encoded text is {cipher_text}")
def decrypt(cipher_text, key_text):
    plain_text = ""
    key_length = len(key_text)    
    for i, letter in enumerate(cipher_text):
        position_text = alphabet.index(letter)
        position_key = alphabet.index(key_text[i % key_length])
        new_position = (position_text - position_key) % 26
        new_letter = alphabet[new_position]
        plain_text += new_letter    
    print(f"The decoded text is {plain_text}")
def main():
    choice = int(input("Enter 0 for encode and 1 for decode: "))
    if choice == 0:
        input_text = input("Type your text:\n").lower()
        key_text = input("Enter the key:\n").lower()
        encrypt(plain_text=input_text, key_text=key_text)
    elif choice == 1:
        cipher_text = input("Enter the encoded text:\n").lower()
        key_text = input("Enter the key:\n").lower()
        decrypt(cipher_text=cipher_text, key_text=key_text)
    else:
        print("Invalid choice, please enter 0 for encode or 1 for decode.")
if __name__ == "__main__":
    main()