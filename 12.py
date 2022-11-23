'''
What is the value of the first triangle number to have over five hundred divisors?

76576500
'''

import sys

i = 0
num = 0
for i in range(50000000000):
    num = num + i
    iter = 0
    for x in range(1, int(num ** (1/2)) + 1):
        if num % x == 0:
            iter += 2
        else:
            continue
    if iter >= 500:
        print(num)
        print(iter)
        sys.exit()
print("Finished.")
