'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

142913828922
'''

prime = 3 + 2
for i in range(2000001):
    rng = int(i ** (1/2))
    for x in range(2, rng + 1):
        if i % x == 0:
            break
        elif x == rng:
            prime = prime + i
print(prime)
