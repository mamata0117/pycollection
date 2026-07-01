# for loop is use for sequential traversal of data structure like list, tuple, string etc. It is also used to iterate over a sequence of numbers using range() function.s
#1 to print numbers in a list
'''list1=[1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
#2
string1='pythonlearn'
for char in string1:
    print(char)
#3 print el in the list
list2=[1,4,9,16,25,36,49,64,81,100]
for num in list2:
    print(num)
# search el in the list
list3=[1,4,9,16,25,36,49,64,81,100]
x=16
idx=0
for num in list3:
    if num==x:
        print(x,'num found at index',idx)
    idx+=1   '''
#range() starts from 0 and ends at n-1
# range(start?,stop,step?)
for i in range(5):    #range(stop)
    print(i,end=' ')
print()    
for i in range(1,5):    #range(start,stop)
    print(i,end=' ')
print()
for i in range(1,10,2):     #range(start,stop,step)
    print(i,end=' ')    
print()