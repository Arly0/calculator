print("Введите пример.")
paradigm = input()

def summ_function(a,b):
	return a + b

def multiple_function(a,b):
	return a * b

def subt_function(a,b):
	return a - b

def div_function(a,b):
	return a / b

# ВАЖНО! функции объявлять перед выполнением.
# Тут нужно будет строку,который вводит юзер разобрать на
# числа, с которыми будут производиться вычисления. 
# Ко всему прочему нужно определить знак и в соотношении с ним
# запустить нужную функцию и передать параметры. И вернуть ответ.

# тут предположительно будет знак и числа, которые спарсяться
symbol = "+"
a = 13
b = 2

switcher = {
	'+': summ_function(a,b),
	'-': multiple_function(a,b),
	'*': subt_function(a,b),
	'/': div_function(a,b)
}


print(switcher[symbol])