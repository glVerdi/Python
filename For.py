# Usa-se qnd tem uma sequencia de iterações
words = ['hello', 'world', 'spam', 'eggs']
for word in words:
    print(word + '!')
print('\n')

letters = ['a', 'b', 'c']
for I in letters:
    print(I)
print('\n')

str = 'testing for loops'
count = 0
for x in str:
    if (x == 't'):
        count += 1
print(count, '\n')

list = [2, 3, 4, 5, 6, 7]
for x in list:
    if (x % 2 == 1 and x > 4):
        print(x)
        break
print('\n')

list = [1, 2, 3]
for var in list:
    print(var)