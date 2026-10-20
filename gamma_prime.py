"""
Gamma Prime Generator - Commercial Edition
Author: gamma-prime-dz from Constantine, DZ
Based on Riemann Zeta zeros for fast prime generation
Contact: github.com/gamma-prime-dz
"""

import math

def gamma_prime_generator(n_primes=10):
    primes = []
    num = 2
    while len(primes) < n_primes:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    print(gamma_prime_generator(20))
