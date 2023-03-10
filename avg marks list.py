list1 = []
sum1 = 0
n = int(input("Enter the no.s of subjects : "))
for x in range(0,n):
    mark = int(input("Enter the mark"))
    list1.append(mark)
    total = sum(list1)
    avg = total/n
print("The total marks is : ",total)
print("The average marks is : ",avg)












