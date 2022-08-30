"""
ImportError - Impotação falhou
IndexError - Lista indexada com um número fora do intervalo
NameError - Variável desconhecida é usada
SyntaxError - Código não está correto sintaticamente
TypeError - Uma função é chamada em um outro tipo de valor
ValueError - Uma função é chamada no mesmo tipo, porém com valor diferente
ZeroDivisionError - Divisão por zero
"""

try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print('Done calculation')
except ZeroDivisionError:
    print('An error occurred')
    print('due to zero division')
print('\n')

try:
    variable = 10
    print(10 / 2)
except ZeroDivisionError:
    print('Error')
print('Finished')
print('\n')

try:
    variable = 10
    print(variable + 'hello')
    print(variable / 2)
except ZeroDivisionError:
    print('Dividede by zero')
except (ValueError, TypeError):
    print('Error occurred')
print('\n')

try:
    meaning = 42
    print(meaning / 0)
    print('The meaning of lif')
except (ValueError, TypeError):
    print('ValueError or TypeError occurred')
except ZeroDivisionError:
    print('Divided by zero')
print('\n')

try:
    word = 'spam'
    print(word / 0)
except:
    print('An error occurred')
print('\n')

try:
    print('Hello')
    print(1 / 0)
except ZeroDivisionError:
    print('Divided by zero')
finally:
    print('This code will run no matter what')
print('\n')

try:
    print(1)
except:
    print(2)
finally:
    print(3)
print('\n')

"""
try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print('unknown_var')
finally:
    print('This is executed last')
print('\n')

print(1)
raise ValueError
print(2)
print('\n')

try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError
print('\n')

name = '123'
raise NameError('Invalid name!')
print('\n')

try:
    num = 5 / 0
except:
    print('An error occurred')
    raise
print('\n')

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
print('\n') 

print(0)
assert 'h' != 'w'
print(1)
assert False
print(2)
assert True
print(3)
print('\n')
"""
temp = -10
assert (temp >= 0), 'Colder than absolute zero!'