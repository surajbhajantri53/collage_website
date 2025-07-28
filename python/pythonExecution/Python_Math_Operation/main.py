from mathOperation.add import add
from mathOperation.sub import sub
from mathOperation.mul import mul
from mathOperation.div import div

a=int(input("Enter the value of a: "))
b=int(input("Enter the vLUE OF B: "))

def main(a,b):
    print("addition of Two numbers: ",add(a,b))
    print("The subtraction of Two Numbers: ",sub(a,b))
    print("The Multiplication of Two numbers: ",mul(a,b))
    print("The Division Of two numbers: ",div(a,b))
    
main(a,b)