'''
What is the sum of the digits of the number 2^1000?

1366
'''
num2 = 0
num = str(2 ** 1000)
for i in range(len(num)):
    num1 = int(num[i])
    num2 = num2 + num1
print(num2)
