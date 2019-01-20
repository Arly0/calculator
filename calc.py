import re

print('Калькулятор к вашим услугам. Доступные действия над числами: +, -, *, /, ^, &(корень), @(деление с отображением остатка)')
paradigm = input("Введите пример: ")

# функции выполнения задач над числами
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
		return 'На ноль делить нельзя'
	return a / b

def pow_function(a,b):
    return a ** b

def sqrt_function(a,b):
	return int(a ** (1/b))

def division_function(a,b):
	x = int(a) // int(b)
	z = int(a) % int(b)
	strXZ = str(x) + '| Остаток: ' + str(z)
	return strXZ


# разбор строки на переменные и работа с ними
numbers = r'[0-9]+[.]?[0-9]?' #search float or int number
allnumbers = re.findall(numbers, paradigm)
symb = r'[\+\-\*\/\^\&\@]' #search '+-*/^&'

paradigm_symbol = re.findall(symb, paradigm)
# symbol = (paradigm_symbol[0])
# Для ввода 3 и больше чисел сделать присвоение цифр через цикл в другой массив и проводить
# с ними действия

def result_function():
	# выбор оператора и вызов соответствующей функции
	switcher = {
		'+': summ_function(a, b),
		'*': multiple_function(a, b),
		'-': subt_function(a, b),
		'/': div_function(a, b),
		'^': pow_function(a, b),
		'&': sqrt_function(a, b),
        '@': division_function(a,b),
	}
	return print('\nОтвет: ' + str(switcher[symbol]))

for i in range(len(allnumbers)):
	symbol = (paradigm_symbol[i])
	if int(i) % 2 == 0:
		a = float(allnumbers[i])
		b = float(allnumbers[i+1])
		result_function()