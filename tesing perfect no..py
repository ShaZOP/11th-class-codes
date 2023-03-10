n = int(input("Enter a value"))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum= sum+i
if sum == n:
    print(n,"is a perfect no.")
else:
    print(n,"not prft no.")
