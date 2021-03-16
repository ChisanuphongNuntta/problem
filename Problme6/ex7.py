def sumTowSmallsetNums(num):
    num = sorted(num)
    sum = []
    for i in num:
        if i >= 0:
            sum.append(i)
    
    sumnum = sum[0] + sum[1]
    return sumnum

print(sumTowSmallsetNums([19,5,42,2,77]))
print(sumTowSmallsetNums([2,5444444444,456484564,456565,745465]))