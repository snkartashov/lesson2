#Практическая работа по уроку "Организация программ и методы строк"
my_string =  input("Введите текст,а мы посчитаем количество символов в тексте:")
size_symbol =  len(my_string)
print(size_symbol)
my_string = ( "Введите текст,а мы посчитаем количество символов в тексте:")
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1]) #30 минут искал ошибку т.к. не отображался результат, оказалось что он отображал пробел после : " "