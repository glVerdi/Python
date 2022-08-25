# Usa-se qnd não tem uma sequencia de iterações
i = 1
while i <= 5:
    print(i)
    i = i + 1
print('finished \n')

i = 3
while i >= 0:
    print(i)
    i = i - 1
print('\n')

x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + ' is even')
    else:
        print(str(x) + ' is odd')
    x += 1
print('\n')  

x = 0
while x <= 20:
    print(x)
    x += 2
print('\n')

i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print('breaking')
        break
print('finished \n')

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break
print('\n')

i = 0
while i < 5:
    i += 1
    if i == 3:
        print('skipping 3')
        continue
    print(i)
print('\n')

while False:
    print('looping...')