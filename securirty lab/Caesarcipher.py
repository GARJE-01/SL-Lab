
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result

text = "Attack at Once!"
shift = 4


print("Text   :", text)
print("Shift  :", shift)
print("Cipher :", encrypt(text, shift))