number = input ("Введи номер завдання (1-5): ")

number = int("10")

print (range(5)) # 0 1 2 3 4 

print(range(3,8)) # 3 4 5 6 7
print(range(3,10,3)) # 3 6 9
r = range(10)
print(type(r))

for i in range(2,4, 3):
    print(i,end=" ") 
    counter= 0
    while counter< 4:
        counter += 1

    print (i)
    for j in range(4):
        print(j, end=" ")
        for k in range(2):
            print(k, end=" ")
        print()
        counter_outer = 0
        while counter_outer < 5:
            counter_inner = 0
            while counter_inner < 4:
                print(counter_outer, counter_inner)
                counter_inner += 1
            counter_outer += 1
            print("\t", end="")
            # number = int(input('Введіть число: '))

# number = int('10')
# print(type(number))

# float()
# str()
# bool()

print(range(5)) # 0 1 2 3 4
print(range(3, 8)) # 3 4 5 6 7
print(range(3, 10, 3)) # 3 6 9
r = range(10)
print(type(r))

#count = int(input('Скільки разів повторити цикл? '))

# counter = 0
# while counter < count:
#     print(counter)
#     counter += 1

# for i in range(count):
#     if i == 100:
#         break
#     if i % 5 == 0:
#         continue
#     print(i, end=' ')
# else:
#     print('Діапазон закінчився')

for i in range(5):
    print(f'i = {i}')
    for j in range(4):
        print(f'\tj = {j}')
        print('\t\t', end='')
        for k in range(2):
            print(f'k = {k}', end=' ')
        print()
    print()

counter_outer = 0
while counter_outer < 5:
    print(counter_outer)
    counter_inner = 0
    while counter_inner < 4:
        print(counter_inner, end=' ')
        counter_inner += 1
    print()
    counter_outer += 1
    import raandom 

    random_number = random.randint(10,50)

    print(random_number)
    randint = 10
    from random import randint

    randint =12
    random_number = randint(10,50)
    


     

