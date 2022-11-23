'''
Which starting number, under one million, produces the longest chain?

837799; 524 chain
'''

list1, list2 = [], []
for i in range(1, 1000001):
    num = i
    seq = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            seq += 1
        else:
            num = (3 * num) + 1
            seq += 1
    print(seq, i)
    list1.append(int(i))
    list2.append(int(seq))
ans = max(list2)
spot = list2.index(ans)
fin = list1[spot]
print(fin)
