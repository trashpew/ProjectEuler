'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

233168
'''

num = 0
top = 1000
for i in range(top):
    if i % 3 == 0:
        num = num + i
        continue
    elif i % 5 == 0:
        num = num + i
        continue
print(num)