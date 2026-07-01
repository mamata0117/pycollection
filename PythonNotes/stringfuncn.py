#string function str.endswith() and str.startswith()
str1="I am learning Python"
print(str1.endswith("on.")) #False
print(str1.endswith("on"))   #true
print(str1.endswith("On"))   #False
print(str1.startswith("I am"))  #True
print(str1.startswith("Iam"))   #False
#str.capitalize() and str.title()
str2="i am learning python"
print(str2.capitalize())  #I am learning python
print(str2.title())       #I Am Learning Python
#str.replace() and str.strip()
str3="I am learning Python"
print(str3.replace("Python", "Java"))  #I am learning Java
# strip helps to remove leading and trailing spaces
str4="  I am learning Coding "
print(str4.strip())     #I am learning Coding
#str.find and str.count()
str5="I am learning Python"
print(str5.find("Python"))  #14
print(str5.count("n"))     #3
print(str5.find("Java"))    #-1