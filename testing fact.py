#factorial#
factorial = 1#always give the value 1(If we give 0 any number multiplied by 0 is 0 u will get error)
num = int(input("Enter a value"))
for i in range(1,num+1):
    factorial = factorial *i
print(num,"!",' = ',factorial)    
