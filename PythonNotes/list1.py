#lists are mutable
marks=[20,80,99.4,44]
print(marks[3])
print(marks[-1])
students=['ram','gita','sita']
print(students)  #['ram','gita','sita']
print(students[0])  #['ram']
print(students[:])     #['ram','gita','sita']
print(students[:1])    #['ram']
combination=['ram',20,'gita',80,'sita',99.4]
print(combination)     #['ram',20,'gita',80,'sita',99.4]
print(len(combination))  #6
combination[1]='Ramesh'
print(combination)  #['ram', 'Ramesh', 'gita', 80, 'sita', 99.4]