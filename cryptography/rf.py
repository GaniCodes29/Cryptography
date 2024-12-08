def encryptRailFence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    return ''.join(rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n')

# Example usage
cipher_text = encryptRailFence(input("enter a word to encrypt:"), key=(int(input("enter key val"))))
print(cipher_text)
