#       LISTS, DICTIONARY AND TUPLE IN PYTHON

# ------------------------------------------------------------

# LIST FUNCTIONS IN USE IN PYTHON 3.7

# list declaration
lists = ['nitin','yash','rachna','anji','somi','rhea']
print("The whole list is",lists)

# adding a value in list
lists.append('shiv')
print("After applying append operation:",lists)

# counting the position of particular item/value in list
lists.count('rachna')
print("After applying count operation:",lists)

# adding a value alphabet wise
# here , it'll add ['a','k','s','h','a','y']
lists.extend('akshay')
print("After applying count operation:",lists)

# to find the index of particular value in list
lists.index('yash')
print("After applying index operation:",lists)

# to insert a value in particular index of list
lists.insert(3,'veena')
print("After applying ")

# deletes an item in list if index is known
lists.pop(5)

# deletes an item in list if value is known 
lists.remove('shiv')

# reverses a list 
lists.reverse()

# if all value satisfies the condition given before for loop then it'll print the same
if all([i == 'kumar' for i in lists]):
    print("Not a single item with 'kumar' is present")

# if any value satisfies the condition given before for loop then it'll print the same
if any([i == 'kumar' for i in lists]):
    print("Not all single item with 'kumar' is present")

# prints the values of items along with their index numbers of list
for v in enumerate(lists):
    print(v)

# deletes the whole list contents & clears it
lists.clear()

# ------------------------------------------------------------

# DICTIONARY FUNCTIONS IN USE IN PYTHON 3.7

# declaring dictionary [key:value]
dic = {
	'nitin':1,
	'yash':2,
	'anji':3,
	'rachna':4,
	'rhea':5
	}

# getting value of key 'yash'
dic.get('yash')

dic.items()

dic.keys()

# deletes last key:value pair from dictionary
dic.pop('rhea')

# same as pop
dic.popitem()

# set value default which'll show every time when you want to print
dic.setdefault(2) # or dic.setdefault('yash')

# update whole dictionary
dic.update()

# display values in dictionary only
dic.values()

#clears the dictionary
dic.clear()

# ------------------------------------------------------------

# TUPLES FUNCTIONS IN USE IN PYTHON 3.7

# declaring tuple
tup = (1,2,3,4,1,6,7,8,9)

# counts the number of value in the tuple
tup.count(1)

# display the index number of value of tuple
tup.index(3)


# ------------------------------------------------------------
