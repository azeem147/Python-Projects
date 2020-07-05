# Uses key value pair instead of index to store various data types
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat["size"])
# In dictionary order doesn't matter unlike list
print(list(myCat.keys()))
print(list(myCat.items()))
print(list(myCat.values()))
# Using for loop
for k in myCat.keys():
    print(k)
for v in myCat.values():
    print(v)
for i in myCat.items():
    print(i)
for k, v in myCat.items():
    print(k, v)
# checking if something exists in dictionary
print('size' in myCat.keys())
print('fat' in myCat.values())
# Using get method to avoid error
print(myCat.get('age', 'does not exist'))
print(myCat.get('size', 'does not exist'))
# setdefault method allows to enter a new value pair if the key doesn't exist
