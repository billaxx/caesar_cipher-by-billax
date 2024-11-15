# Caesar Cipher Program
# Author: Mohamed Thaslim

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    :param text: Input text (string)
    :param shift: Shift value (integer)
    :param mode: 'encrypt' or 'decrypt' (string)
    :return: Resulting text after applying the cipher
    """
    result = ""

    # Adjust the shift for decryption
    if mode == "decrypt":
        shift = -shift

    for char in text:
        # Check if the character is alphabetic
        if char.isalpha():
            # Determine if it's uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Shift the character
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

# Main function to interact with the user
def main():
    print("Welcome to the Caesar Cipher Program!")
    mode = input("Do you want to 'encrypt' or 'decrypt'? ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid option. Please choose 'encrypt' or 'decrypt'.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))

    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
