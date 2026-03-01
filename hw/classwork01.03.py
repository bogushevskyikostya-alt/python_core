def my_sum(num1: float | int, num2: float | int) -> float | None:
    if type(num1) != float or type(num2) != float:
        return
    return num1 + num2

result = my_sum(10.0, 12.0)
print(result)


def print_full_name(last_name, first_name):
    print("Повне ім'я:", last_name, first_name)


print_full_name('Ковальчук', 'Антон')
print_full_name(last_name='Ковальчук', first_name='Антон')


def print_full_name(last_name, first_name):
    print("Повне ім'я:", last_name, first_name)


print_full_name('Ковальчук', 'Антон')
print_full_name(last_name='Ковальчук', first_name='Антон')

def my_animal(type, name, age):
    print(f'У мене є {type} на ім\'я {name}. Вік: {age}')


my_animal('собака', age=10, name='Патрон')

def my_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print(my_sum(10,12, 34))
print(my_sum(10))
print(my_sum(10,10,10,10,10,10,10,10,10,10,10))

def unpack_positional(a,b,c):
    print(a, b, c)

    def unpack_positional(a, b, c):
    print(a, b, c, sep=', ')


fruits = ['apple', 'orange', 'banana']
unpack_positional(*fruits)


def unpack_kw_args(red, green, yellow):
    print(red, green, yellow)


fruits = {
    'red': 'apple',
    'green': 'pear',
    'yellow': 'banana'
}

unpack_kw_args(**fruits)
global_var = 12

def local_func(local_param):
    global global_var
    global_var = 50
    local_var = 10 # локальна область видимості
    print(local_var)
    print(global_var)

local_func(10)
print(global_var)


def do_smth():
    print('Щось робимо...')


def main():
    print('Початок роботи!')
    do_smth()
    print('Кінець роботи!')


if __name__ == '__main__':
    main()

    


    