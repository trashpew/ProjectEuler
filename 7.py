'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

104743
'''
prime = 10001
p = 1
n_iter = 1
while n_iter <= (prime - 2):
    p = p + 2
    div = 1
    while div < (p ** (1/2)):
        div = div + 2
        if (p % div) == 0:
            break
        if div >= (p ** (1/2)):
            n_iter += 1

print("The {}'th prime is {}".format(prime, p))
