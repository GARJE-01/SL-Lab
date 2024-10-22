def gcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a 

def mod_inverse(e, phi): 
    for d in range(1, phi): 
        if (e * d) % phi == 1: 
            return d 

def generate_keys(): 
    p, q = 61, 53  # Two prime numbers
    n = p * q  # Modulus
    phi = (p - 1) * (q - 1)  # Euler's Totient function
    e = 17  # Public exponent (chosen here as 17)
    d = mod_inverse(e, phi)  # Private exponent (calculated)
    return (e, n), (d, n)  # Return public and private keys

def encrypt(message, public_key): 
    e, n = public_key 
    return [(ord(char) ** e) % n for char in message]  # Encrypt each character

def decrypt(cipher, private_key): 
    d, n = private_key 
    return ''.join([chr((char ** d) % n) for char in cipher])  # Decrypt back to message

# Example usage 
public_key, private_key = generate_keys() 
message = "HELLO" 
encrypted = encrypt(message, public_key) 
decrypted = decrypt(encrypted, private_key) 

print("Original:", message) 
print("Encrypted:", encrypted) 
print("Decrypted:", decrypted)

# import math

# def gcd(a, h):
#     temp = 0
#     while(1):
#         temp = a % h
#         if (temp == 0):
#             return h
#         a = h
#         h = temp


# p = 3
# q = 7
# n = p*q
# e = 2
# phi = (p-1)*(q-1)

# while (e < phi):

#     if(gcd(e, phi) == 1):
#         break
#     else:
#         e = e+1


# k = 2
# d = (1 + (k*phi))/e

# msg = 12.0

# print("Message data = ", msg)

# c = pow(msg, e)
# c = math.fmod(c, n)
# print("Encrypted data = ", c)

# m = pow(c, d)
# m = math.fmod(m, n)
# print("Original Message Sent = ", m)
# def gcd(a, b): 
#     while b: 
#         a, b = b, a % b 
#     return a 
 
# def mod_inverse(e, phi): 
#     for d in range(1, phi): 
#         if (e * d) % phi == 1: 
#             return d 
# def generate_keys(): 
#     p, q = 61, 53 
#     n = p * q 
#     phi = (p - 1) * (q - 1) 
#     e = 17 
#     d = mod_inverse(e, phi) 
#     return (e, n), (d, n) 
 
# def encrypt(message, public_key): 
#     e, n = public_key 
#     return [(ord(char) ** e) % n for char in message] 
 
# def decrypt(cipher, private_key): 
#     d, n = private_key 
#     return ''.join([chr((char ** d) % n) for char in cipher]) 
 
# # Example usage 
# public_key, private_key = generate_keys() 
# message = "HELLO" 
# encrypted = encrypt(message, public_key) 
# decrypted = decrypt(encrypted, private_key) 
 
# print("Original:", message) 
# print("Encrypted:", encrypted) 
# print("Decrypted:", decrypted)