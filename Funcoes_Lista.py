nums = [1, 2, 3]
nums.append(4)
print(nums, '\n')

words = ['Hello']
words.append('world')
print(words[1], '\n')

nums = [1, 3, 5, 2, 4]
print(len(nums), '\n')

letters = ['a', 'b', 'c']
letters.append('d')
print(len(letters), '\n')

words = ['Pythin', 'fun']
index = 1
words.insert(index, 'is')
print(words, '\n')

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11) # Na posição 2 irá inseriri o 11
print(len(nums), '\n')

letters = ['p', 'q', 'r', 's', 't', 'u']
print(letters.index('r')) # Retorna a posição em que ele se encontra
print(letters.index('p')) # Retorna a posição em que ele se encontra
# print(letters.index('z')) # Vai dar erro, pois na lista não existe 
print('\n')

list = [1, 2, 3, 4]
if len (list) % 2 == 0:
    print(list[0])
print('\n')

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters)
print(letters[2])