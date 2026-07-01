#wap to ask user to enter name of their 3 fav movie  and store them in a list
# movies=[]
# movie1=input("Enter 1st movie name:")
# movie2=input("Enter 2nd movie name:")
# movie3=input("Enter 3rd movie name:")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)
#wap to check whether list contains palindrome of elements
# using copy method
list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if list1==copy_list1:
    print("List contains palindrome of elements")
else:
    print("List does not contain palindrome of elements")    

#tuple program
#wap to count the num of students with 'A' grade in following tuple
tup1=('C','D','A','A','B','B','A')
print(tup1.count('A'))

#store above value in list and sort them from A to D
list1=list(tup1)
print(list1)
list1.sort()
print(list1)