**Decorators, Iterators, and Generators in Python**

---

# **1. Decorators in Python**
Decorators are a powerful feature in Python that allows modifying functions or methods without changing their actual code. 
They wrap another function and can be used for logging, authentication, timing functions, and more.

# **Using a Basic Decorator**
```python


def my_decorator(func):
    def wrapper():
        print("Something before the function execution")
        func()
        print("Something after the function execution")
    return wrapper


@my_decorator
def say_hello():
    print("Hello, World!")


say_hello()
```
# **Output:**
```
Something before the function execution
Hello, World!
Something after the function execution
```

# **Decorator with Arguments**
```python


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
```

---
# **2. Iterators in Python**
An ** iterator ** is an object that contains a countable number of values and can be traversed using the `next()` function. 
Any object with the methods `__iter__()` and `__next__()` is an iterator.

# **Creating an Iterator**
```python


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Iterator object itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


counter = Counter(1, 5)
for num in counter:
    print(num)
```
# **Output:**
```
1
2
3
4
5
```

---
# **3. Generators in Python**
A ** generator ** is a simpler way to create iterators using functions and the `yield ` keyword.

# **Basic Generator Example**
```python


counter = Counter(5, 1)
for num in counter:
    print(num)
a = 4

for value in my_generator():
    print(a, "x", value, "=", a * value)
```
# **Output:**
```
1
2
3
```

# **Using Generators for Large Data**
```python


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(5):
    print(num)
```
# **Output:**
```
0
1
1
2
3
```

---
# **4. Summary**
| Concept | Description |
|------------- | -------------|
| **Decorators ** | Modify functions dynamically without changing their code. |
| **Iterators ** | Objects that allow iteration using `next()` and `__iter__()`. |
| **Generators ** | Functions that yield values and maintain state for efficient looping. |
