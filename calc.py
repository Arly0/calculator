import re
#import math
print('Калькулятор к вашим услугам. Доступные действия над числами: +, -, *, /, ^, &(корень), $(деление с отображением остатка)')
paradigm = input("Введите пример: ")

def summ_function(a,b):
	return a + b

def multiple_function(a,b):
	return a * b

def subt_function(a,b):
	return a - b

def div_function(a,b):
	try:
		a / b
	except ZeroDivisionError:
		return "На ноль делить нельзя"
	return a / b

def pow_function(a,b):
    return a ** b

def sqrt_function(a,b):
	return int(a ** (1/b))

def division_function():
	x = int(a) // int(b)
	z = int(a) % int(b)
	print('Ответ: ' + str(x) + '/Остаток: ' + str(z))

numbers = r'[0-9]+[.]?[0-9]?' #search float or int number
allnumbers = re.findall(numbers, paradigm)
symb = r'[\+\-\*\/\^\&\$]' #search '+-*/^&'

paradigm_symbol = re.findall(symb, paradigm)

# Для ввода 3 и больше чисел сделать присвоение цифр через цикл в другой массив и проводить
# с ними действия
a = float((allnumbers[0]))
b = float((allnumbers[1]))

symbol = (paradigm_symbol[0])

switcher = {
	'+': summ_function(a,b),
	'*': multiple_function(a,b),
	'-': subt_function(a,b),
	'/': div_function(a,b),
    '^': pow_function(a,b),
	'&': sqrt_function(a,b),
}

if symbol == '$':
	division_function()
else:
	print('Ответ: ' + str(switcher[symbol]))
