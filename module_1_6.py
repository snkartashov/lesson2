#Практическое задание по теме: "Словари и множества"
#словари
my_dict = ({"Sergey" : 1995, "Nikolai" : 1967, "Valentin" : 1993, "Maria" : 1988, "Pavel" : 2007, " Alex" : 2001})
print(my_dict)
print(my_dict.get("Sergey"), my_dict.get("Max"))
my_dict.update({"Oleg" : 1756,
                   "Petr" : 1725,
                   "Leonid" : 2020})
del my_dict["Maria"]
print(my_dict)
#множества
my_set = {1, 2, 3, 2,'keys', 4, 5, 1, 2, 6,"set", "trembolon", 'oleg', ' true', 'true', 'oleg', 'keys', 4, 5, 6, 2, 7, 8}
print(set(my_set))
my_set.add("clock") #.add 1 элемент добавляет
my_set.add(99)
print(my_set)
my_set.update({'nice', 18, 21, 99, 'tea', 'coffee'}) #.update несколько элементов
print(my_set)
my_set.discard("true")
my_set.remove("nice")
#my_set.remove("77")  нет такого элемента и выдаст ошибку
print(my_set)