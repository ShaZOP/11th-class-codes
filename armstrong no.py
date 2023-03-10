num = int(input("Enter a value"))
x=num
y = num
count = 0
while num>0:
    r=num%10
    count = count+1
    num=num//10
sum = 0
while x>0:
    r = x%10
    sum = sum +(r**count)
    x = x//10
if sum == y:
    print(y,"is an armstrong number")
else:
    print(y,"is not a armstrong number")
