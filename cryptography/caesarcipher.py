
word = input('Enter a word: ')
key_value = int(input('Enter a key value: '))
encrypt = ''
decrypt = ''
for i in range(len(word)):
    char = word[i]
    if (char.isupper()):
        encrypt += chr((ord(char) + key_value - 65) % 26 + 65)
    else:
        encrypt += chr((ord(char) + key_value - 97) % 26 + 97)
print(f'The encrypt text is: {encrypt}')
for i in range(len(encrypt)):
    ch = encrypt[i]
    if (ch.isupper()):
        decrypt += chr((ord(ch) - key_value - 65) % 26 + 65)
    else:
        decrypt += chr((ord(ch) - key_value - 97) % 26 + 97)
print(f'The decrypt text is {decrypt}')
