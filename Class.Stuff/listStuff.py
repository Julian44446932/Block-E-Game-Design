#Julian Meyer
#lists and lists Methods
import os, random
os.system('cls')
fruits=["bananas", "grapes", "bananas", "watermelon", 'oranges', 'tomatoes', 'mangos', "kiwis", 'strawberry', 'apples', 'blackberries', 'blueberries', 'mangos']
#length of your array
size=len(fruits)
print(size)
fruits.append("rambutan")
for i in range(size+1): # 13 is not included
    print(fruits[i])
print(fruits[size])
print(fruits[-2])
print(fruits.count('bananas'))
list2=[3,6,8,8,10]
fruits.append(list2)
print("append\n",fruits)
fruits.pop(-1)
fruits.extend(list2)
print("extend \n",fruits)
fruits.insert(2,"dragon fruit")
print(fruits)

