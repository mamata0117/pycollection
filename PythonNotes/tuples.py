'''tuples use () brackets and are immutable
tuples are faster than lists
tuples can be used as keys in dictionaries
tuples can be used to store multiple items in a single variable'''
tuples=(1,2,3,4,5.6,7,8,9,10,'green','blue','yellow')
print(tuples)
# tuples[0]= 80 or tuples[0]+1 # this will give error because tuples are immutable
print(type(tuples))
print(tuples[0]) # printing specific element in tuple
print(tuples.index(9)) # printing index of first occurrence of specific element in tuple
# negative and positive indexing in tuple is same as in list
print(tuples[-1]) # printing last element in tuple using negative indexing
# slicing in tuple is also same as in list
print("Slicing in tuple")
print(tuples[1:4]) # printing elements from index 1 to 3
print(tuples[:3]) # printing elements from beginning to index 2
print(tuples[3:6]) # printing elements from index 3 to 5