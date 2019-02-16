fruits = {}
fruits['apples'] = 10
print('apples' in fruits)
if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1
fruits.setdefault('peaches', 0)
fruits['peaches'] += 1
print(fruits)