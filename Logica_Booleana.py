print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6, '\n')

if (1 == 1) and (2 + 2 > 3):
    print('true')
else:
    print('false \n')

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6, '\n')

age = 15
money = 500
if age > 18 or money > 100:
    print('Welcome \n')

print(not 1 == 1)
print(not 1 > 7, '\n')

if not True:
    print('1')
elif not (1 + 1 == 3):
    print('2')
else:
    print('3')