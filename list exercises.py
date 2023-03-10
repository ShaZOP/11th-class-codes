list1 = []
n = int(input("Enter how many marks in"))
for x in range(0,n):
    marks = int(input("enter the marks in sub"))
    list1.append(marks)
    sum1 = sum(list1)
    avg = sum1/n
print("The total is : ",sum1)    
print("The average value is : ",avg)    
    
    
