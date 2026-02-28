collection = list()#
collection = {}

print(type(collection))

coolection ={10,10.5,"text",True}

print(list(coolection)[0].upper())

fruits= ["apple","lemon","pamelo","pineapple","mango"]

print(fruits[0])

print(fruits[1:3])

print(fruits[:4])
print(fruits[1:])

fruits_count = len


print(', '.join(fruits))
fruits.append('kiwi')
print(', '.join(fruits))
fruits.extend(['orange', 'banana'])
print(', '.join(fruits))
fruits.insert(3, 'watermelon')
print(', '.join(fruits))

fruits = ['apple', 'lemon', 'pamelo', 'mango', 'pineapple', 'watermelon']

print(', '.join(fruits))
fruits.append('kiwi')
print(', '.join(fruits))
fruits.extend(['orange', 'banana'])
print(', '.join(fruits))
fruits.insert(3, 'watermelon')
print(', '.join(fruits))

apple_count = fruits.count('apple')
print(apple_count)
watermelon_count = fruits.count('watermelon')
print(watermelon_count)
grapefruit_count = fruits.count('grapefruit')
print(grapefruit_count)

while 'watermelon' in fruits:
    fruits.remove('watermelon')

print(', '.join(fruits))

if 'grapefruit' in fruits:
    fruits.remove('grapefruit')

    print(fruits.index("pineapple"))
    print(fruits.index("watermelon"))
    print(fruits.index("grapefruit"))
    print(fruits_coppy)
    print(fruits)
    fruits_copy.append("grapefruit")
    fruits.sort()
    print(fruits)
    fruits.reverse()
    print(fruits)
    new_list = {expression for variable in iterable if condition}
    numbers={10,1,2,3,-6,12,0,-11,5}
    even_numbers=[]
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
            

    

