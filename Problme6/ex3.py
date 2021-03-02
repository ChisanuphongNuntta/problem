message = input('Enter : ')
def capToFront(message):
    e = ''.join(sorted(message))
    return e


print(capToFront(message))