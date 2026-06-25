'''# Methods to manipulate tuples in Python.
countries=('India','USA','UK','Australia','Canada')
added_countries=countries + ('Germany','France') # adding two tuples
print(added_countries)
# you can also use append() method to add element in tuple but it will give error because tuples are immutable
added_countries.append('Italy') # this will give error because tuples are immutable
# removing something from tuple is also not possible because tuples are immutable
added_countries.remove('Germany') # this will give error because tuples are immutable
added_countries.pop() # this will give error because tuples are immutable'''
print('But we can convert tuple to list and then perform operations on it and then convert it back to tuple')
colors=['red','green','blue','yellow']
temp=list(colors) # converting tuple to list
temp.append('orange') # adding element in list
print(temp)
temp.remove('green') # removing element from list
temp.pop() # removing last element from list
print(temp)
temp[0]='purple' # changing element in list
print(temp)
temp.pop(1) # removing element at index 1 from list
colors=tuple(temp) # converting list back to tuple
print(colors)
utensils1=('spoon','fork','knife')
utensils2=('plate','bowl','cup')
# joining two tuples together
print('Joining two tuples together')
utensils3=utensils1 + utensils2
print(utensils3)
# use counter() method to count the number of occurrence of specific element in tuple
tuple1=(1,2,3,5,6,1,21,2,1,66,2,77,88,99,2,11,22,2)
print("Counting the number of occurrence of specific element in tuple")
print(tuple1.count(1))
# using index() method to find the index of first occurrence of specific element in tuple
print("Finding the index of first occurrence of specific element in tuple")
print(tuple1.index(2))
# you can also use slicing to find the index of first occurrence of specific element in tuple
print("Finding the index of first occurrence of specific element in tuple using slicing")
result=tuple1.index(2,5,11)
print(result)
print('length of tuple1:', len(tuple1))