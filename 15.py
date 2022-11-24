'''
How many such routes are there through a 20×20 grid?

137846528820
'''


# 20 x 20 grid = 441 spots
# How many ways can we arrange 40 objects, 20 of which are similar (20 ups / 20 downs)?
num = 1
div = 1
for x in range(2, 41):
    num = num * x
    print(num)

for y in range(2, 21):
    div = div * y
    print(div)

num = (num / (div * div))
print(num)

'''
I hate combinatorics
'''
