shopList = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shopList),'items to purchase')

print('These items are:', end = ' ')
for item in shopList:
    print(item, end = ' ')

print('\nI also have to buy rice.')
shopList.append('rice')
print('My shopping list is now', shopList)

print('I will sort my list now')
shopList.sort()
print('Sorted shopping list is', shopList)

print('The first item I will buy is', shopList[0])
olditem = shopList[0]
del shopList[0]
print('I bought the', olditem)
print('My shopList list is now', shopList)