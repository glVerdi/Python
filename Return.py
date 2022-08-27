def max(x, y):
    if x >= y:
        return x
    else:
        return y
print(max(4, 7))
z = max(8, 5)
print(z)
print('\n')

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")
print(add_numbers(4, 5))
print('\n')

def print_numbers():
    print(1)
    print(2)
    return
    print(4)
    print(6)
print(print_numbers())
print('\n')

def print_nums(x):
    for i in range(x):
        print(i)
        return 
print_nums(10)
print('\n')

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(4))
print('\n')

celsius = int(input())

def conv(celsius):
    F = (celsius * 9/5) + 32
    return F

fahrenheit = conv(celsius)
print(fahrenheit)