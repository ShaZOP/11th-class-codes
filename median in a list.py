#taking median in a list
list1 = []
index1 = len(list1)
n = int(input("Enter the number of elements"))
for x in range (n):
    val = int(input("Enter the value"))
list1.append(val)
odd = n+1
if (n% 2 == 0):
    print("The median is ",n/2)
else:
    print("The median is : " ,odd/2)
    
