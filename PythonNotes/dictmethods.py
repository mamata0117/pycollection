# dict1={
#     'name':'ram',
#     'age':20,
#     'subjects':['maths','science','english'],
#     'marks':{
#         'maths':90,
#         'science':85,
#         'english':95
#     }
# }
# #getting all keys from dictionary
# print(dict1.keys())
# #keys as list
# print(list(dict1.keys()))
# #getting all values from dictionary
# print(dict1.values())
# #getting all items from dictionary
# print(dict1.items())
# print()
# #finding length of dictionary by which we get to know len of key and value pairs in dictionary
# print(len(dict1))
# # finding  length of key another way
# print(len(dict1.keys()))
#2
# dict2={
#     'name':'rama',
#     'age':21,
#     'subjects':['maths','science','english'],
#     'marks':{
#         'maths':90,
#         'science':85,
#         'english':95
#     }
# }
# print(dict2['name'])
# lists=list(dict2.items())
# print(lists)
# print(lists[0])

#3
import dictionary


dict2={
    'name':'rita',
    'age':21,
    'subjects':['maths','science','english'],
    'marks':{
        'maths':90,
        'science':85,
        'english':95
    }
}
print(dict2['name'])
print(dict2.get('name'))
# we use get method because if we try to access a key that does not exist in the dictionary using the square bracket notation, it will raise a KeyError. However, using the get() method will return None (or a specified default value) instead of raising an error, making it safer to use when accessing keys that may not be present in the dictionary.So that further code wont be affected or stopped due to error.
dict2.update({'city':'New York'})
print(dict2)
new_dict={'height':5.9,'weight':70}
dict2.update(new_dict)
print(dict2)
#another way to add new key value pair in dictionary
dict2['salary']=50000
print(dict2)
#we we update to an existing key value pair in dictionary it will update the value of that key 
# we could we square bracket notation or update method to update the value of an existing key in a dictionary. Both methods will achieve the same result, but the update method allows you to update multiple key-value pairs at once by passing a dictionary as an argument.