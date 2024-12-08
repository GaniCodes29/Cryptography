
import math

p = 3
q = 5

n = p * q
modls_n= ((p - 1) * (q - 1))

e = 2
while e < modls_n:
    if math.gcd(e, modls_n) == 1:
        break
    e += 1

d = pow(e, -1, modls_n)

print(f'Public key: ({e, n})')
print(f'Private key: ({d, n})')

m = 4
ct = math.pow(m, e) % n
dt = math.pow(ct, d) % n
print(f'Encrypt: {ct}')
print(f'Decrypt: {dt}')
