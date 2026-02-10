import string

def encrypt_decrypt(text, mode, key):
    letters = string.ascii_lowercase
    num_letters = len(letters)
    result = ''

    key = key % num_letters
    if mode == 'd':
        key = -key

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_position = (ord(char) - start + key) % 26
            result += chr(start + new_position)
        else:
            result += char

    return result

def get_valid_key():
    while True:
        try:
            key = int(input('Enter a key (1 through 25): '))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")
