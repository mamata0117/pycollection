'''Lists are denoted by square brackets [] and are ordered, mutable, and allow duplicate elements. 
They can contain elements of different data types.'''
# Creating a list
my_list = [1, 2, 3, 'Hello', 4.5]
# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: Hello
# negative indexing
print(my_list[-1])  # Output: 4.5
# converting negative index to positive index
print(my_list[len(my_list) - 1])  # Output: 4.5
# check whether certain element is in the list
if 2 in my_list:
    print("2 is in the list")
else:
    print("2 is not in the list")
if 5 in my_list:
    print("5 is in the list")
else:   
    print("5 is not in the list")    
if '4.5' in my_list:
    print("4.5 is in the list") 
else:
    print("4.5 is not in the list")
# checking for a substring in a string
if 'ello' in 'Hello':
    print("ello is in the string 'Hello'")
else:
    print("ello is not in the string 'Hello'")
#   printing all elements in the list
list=[1,2,3,4,5,9,8,7,6]
# using a for loop
for i in list:
    print(i)
print(list)
print(list[:])  
print(list[1:-1])# it prints the elements from index 1 to index 3 (4 is not included)
print(list[1:4]) # it prints the elements from index 1 to index 3 (4 is not included)
# reverselist
print(list[::-1]) # it prints the list in reverse order
# JUMP indexing
print(list[::2]) # it prints every second element in the list
print(list[::3]) # it prints every third element in the list
print(list[1::2]) # it prints every second element in the list starting from index 1
print(list[1::3]) # it prints every third element in the list starting from index 1
print(list[1:4:2]) # it prints every second element in the list from index 1 to index 3 (4 is not included) 
print(list[0:len(list)])
print(list[:len(list)])
print(list[:-1])
# above 3 lines print the same thing, which is the entire list except the last element
print(list[0:len(list)])
print(list[0:])
# it prints the entire list
print('list comprehension')
list1=[i for i in range(4)]
print(list1)
# it prints a list of numbers from 0 to 3
list2=[i**2 for i in range(4)]
print(list2)
# it prints a list of squares of numbers from 0 to 3
list3=[i for i in range(10) if i%2==0]
print(list3)
# it prints a list of even numbers from 0 to 9
list4=[i**2 for i in range(10) if i%2==0]
print(list4)
# it prints a list of squares of even numbers from 0 to 9
