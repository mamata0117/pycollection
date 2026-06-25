lists=[1,2,3,4,5.6,7,8,9,10]
print(lists)
# adding element in list
lists.append(11)
print(lists)
#sorting list
list1=[5,66,4,8,0,9,7,44,2,9]
#sorting in ascending order
print("Sorting in ascending order")
list1.sort()
print(list1)
# sorting in descending order
print("Sorting in descending order")
list1.sort(reverse=True)
print(list1)
list1.reverse()
print("Reversing the list")
print(list1)
# printing specific element in list
print("Printing specific element in list")
print(list1[3])
# printing index of specific element in list
print("Printing index of first occurrence of specific element in list")
print(list1.index(9))
list2=[1,2,3,4,5,1,3,7,9,88,77,1]
# counting the number of occurrence of specific element in list
print("Counting the number of occurrence of specific element in list")  
print(list2.count(1))
# copying list
print("Copying list")
fruits=["apple","banana","grapes","orange"]
fruitsnewlist=fruits.copy()
print(fruitsnewlist)
# inserting element in list
print("Inserting element in list")
fruits.insert(2,"kiwi")
print(fruits)
#  two lists are joined together
print("Joining two lists together")
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print('you can use + operator to join two lists together')
list3=list1+list2
print(list3)
# you can also use extend() method to join two lists together
list1.extend(list2)
print(list1)
