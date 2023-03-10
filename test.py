#inputing a list,times repeated and index position
list1 = []
n = int(input("Enter no. of elements")) #no. of elements u are going  to write in the  list
for x in range(0,n):
    ele = int(input("Enter the number"))
    list1.append(ele)
search = int(input("Enter what u want to search"))    
if search in list1:
    print(search,"is there in the list")
    print("times is ",search,"there in the list",list1.count(search))
    print(search,"is in index",list1.index(search))
