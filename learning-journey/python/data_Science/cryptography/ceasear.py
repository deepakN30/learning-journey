text = "Hello World"
shift = 3
aplhabet = "abcdefghijklmnopqrstuvwxyz"
ecrypted_text = ''

for char in text.lower():
    index = aplhabet.find(char)
    new_index = index + shift
    encrypted_text = aplhabet[new_index]
    print('char: ', char,'encrypted_text: ',encrypted_text)
