# Домашняя работа по уроку "Стиль кода часть II. Цикл While"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
    if my_list[index] > 0:
        continue
    elif my_list[index] == 0:
        pass
        index += 1
    elif my_list[index] < 0:
        break

