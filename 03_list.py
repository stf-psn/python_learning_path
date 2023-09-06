empty_list = [];
# creazione di una lista

list_str = ['a','d','c'];
print(type(list_str))
# output class list

# print(list_str[4])
# index out of range

print((list_str[2]))
# output is c

print(list_str[-1])
# output is c

print(len(list_str))
# output is 3

list_str.sort()
print(list_str)
# output is a,c,d

list_str.append('f')
print(list_str)
#output a,c,d,f

list_str.insert(2, 'h')
print(list_str)
# output a,c,h,d,f

list_str.extend(['x', 'y', 'z'])
print(list_str)
# output a,c,h,d,f,x,y,z