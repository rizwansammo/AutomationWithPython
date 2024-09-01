def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher(text, shift, encrypt=True)
print(f"Encrypted: {encrypted_text}")
decrypted_text = caesar_cipher(encrypted_text, shift, encrypt=False)
print(f"Decrypted: {decrypted_text}")
