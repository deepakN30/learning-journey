text = str(input("Enter your secrete message: "))
shift = int(input("Enter your shifing or offset values: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(text,shift,value =1):
    encrypted_text = ''
    for char in text.lower():
        if char ==" ":
            encrypted_text += char
        elif char in alphabet:
            index = alphabet.find(char)
            new_index =( index + value*shift)%len(alphabet)
            encrypted_text += alphabet[new_index] 
        else:
            encrypted_text +=char
    return encrypted_text

Encryption = caesar(text,shift)
print(Encryption)

decryption = caesar(Encryption,shift,-1)
print(decryption)
