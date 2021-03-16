def numberSplit(num):
    value1 = num // 2
    value2 = num // 2 + (num % 2)
    return value1,value2

print(numberSplit(5))