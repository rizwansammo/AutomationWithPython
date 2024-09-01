import hashlib

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

text = input("Enter text to hash: ")
print(f"SHA-256 Hash: {hash_text(text)}")
