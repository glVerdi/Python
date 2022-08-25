numbers = list(range(10))
print(numbers, '\n')

nums = list(range(5))
print(nums[4], '\n')

numbers = list(range(3, 8)) # Começa em 3 e termina no 7
print(numbers, '\n') 
print(range(20) == range(0, 20), '\n')

nums = list(range(5, 8)) # Começa em 5 e termina em 7
print(nums)
print(len(nums), '\n')

numbers = list(range(5, 20 , 2)) # Começa em 5 e vai até 19, pulando de dois em dois
print(numbers, '\n')

nums = list(range(3, 15, 3)) # Começa em 3 e vai até 12, pois tem que parar antes de aparecer o 15, de tres em tres
print(nums)
print(nums[2], '\n')

for i in range(5):
    print('hello \n')

for i in range(0, 20 , 2):
    print(i)
print('\n')

for i in range(10):
    if not i % 2 == 0:
        print(i + 1)