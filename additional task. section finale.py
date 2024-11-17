
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_scores = [sum(student_grades) / len(student_grades) for student_grades in grades]
#print(average_scores)

#print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(list(sorted(students)))
students = (list(students))
dict = ({key:value for (key,  value) in zip (sorted(students), average_scores)})
print(dict)





