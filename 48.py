'''
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

9110846700
'''


num = 0
for i in range(1, 1001):
    num = num + (i ** i)
print(num)
