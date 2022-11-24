'''
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

4782
'''

fibnum = [1, 1]
fib = 1
while fib < 1000:
    fibnew = fibnum[-1] + fibnum[-2]
    fibnum.append(fibnew)
    fib = len(str(fibnew))
print(len(fibnum))
