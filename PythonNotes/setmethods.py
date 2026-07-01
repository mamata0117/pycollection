#set is mutable but its elements are immutable
set1={'ram','shyam','hari',2,4,1,5,9}
#adding el
set1.add('gita')
print(set1)
#removing el
set1.remove('ram')
print(set1)
#removing random el
print(set1.pop())
print(set1.pop())
print(set1.pop())
#removing all el
set1.clear()
print(set1)
#union of two sets
set2={1,2,3,4,5}
set3={4,5,6,7,8}
print(set2.union(set3))
#intersection
print(set2.intersection(set3))