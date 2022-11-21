'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

25164150
'''
num = 0
num1 = 0
for i in range(1, 101):
    num = (num + (i ** 2))
print(num)
for i in range(1, 101):
    num1 = num1 + i
num1 = (num1 ** 2)
print(num1)
print(num1 - num)
