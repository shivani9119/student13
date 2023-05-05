'''#LIST
mylst = ["1.1.1.1", "2.2.2.2", '3.3.3.3']
print('List is ordered and allows duplicate hence resulted in:',mylst)
print(len(mylst)) #finding length of list
print(type(mylst)) #finding type of datatype
mylst[2] = "145.78.5.6"
print('changed the element at index 2',mylst)
mylst.append(['23.46.78.56'])#append method
print('output after appending is:',mylst)
mylst.extend(['3.6.8.6'])#extend method
print('output after extending is:',mylst)
mylst.insert(2,'1.1.1.1') #Insert method
print('output after inserting an element at specified position is:',mylst)
mylst.remove('1.1.1.1')
print('output after removing element mentioned is:',mylst)
mylst.pop()#pop operation without specifying index
print(mylst)
mylst.pop(2)#pop operation with specifying index
print(mylst)
mylst.clear()#clear method
print(mylst)
mylst = ['a','b','c','b','a']#getting the index
index_pos = mylst.index('a')
print(index_pos)
count_oper = mylst.count('b')#count method
print(count_oper)
mylst.sort()#sort method
print(mylst)
mylst.reverse()#reverse method
print(mylst)

#SET
set_data = {"1.1.1.1", "2.2.2.2", '3.3.3.3'}
print('\nSet is not ordered format hence resulted in:',set_data)

#DICTIONARY
dict_data =  {"ip": "1.1.1.1","username": "admin","password": "cisco"}
print(dict_data["password"])# getting the value at specified index
dict_data =  {"ip": "1.1.1.1","username": "admin","password": "cisco","username": "shivani"}# Dictionary doesn't allow duplicates
print(dict_data)
dict_data["ip"] = "1.2.3.4"#changing the value of key 'ip'
print(dict_data)
val = dict_data['ip']#Accessing a value by key
print(val)
dict_data['mac'] = '00-B0-D0-63-C2-26'#Adding or updating a key-value pair
print(dict_data)
if 'username' in dict_data:#checking if key is in dicttionary
    print('key found')
del dict_data['mac']#removing a key value pair
print(dict_data)
val = dict_data.get('ip1','3.3.3.3')#Getting value using get
print(val)
print(len(dict_data))
for key in dict_data.keys():#Iterating over keys
    print(key)
for val in dict_data.values():#Iterating over values
    print(val)
for key,val in dict_data.items():#Iterating over key, value pairs
    print(key,val)
other_dict = {"mac": "00-B0-D0-63-C2-26"}
dict_data.update(other_dict)#merging two dictionaries using merge
print(dict_data)
x = dict_data.copy()#copy method
print(x)
key_data = ('key1', 'key2', 'key3')
y = 'value'
new_dict = dict.fromkeys(key_data, y)
print(new_dict)
print(dict_data.clear())#clear method'''


#Operators
x = int(input('enter the data for a:'))
y = int(input('enter the data for b:'))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x & y)
print(x > 3 and x < 10)
print(x < 3 or y > 10)
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << y)
print(x >> y)
a=6
print(a)
a += 3
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)

