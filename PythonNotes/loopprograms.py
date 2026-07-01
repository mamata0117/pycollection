# 1 to 100
'''i=1
while i<=100:
    print(i)
    i+=1
# 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
# multiple of table n=3
i=1
while i<=10:
    print(3*i)
    i+=1
# 4    1,4,9,.....100
i=1
while i<=10:
    print(i*i)
    i+=1
#5
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1
#6 search for a number in tuple
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
while idx<len(nums):
    if nums[idx]==x:
        print(f"Number found at index {idx}")
        break
    idx+=1'''

#sum of first n natural numbers using while loop
n=8   
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)  
#using for loop
n=8
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
#factorial of a number using forloop
n=5
fact=1
for i in range(1,n+1):
    fact*=i
    
print(fact)
#while loop
n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)
