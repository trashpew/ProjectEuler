'''
Find the sum of the digits in the number 100!

648
'''
num = 1
num2 = 0
for x in range(1, 101):
    num = num * x
num = str(num)
for i in range(len(num)):
    num1 = int(num[i])
    num2 = num2 + num1
print(num2)
