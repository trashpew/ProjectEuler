'''
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

21124
'''

ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [0, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
hundreds = [0, 10, 10, 12, 11, 11, 10, 12, 12, 11]
thousands = [0, 11]
an = 3

length = 0

for i in range(1, 1001):
    num = str(i)
    if len(num) == 1:
        length += ones[int(num[0])]
    if len(num) == 2:
        if num[0] == '1':
            length += teens[int(num[1])]
            if num[1] == '0':
                length += tens[1]
        else:
            length += tens[int(num[0])]
            length += ones[int(num[1])]
    if len(num) == 3:
        length += hundreds[int(num[0])]
        length += an
        if num[1] == '0' and num[2] == '0':
            length -= an
        if num[1] == '1':
            length += teens[int(num[2])]
            if num[2] == '0':
                length += tens[1]
        else:
            length += tens[int(num[1])]
            length += ones[int(num[2])]
    if len(num) == 4:
        length += thousands[int(num[0])]
        length += hundreds[int(num[1])]
        length += an
        if num[1] == '0' and num[2] == '0':
            length -= an
        if num[2] == '1':
            length += teens[int(num[3])]
            if num[3] == '0':
                length += tens[1]
        else:
            length += tens[int(num[2])]
            length += ones[int(num[3])]
print(length)
