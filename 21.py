'''
Evaluate the sum of all the amicable numbers under 10000

31626
'''


def amic(num):
    div_num = [1]
    for i in range(2, int((num/2)) + 1):
        if num % i == 0:
            div_num.append(i)
            continue
    return sum(div_num)


lst = []
for i in range(10001):
    if amic(amic(i)) == i and amic(i) != i:
        if i not in lst:
            lst.append(i)
print(sum(lst))
