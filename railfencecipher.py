def encrypt_rail_fence(text, depth):
    # Remove spaces from the plaintext
    text = text.replace(" ", "")
    
    rail = [''] * depth
    direction = 1
    row = 0
    
    for char in text:
        rail[row] += char
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1
            
    return ''.join(rail)

def decrypt_rail_fence(ciphertext, depth):
    rail = [['' for _ in range(len(ciphertext))] for _ in range(depth)]
    direction = 1
    row = 0
    index = 0

    for i in range(len(ciphertext)):
        rail[row][i] = '*'
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1
    
    for i in range(depth):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*':
                rail[i][j] = ciphertext[index]
                index += 1
                
    result = ''
    row = 0
    direction = 1
    for i in range(len(ciphertext)):
        result += rail[row][i]
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1
    
    # Add spaces back to the decrypted text
    decrypted_text = ''
    space_index = 0
    for char in ciphertext:
        if char == ' ':
            decrypted_text += ' '
        else:
            decrypted_text += result[space_index]
            space_index += 1
            
    return decrypted_text

# Get input from user
plaintext = input("Enter the plaintext: ")
depth = int(input("Enter the depth: "))

# Encrypt the plaintext
encrypted_text = encrypt_rail_fence(plaintext, depth)
print("Encrypted:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt_rail_fence(encrypted_text, depth)
print("Decrypted:", decrypted_text)
