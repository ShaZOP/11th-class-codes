#list practical
mylist = []
#creating the elements in list and list elements
n = int(input("Enter number of elements in list"))
for x in range(n):
    num = int(input("Value : "))
    mylist.append(num)
#seperating odd list and even list
odd = []
even = []
for i in range(0,len(mylist)):
    if i %2 == 0 :
        even.append(mylist[i])
    else:
        odd.append(mylist[i])
result = odd + even
print("The list is : ",str(result))
    
