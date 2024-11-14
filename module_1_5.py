# example = "Топинамбур"
# print(example[0])
# print(example[-1])
# print(example[5:])
# print(example[::-1])
# print(example[1:10:2])


#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = 1, 2, 3, 4, 5, 6, 'jww', 1.55 , 18, 'one'
print(immutable_var)
#immutable_var[0] = 7 #тип данных "tuple" нельзя изменять, поэтому закинем эту функцию тоже в комментарий
mutable_list = [2002, "inst", 'а почему бы и нет?', "будет или", "не будет"]
mutable_list[2] = "а потому что! :D "
print(mutable_list)
