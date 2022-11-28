'''
1 + (3 + 5 + 7 + 9) + (13 + 17 + 21 + 25)
'''
num = 1
count = 1
for b in range(2, 1001, 2):
    for a in range(1, 5):
        num += b
        count += num
print(count)
