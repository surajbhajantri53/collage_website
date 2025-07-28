#  Parameter Passing Mechanism
# 1 Positional Argument

def add(a,b):
    return a+b
print(add(10,20))

# 2 Default Arguments

def greet(name="user"):
    print("Hello ",name," !")
greet()
greet("anusuya")

# 3 Keyword Argument

def describe_pet(animal,name):
    print(f"I have a {animal} named {name}")
describe_pet(name="Buddy",animal="dog")

# 4 Variable-Length Argument
# using *args (Non-keyword Arguments)

def sum_number(*numbers):
    return sum(numbers)

print(sum_number(10,20,30,40))

# using **kwargs (keyword Arguments)

def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
display_info(name="Ali",age=25,city="Bengaluru")