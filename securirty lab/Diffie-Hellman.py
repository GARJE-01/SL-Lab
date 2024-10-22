p = 23 
g = 5   

alice_private = 6
alice_public = pow(g, alice_private, p)

bob_private = 15
bob_public = pow(g, bob_private, p)

alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

print("Alice's shared secret:",alice_shared)
print("Bob's shared secret:",bob_shared)

print("Shared secrets match:", alice_shared == bob_shared)

4.
import random

def diffie_hellman(p, g):
    a = random.randint(1, p-1)  # Alice's private key
    b = random.randint(1, p-1)  # Bob's private key
    A = pow(g, a, p)            # Alice's public key
    B = pow(g, b, p)            # Bob's public key
    secret_a = pow(B, a, p)     # Shared secret for Alice
    secret_b = pow(A, b, p)     # Shared secret for Bob
    return A, B, secret_a

# Example usage
p = 23  # Prime number
g = 5   # Generator
A, B, secret = diffie_hellman(p, g)
print("Alice's public key:", A)
print("Bob's public key:", B)
print("Shared secret:", secret)
