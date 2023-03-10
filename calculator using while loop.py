#building a calculator with loops
num1 = int(input("Enter 1st value"))
num2 = int(input("Enter 2nd value"))
opp = input("Choose 1 for add,2 for subraction,3 for multiplication and 4 for division")
while True:
    if (opp == 1):
        print("Sum of ",num1,'and',num2," = ",num1+num2)
    elif opp == 2:
        print("Subraction of ",num1,'and',num2,' = ',num1-num2)
    elif opp == 3:
        print("Multiplication of ",num1,'and',num2,' = ',num1*num2)
    elif opp == 4:
        print("Division of ",num1,'and',num2,' = ',num1/num2)
    break
    
        
        
