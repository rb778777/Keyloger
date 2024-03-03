def encrypt(message, key):
    key = key % 26  
    result = ""

    for char in message:
        if char.isalpha():
            
            base = ord('A') if char.isupper() else ord('a')

            
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            result += encrypted_char
        else:
            result += char

    return result

def decrypt(message, key):
    
    return encrypt(message, -key)

def main():
    message = input("Enter your text: ")
    
    while True:
        try:
            choice = int(input("Choose your option:\n1. Encrypt\n2. Decrypt\nEnter (1 or 2): "))
            if choice in [1, 2]:
                break
            else:
                print("Invalid input. Please enter a valid option (1 or 2).")
        except ValueError:
            print("Invalid input. Please enter a valid option (1 or 2).")

    while True:
        try:
            key = int(input("Enter your key (0 to 25): "))
            if 0 <= key <= 25:
                break
            else:
                print("Invalid input. Please enter a valid key (0 to 25).")
        except ValueError:
            print("Invalid input. Please enter a valid key (0 to 25).")

    if choice == 1:
        
        encrypted_message = encrypt(message, key)
        print("\nEncrypted text:", encrypted_message)
    elif choice == 2:
        
        decrypted_message = decrypt(message, key)
        print("Decrypted text:", decrypted_message)

if __name__ == "__main__":
    main()
