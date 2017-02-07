""" Example 1
p = 7
q = 5
d = 11 as the private keys,
n = 35
phi(n) = 24
e = 11 as the public keys """
# totient of n = (p-1)(q-1) = phi(n)
# e : (must be coprime to phi(n)) && 1 < e < phi(n)
#finds e
"""for e in range(1000000):
	test = gcd(e, phi(n))
	if test == 1:
		print(e)"""
# de = 1 (mod phi(n))  <- congruence relation
#finds d
"""for d in range(1000000):
	mod = (d*e) % phi(n)
	if mod == 1:
		print(d)"""

""" Example 2
p = 1549
q = 1543
n = 2390107
phi(n) = 2387016
d = 179987
e = 2040131
"""
from fractions import gcd
# in working condition!!!
# uses RSA encryption to encrypt or decrypt a message
#                                                            To be implemented:
# (1) plug in a series of numbers into the function, and it can either encrypt it or decrypt it.
# (2) the numbers will come from letters and be converted back into letters when decrypted
# (3) easy way to deal with large values of p, q, n, phi(n), d, and e. (not have to type them in every time)
# (4) add a padding scheme to turn the message, M, into number(s), m, to encrypt
def encrypt(m):
    e = int(input("public key exponent? (e) "))
    n = int(input("product of primes? (n) "))
    #c gets (m^e) % n
    c = pow(m, e, n)
    return c

def decrypt(c):
    n = int(input("product of primes? (n) "))
    d = int(input("d such that de = 1 + k * phi(n)? "))
    m = pow(c, d, n)
    return m








