# 1. Create a dictionary and print the value of 'Age'.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur'}
print("Q1")
print(dict1)
print("Age =", dict1['Age'])
print()


# 2. Add 'Occupation':'Engineer' to an existing dictionary.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur'}
print("Q2")
print("Existing dictionary =", dict1)
dict1['Occupation'] = 'Engineer'
print("New dictionary =", dict1)
print()


# 3. Change the value of 'City' to 'Kathmandu'.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur', 'Occupation': 'Engineer'}
print("Q3")
print("Existing dictionary =", dict1)
dict1['City'] = 'Kathmandu'
print("Modified dictionary =", dict1)
print()


# 4. Remove the key 'Age' from the dictionary.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur', 'Occupation': 'Engineer'}
print("Q4")
print("Existing dictionary =", dict1)
del dict1['Age']
print("Modified dictionary =", dict1)
print()


# 5. Iterate through the dictionary and print all keys and values.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur'}
print("Q5")
for k, v in dict1.items():
    print(f"Key = {k}, Value = {v}")
print()


# 6. Get all keys, values and items.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur'}
print("Q6")

print("Keys:")
for k in dict1.keys():
    print(k)

print("\nValues:")
for v in dict1.values():
    print(v)

print("\nItems:")
for item in dict1.items():
    print(item)
print()


# 7. Check whether the key 'email' exists.

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur'}
print("Q7")

if 'email' not in dict1:
    print("Key not found")
else:
    print("Key found")
print()


# 8. Merge two dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print("Q8")
dict1.update(dict2)
print(dict1)
print("The value of key 'b' is overwritten by dict2.")
print()


# 9. Convert a list of tuples into a dictionary.

print("Q9")

lists = [('a', 1), ('b', 2), ('c', 3)]
d = dict(lists)

print(d)
print()


# 10. Use get() method.

print("Q10")

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur'}
print(dict1.get('Age', 'Key not available'))
print()


# 11. Find all keys having the given value.

print("Q11")

dict1 = {
    'Brazil': 5,
    'Germany': 4,
    'Italy': 4,
    'Argentina': 3,
    'France': 2,
    'Uruguay': 2,
    'Spain': 1,
    'England': 1
}

value = 4
keys = []

for k, v in dict1.items():
    if v == value:
        keys.append(k)

print(keys)
print()


# 12. Sort dictionary by keys.

print("Q12")

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur', 'Occupation': 'Engineer'}

sorted_keys = sorted(dict1.items(), key=lambda t: t[0])

print(sorted_keys)
print()


# 13. Sort dictionary by values.

print("Q13")

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur', 'Occupation': 'Engineer'}

sorted_values = sorted(dict1.items(), key=lambda t: t[1])

print(sorted_values)
print()


# 14. Check whether a given key exists.

print("Q14")

dict1 = {'Name': 'Hari', 'Age': '29', 'City': 'Bhaktapur', 'Occupation': 'Engineer'}

key1 = 'Age'
key2 = 'Salary'

if key1 in dict1:
    print(f"{key1} exists.")
else:
    print(f"{key1} does not exist.")

if key2 in dict1:
    print(f"{key2} exists.")
else:
    print(f"{key2} does not exist.")

print()


# 15. Sort lists inside a dictionary.

print("Q15")

num_dict = {
    'n1': [2, 3, 1],
    'n2': [5, 1, 2],
    'n3': [3, 2, 4]
}

for key in num_dict:
    num_dict[key] = sorted(num_dict[key])

print(num_dict)
print()


# 16. Reverse dictionary order.

print("Q16")

d = {'a': 1, 'b': 2, 'c': 3}

print("Original =", d)

items = list(d.items())
items.reverse()

new_d = dict(items)

print("Reversed =", new_d)
print()


# 17. Count characters in a string.

print("Q17")

sample = input("Enter a string: ")

count = {}

for ch in sample:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)
print()


# 18. Find top 3 highest values.

print("Q18")

d = {'a': 10, 'b': 45, 'c': 23, 'd': 99, 'e': 5, 'f': 67}

top3 = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

for key, value in top3:
    print(key, value)

print()


# 19. Remove empty items.

print("Q19")

d = {'c1': 'Red', 'c2': 'Green', 'c3': None}

new_d = {k: v for k, v in d.items() if v is not None}

print("Original =", d)
print("New =", new_d)
print()


# 20. Find specified number of maximum values.

print("Q20")

d = {
    'a': 5,
    'b': 14,
    'c': 32,
    'd': 35,
    'e': 24,
    'f': 100,
    'g': 57,
    'h': 8,
    'i': 100
}

n = int(input("Enter number of maximum values: "))

temp = d.copy()
result = []

for _ in range(n):
    max_key = max(temp, key=temp.get)
    result.append(max_key)
    temp.pop(max_key)

print(result)
print()


# 21. Find keys with maximum and minimum values.

print("Q21")

d = {'a': 5, 'b': 14, 'c': 32, 'd': 35}

max_key = max(d, key=d.get)
min_key = min(d, key=d.get)

print("Maximum and minimum key values:", (max_key, min_key))