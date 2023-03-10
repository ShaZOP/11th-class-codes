#inputing a list and searching the element from them.
list1= []
n = int(input("Enter how many numbers : "))
for x in range(0,n):
    ele = int(input("Enter a number"))
    list1.append(ele)
search = int(input("enter a number to search"))              
if search in list1:
    print("Yes,Element is there in the list")
    print("The number of times",search,"in list",list1.count(search))
    print("The number is placed on index ",list1.index(search))

              
              
              
