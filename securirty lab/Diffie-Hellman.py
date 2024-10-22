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