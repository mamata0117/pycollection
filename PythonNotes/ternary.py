#1
fruit=input('Fruit:')
tasty='yes'if fruit=='watermelon' else 'not tasty'
print(tasty)
#2with print
fruit=input('fruit:')
print('tasty') if fruit=='watermelon'or fruit=='mango' else print('not tasty')
#clever if/ternary operator
age=int(input('age:'))
vote=('No','Yes') [age<18]
print(vote)
# in python index(0,1)0=false and 1=true
salary=float(input("Salary:"))
tax=(0.2,0.3) [salary>=99000]
print(tax)
# print(input('name:'))
#logical operators
a,b=50,20
print(a==b) #false
print(a!=b) #true
print(not(a==b)) #true
#typecasting
a,b=1,'2'
c=int(b)
print(a+c)
#use of input
input('Enter your name:')
#use of input and storing
name=input('Enter your name:')
print("Welcome",name)
#wap to enter side of square and print area
length=int(input("Enter your side:"))
print(length*length)
#wap to input 2 floating numbers and print their average
length1=float(input('Num1:'))
length2=float(input('Num2:'))
avg=(length1+length2)/2
print(avg)
#3
a=int(input('Num1:'))
b=int(input('Num2:'))
if (a>=b):
    print("True")
else:
    print('False')
#4
a=int(input('Num1:'))
b=int(input('Num2:'))
print(a>=b)
#string

