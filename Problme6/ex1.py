def numberSplit(num):
    value1 = num // 2
    value2 = num // 2 + (num % 2)
    return value1,value2

print(numberSplit(4))
print(numberSplit(10))
print(numberSplit(11))
print(numberSplit(-9))