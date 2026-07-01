#mutable,unordered data type in python
#denoted by curly braces {} and items are stored in key value pairs
#  brand={
#     'name':'Apple',
#     'model':'Iphone 14',
#     'year':2026,
# }
# print(brand)
#you can also store list and tuple in dictionary
# brand1={
#     'name':'Apple',
#     'model':'Iphone 14',
#     'year':2026,
#     'colors':['red','blue','green'],
#     'features':('5G','Face ID')
# }
# print(brand1)
# print(brand1['colors'])
# print(brand1['year'])
#3
person={'name':'John',
        'age':30,
        'city':'New York'
        }
#adding new key value pair in dictionary
person['height']=5.9
#updating existing key value pair in dictionary
person['age']=31
print(person)
#4nested dictionary
print("Nested dictionary")
students={
    'name':'Rita',
    'age':20,
    'marks':{
        'maths':90,
        
        'science':85,
        'english':95
    }
}
print(students)
print(students['marks'])
print(students['marks']['maths'])