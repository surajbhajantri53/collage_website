from mathOp import *

a=int(input("Enter First value : "))
b=int(input("Enter Second Value : "))
addObj=addition(a,b)
subObj = subtraction(a,b)
mulObj = multiplication(a,b)

def main():
    print("Addition of Two numbers : ",addObj.add())
    print("Subtraction of Two numbers : ",subObj.sub())
    print("Multiplication of Two Numbers : ",mulObj.mul())
    
main()