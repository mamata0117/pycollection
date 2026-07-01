number=[2,4,6,71,3,1,5]
#to add element in list
number.append(8)
print(number)
#sorting list
number1=[10,5,3,7,1,9,2]
number1.sort()
print(number1)
number1.sort(reverse=True)
print(number1)
number1.reverse()
print(number1)
number1.insert(4,11)
print(number1)
#
list1=[1,2,3,4,5]
print(list1.append(6)) #it returns None because append() method does not return any value
print(list1)
print(list1.count(1)) #it returns the number of occurrence of 1 in list1
#functions like append(),sort(),reverse() and insert() do not return any value. They just modify the list in place.
#soring in strings
list2=['banana','apple','grapes','kiwi']
list2.sort()
print(list2)

list3=['banana','litchi','apple']
list3.sort()
print(list3)
#reverse sorting in strings
list4=['banana','litchi','apple']
list4.sort(reverse=True)
print(list4)
#
list3=['a','f','c','b','d','e']
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
#removing element from list
list7=['banana','litchi','apple','litchi']
list7.remove('litchi')
print(list7)
#using remove method to remove element from list
list4=[9,8,7,6,5,4,3,2,1,9,7,9]
print(list4.remove(9)) 
#it returns None because remove() method does not return any value
print(list4)
list4.pop() #it removes the last element from the list
print(list4)
list4.pop(3) #it removes the element at index 3 from the list
print(list4)