import re

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

numbers = r'[0-9]+[.]?[0-9]?' #search float or int number
allnumbers = re.findall(numbers, paradigm)
symb = r'[\+\-\*\/\^]' #search '+-*/^'
paradigm_symbol = re.findall(symb, paradigm)

a = float((allnumbers[0]))
b = float((allnumbers[1]))
symbol = (paradigm_symbol[0])

switcher = {
	'+': summ_function(a,b),
	'*': multiple_function(a,b),
	'-': subt_function(a,b),
	'/': div_function(a,b),
    '^': pow_function(a,b)
}


print('Ответ: ' + str(switcher[symbol]))