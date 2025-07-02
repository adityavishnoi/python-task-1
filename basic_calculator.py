def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        return a/b
    
print("\t Welcome to Basic Calculator \n")    
print("1 for Addition:")
print("2 for Subtraction:")
print("3 for Multiplication:")
print("4 for Divsion:")
choice=int(input("enter your choice : "))
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

if(choice==1):
    print(f" result : {add(num1,num2)}")
elif(choice==2):
    print(f" result : {sub(num1,num2)}")    
elif(choice==3):
    print(f" result : {multi(num1,num2)}")
elif(choice==4):
    print(f" result : {div(num1,num2)}")