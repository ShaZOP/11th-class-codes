#building a calculator
num1 = int(input("Enter the first number"))
num2 = int(input("enter the 2nd number"))
opp = str(input("choose a opperator +,-,/,*"))
if (opp == '+'):
    result = num1+num2
if (opp == "-"):
    if num1>num2:
        result = num1-num2
    else:
        result = num2-num1
if (opp == "*"):
    result = num1*num2
if(opp == '/'):
    if (num1 == 0):
        print("We cant divide with 0")
    elif (num2 == 0):
        print("We cant divide with 0")
    else:
        result = num1/num2
print("The result is : ",result)        

    
    
