num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))
operation = input('''Введите требуемое действие
+ для сложения 
- для вычитания
* для умножения
/ для деления ''')
try:
	if operation == '+':
		print ("Сумма чисел равна", num_1 + num_2)
	elif operation == '-':
		print ("Разность чисел равна", num_1 - num_2)
	elif operation == '*':
		print ("Произведение чисел равно", num_1 * num_2)
	elif operation == '/':
		print ("Частное чисел равно", num_1 / num_2)
	else:
		print ("Что-то пошло не так, перезапустите калькулятор")
except: 
	print ("Попробуйте еще раз!")

