tuple1 = ()
num = int(input("Enter the number of elements"))
for x in range(num):
    n = int(input("Enter the values"))
tuple1 = tuple1 + n    
search = int(input("Enter the element to search"))
ind = n.index(search)
print("Position of element",ind)
