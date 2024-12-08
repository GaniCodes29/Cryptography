import numpy as np
letter_num = {chr(i): i - 97 for i in range(97, 123)}
num_to_letter = {v: k for k, v in letter_num.items()}

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"No modular inverse for {a} under modulo {m}")

def matrix_mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix))) % modulus
    det_inv = mod_inverse(det, modulus)
    adj = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % modulus
    return (det_inv * adj) % modulus

def text_to_numbers(text):
    return [letter_num[char] for char in text]

def numbers_to_text(numbers):
    return ''.join(num_to_letter[num % 26] for num in numbers)

def process_chunks(text, matrix_size, pad_char='x'):
    if len(text) % matrix_size != 0:
        text += pad_char * (matrix_size - len(text) % matrix_size)
    return [text[i:i + matrix_size] for i in range(0, len(text), matrix_size)]

def matrix_multiply_chunks(chunks, matrix, modulus):
    return [(np.dot(matrix, np.array(chunk).reshape(-1, 1)) % modulus).flatten() for chunk in chunks]

# Input data
plain_text = input("Enter plain text: ").lower()
matrix = np.array([[int(input(f"Enter matrix[{i}][{j}]: ")) for j in range(int(input("Enter columns: ")))] for i in range(int(input("Enter rows: ")))])
modulus = 26

# Encryption
chunks = process_chunks(plain_text, len(matrix))
number_chunks = [text_to_numbers(chunk) for chunk in chunks]
encrypted_chunks = matrix_multiply_chunks(number_chunks, matrix, modulus)
encrypted_text = ''.join(numbers_to_text(chunk) for chunk in encrypted_chunks)
print(f"Encrypted text: {encrypted_text}")

# Decryption
matrix_inv = matrix_mod_inverse(matrix, modulus)
decrypted_chunks = matrix_multiply_chunks(encrypted_chunks, matrix_inv, modulus)
decrypted_text = ''.join(numbers_to_text(chunk) for chunk in decrypted_chunks)
print(f"Decrypted text: {decrypted_text}")
