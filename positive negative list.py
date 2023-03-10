list1 = []
list2 = []
list3 = []
n = int(input("Enter how many numbers u are going to give"))
for x in range(n):
    num = int(input("Enter the numbers : "))
list1.append(num)
for j in range(0,num):
    if j >= 0:
        list2.append(list1[j])
    else:
         list3.append(list1[j])
print("The list u given",list1)
print("Postive list",list2)
print("Negative list ",list3)
