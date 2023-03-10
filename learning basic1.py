#stars
star = int(input("enter the number"))
for x in range(1,star*'*'):
    for j in range(1,x*'*'):
        print(j,end = '')
    print()   
