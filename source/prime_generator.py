
from Crypto.Util.number import isPrime, getPrime
import random, time
    
Prime = [i for i in range(3, 2000) if isPrime(i)]


def weak_prime():
    while 1:
        p = 2
        for i in random.sample(Prime, 85):
            p = p * i
        if isPrime(p + 1): break
    return p + 1


def safe_prime(nbits):
    q = getPrime(nbits)
    i = 1
    while 1:
        p = 2 * i * q + 1
        i = i + 1
        if isPrime(p): break
    return p, q


def find_generator(p, q):
    k = (p - 1) // q
    while 1:
        g = random.randint(2, p - 2)
        if pow(g, k, p) != 1: break
    return g



def strong_prime(nbits):
    s = getPrime(nbits // 2 - 4)
    t = getPrime(nbits // 2 - 4)
    i = random.randint(0, 100)
    while 1:
        r = 2 * i * t + 1
        i = i + 1
        if isPrime(r): break

    q = 2 * pow(s, r - 2, r) * s - 1
    j = random.randint(0, 100)
    while 1:
        p = q + 2 * j * r * s
        j = j + 1
        if isPrime(p): break
    return p


def generate_data():
    output = open("safe_prime_variance", "w")
    for i in range(1000):
        start = time.time()
        p, q = safe_prime(1024)
        finis = time.time()
        result = str(finis - start) + ' ' + str(p.bit_length()) + ' ' + str(i)
        output.write(result + '\n')
    output.close()


generate_data()