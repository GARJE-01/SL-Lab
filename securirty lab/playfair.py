import numpy as np

def generate_key_table(key):
    key = ''.join(dict.fromkeys(key.lower().replace('j', 'i').replace(" ", "")))
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key_table = [c for c in key if c in alphabet] + [c for c in alphabet if c not in key]
    return np.array(key_table).reshape(5, 5)

def search(key_table, a, b):
    if a == 'j': a = 'i'
    if b == 'j': b = 'i'
    p1, p2 = np.where(key_table == a)[0][0], np.where(key_table == b)[0][0]
    return (p1 // 5, p1 % 5), (p2 // 5, p2 % 5)

def decrypt(cipher, key):
    key_table = generate_key_table(key)
    deciphered = []

    for i in range(0, len(cipher), 2):
        p1, p2 = search(key_table, cipher[i], cipher[i+1])
        if p1[0] == p2[0]:  # Same row
            deciphered.append(key_table[p1[0], (p1[1]-1)%5])
            deciphered.append(key_table[p2[0], (p2[1]-1)%5])
        elif p1[1] == p2[1]:  # Same column
            deciphered.append(key_table[(p1[0]-1)%5, p1[1]])
            deciphered.append(key_table[(p2[0]-1)%5, p2[1]])
        else:  # Rectangle swap
            deciphered.append(key_table[p1[0], p2[1]])
            deciphered.append(key_table[p2[0], p1[1]])

    return ''.join(deciphered)

if __name__ == "__main__":
    key = "Monarchy"
    cipher = "gatlmzclrqtx"
    decrypted_text = decrypt(cipher, key)
    print("Deciphered text:", decrypted_text)