'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

906609
'''

list = []
f1 = 100
for i in range(899):
    f1 += 1
    f2 = 100
    for x in range(899):
        f2 += 1
        num = (f1 * f2)
        list.append(num)
sort = []
for i in range(int(len(list))):
    num = list[i]
    rev = str(num)[::-1]
    num = str(num)
    if rev == num:
        num = int(num)
        sort.append(num)
print(max(sort))