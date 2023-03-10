#dictionary program 10.5
dict1 = {1:'one',3:'three',5:'five',7:'seven',9:'nine'}
keys = print(dict1.keys())
values = print(dict1.values())
items = print(dict1.items())
if 7 in dict1:
    print("Present")
else:
    print("Not")
length = print(len(dict1))
if 2 in dict1:
    print("yes")
else:
    print("no")
print(dict1.get(9))
del dict1[9]
print(dict1)
dict1.popitem()
print(dict1)
y = dict1.copy()
print(y)

