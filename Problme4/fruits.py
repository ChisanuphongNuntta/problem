fruits = []

#Let's anqueue some fruits into list
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

#Now let's dequeue our fruits, we should get 'banana'
first_item = fruits.pop(0)
print(first_item)

#'mango' and 'orange' remain
print(fruits)