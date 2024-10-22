import hashlib
def sha384_hash(text):
    sha384 = hashlib.sha384()
    sha384.update(text.encode('utf-8'))
    return sha384.hexdigest()

def sha512_hash(text):
    sha512 = hashlib.sha512()
    sha512.update(text.encode('utf-8'))
    return sha512.hexdigest()

text = "MayurGarje"
sha384_result = sha384_hash(text)
sha512_result = sha512_hash(text)

print(f"SHA-384 Hash of '{text}': {sha384_result}")
print(f"SHA-512 Hash of '{text}': {sha512_result}")
