def create_grid(keyword):
    keyword = ''.join(dict.fromkeys(keyword.replace('j', 'i')))
    alpha_letter = 'abcdefghiklmnopqrstuvwxyz'
    grid = [*keyword] + [ch for ch in alpha_letter if ch not in keyword]
    return [grid[i:i + 5] for i in range(0, 25, 5)]

def prepare_digraphs(plain_text):
    plain_text = plain_text.replace('j', 'i')
    digraphs, i = [], 0
    while i < len(plain_text):
        pair = plain_text[i:i + 2]
        if len(pair) == 1 or pair[0] == pair[1]:
            digraphs.append(pair[0] + 'x')
            i += 1
        else:
            digraphs.append(pair)
            i += 2
    return digraphs

def find_position(grid, letter):
    for r, row in enumerate(grid):
        if letter in row:
            return r, row.index(letter)

def encrypt_decrypt_digraph(digraph, grid, mode=1):
    pos1, pos2 = find_position(grid, digraph[0]), find_position(grid, digraph[1])
    if pos1[0] == pos2[0]:  # Same row
        return grid[pos1[0]][(pos1[1] + mode) % 5] + grid[pos2[0]][(pos2[1] + mode) % 5]
    elif pos1[1] == pos2[1]:  # Same column
        return grid[(pos1[0] + mode) % 5][pos1[1]] + grid[(pos2[0] + mode) % 5][pos2[1]]
    else:  # Rectangle rule
        return grid[pos1[0]][pos2[1]] + grid[pos2[0]][pos1[1]]

def playfair_cipher(keyword, plain_text, mode=1):
    grid = create_grid(keyword)
    digraphs = prepare_digraphs(plain_text)
    return ''.join(encrypt_decrypt_digraph(d, grid, mode) for d in digraphs)

# Input and output
keyword = input('Enter a keyword: ').lower()
plain_text = input('Enter a plain text: ').lower()

encrypted_text = playfair_cipher(keyword, plain_text, mode=1)
decrypted_text = playfair_cipher(keyword, encrypted_text, mode=-1)

print(f'Encrypted Text: {encrypted_text}')
print(f'Decrypted Text: {decrypted_text}')
