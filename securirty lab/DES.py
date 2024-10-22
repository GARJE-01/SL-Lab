# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'abcdefgh'  # Example key
cipher = DES.new(key, DES.MODE_CBC)


plaintext = b'This is a test.'
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))


decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)


print("Ciphertext:",ciphertext)
print("Decrypted:",decrypted.decode('utf-8'))
# from Crypto.Cipher import DES

# key = b'8bytekey'  # 8-byte key
# cipher = DES.new(key, DES.MODE_ECB)

# plaintext = "Hello DES"  # Text to encrypt
# padded_text = plaintext + ' ' * (8 - len(plaintext) % 8)  # Padding

# encrypted = cipher.encrypt(padded_text.encode())
# print("Encrypted:", encrypted)

# decrypted = cipher.decrypt(encrypted).decode().strip()
# print("Decrypted:", decrypted)