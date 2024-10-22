import hashlib

def sha384_hash(message):
    return hashlib.sha384(message.encode()).hexdigest()

def sha512_hash(message):
    return hashlib.sha512(message.encode()).hexdigest()

# Example usage
msg = input("Enter message: ")
print("SHA-384 Hash:", sha384_hash(msg))
print("SHA-512 Hash:", sha512_hash(msg))
