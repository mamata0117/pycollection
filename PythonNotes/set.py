'''collection={1,2,3,'a','b','c',5}
print(collection)
collection1={1,2,3,'a','b','c',1,2,3}
print(collection1)
print(type(collection1))'''
# set does not allow duplicate values.
set1={1,3,5,67,2,1,1,3}
print(len(set1))
# since doesnt support duplicate value it will count duplicate value as one and will not count it again.
items={}
print(type(items))
# it will return dictionary because we have not used set() function to create a set.
items=set()
print(type(items))