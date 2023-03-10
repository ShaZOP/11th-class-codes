#largest element in the given list
list1 =[]
n = int(input("Enter the no. of elements"))
for x in range(n):
    num = int(input("Enter the number"))
    list1.append(num)
print("The largest number is ",max(list1))    
