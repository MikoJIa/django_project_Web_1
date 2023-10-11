def accum(s):
    index = 1
    lst = ''
    for i in s:
        lst += (i * index + '-').capitalize()
        index += 1
    return lst[0:-1]


print(accum('ZpglnRxqenU'))