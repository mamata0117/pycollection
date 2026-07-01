#break is used  to terminate the loop 
#break program when 4 is encountered
i=1
while i<=10:
    print(i)
    if i==4:
        break
    i+=1
#print num from 1 to 10 except 7
i=1
while i<=10:
    if i==7:
        i+=1
        continue
    print(i)
    i+=1
#print only odd num form 1 to 10
i=1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1
#print only even num form 1 to 10
i=1
while i<=10:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1