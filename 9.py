'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a = 200, b = 375, c = 425
a*b*c = 31875000
'''

for a in range(0, 500):
    for b in range(0, 500):
        for c in range(0, 500):
            if ((a ** 2) + (b ** 2)) == (c ** 2) and (a + b + c) == 1000:
                    ans = a * b * c
                    print(ans)
