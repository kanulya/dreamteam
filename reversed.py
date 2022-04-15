
reverse = input("Введите пример функции reversed() через пробел: ")
list = reverse.split()
list1 = list[::-1]
print (list)
print (reverse(list1))

if list1 == reversed(list):
	print ("Вы очень хорошо знаете как работает функция reversed()")
#else: 
#	print ("Вам надо подучить как работает эта функция ))")




