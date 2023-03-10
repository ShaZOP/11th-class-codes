#sum of factorials
n = int(input("Enter a value"))
s = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact*j
    s = s+fact
    print(str(i) + "!" , end = '')
    if i!=n:
        print("+",end = '')
print(" = " + str(s))        
