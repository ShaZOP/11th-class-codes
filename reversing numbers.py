#reversing number
num = int(input("Enter a number"))
sum = 0
while(num>0):
    sum =(num%10)+sum*10
    num=num//10
print("The reversed no. is : ",sum)
