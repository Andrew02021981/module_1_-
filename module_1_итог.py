 # 1 способ
grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Джонни', 'Бильбо', 'Стив', 'Гендрик', 'Аарон'}
a=sum(grades[0])/len(grades[0])
b=sum(grades[1])/len(grades[1])
c=sum(grades[2])/len(grades[2])
d=sum(grades[3])/len(grades[3])
e=sum(grades[4])/len(grades[4])
stud_list=sorted(list(students))
average_grades={stud_list[0]:a,stud_list[1]:b,stud_list[2]:c,stud_list[3]:d,stud_list[4]:e}
print(average_grades)

# 2 способ
grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Джонни', 'Бильбо', 'Стив', 'Гендрик', 'Аарон'}
stud_list=sorted(list(students))
average_grades={}
for i in range (0, len(grades)):
    a=sum(grades[i])/len(grades[i])
    average_grades.update({stud_list[i]:a})
print(average_grades)