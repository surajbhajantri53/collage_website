# **Functions in Python**
A ** function ** is a block of reusable code that performs a specific task.

# **1️⃣ Types of Functions in Python**
1. ** Built-in Functions ** (Predefined by Python)
2. ** User-defined Functions ** (Created by the user)

---

# **2️⃣ Built-in Functions**
Python provides many ** built-in functions ** that can be used directly.

# **Example of Built-in Functions**
```python
print(len("Hello"))  # len() gives the length of a string
print(max(10, 5, 8))  # max() returns the largest number
print(sum([1, 2, 3]))  # sum() adds all numbers in a list
```

---

# **3️⃣ User-defined Functions**
A ** user-defined function ** is created using the `def ` keyword.

# **Example of a Simple Function**
```python


def greet():
    print("Hello! Welcome to Python.")


# Calling the function
greet()
```
# **Output:**
```
Hello! Welcome to Python.
```
---

# **4️⃣ Parameter Passing in Functions**
Functions can take ** parameters ** (inputs) to process data.

# **Example: Function with Parameters**
```python


def add(a, b):
    return a + b


# Calling the function with arguments
result = add(5, 7)
print("Sum:", result)
```
# **Output:**
```
Sum: 12
```

---

# **5️⃣ Parameter Passing Mechanisms in Python**
Python ** passes parameters ** to functions in two ways:
1. ** Pass by Value(Immutable Data Types)**
2. ** Pass by Reference(Mutable Data Types)**

# **📌 Pass by Value (Immutable Types)**
When we pass **immutable ** types(`int`, `float`, `str`, `tuple`), a ** copy ** is created.

```python


def modify(x):
    x = 10  # Changing value inside function
    print("Inside function:", x)


a = 5
modify(a)
print("Outside function:", a)  # Original value remains unchanged
```
# **Output:**
```
Inside function: 10
Outside function: 5
```

🔹 `x` inside the function is **a copy**, so `a` remains `5`.

---

# **📌 Pass by Reference (Mutable Types)**
When we pass **mutable ** types(`list`, `dict`), changes affect the original object.

```python


def modify_list(lst):
    lst.append(4)  # Modifying the list


numbers = [1, 2, 3]
modify_list(numbers)
print("Outside function:", numbers)  # List is modified
```
# **Output:**
```
Outside function: [1, 2, 3, 4]
```
🔹 The original `numbers` list is modified because ** lists are mutable**.

---

# **Summary Table**
| Concept | Explanation |
|------------------------- | ------------|
| **Built-in Functions ** | Predefined functions like `print()`, `len()`, `max()` |
| **User-defined Functions ** | Functions created using `def ` keyword |
| **Pass by Value ** | Immutable types(`int`, `float`, `str`, `tuple`) are copied |
| **Pass by Reference ** | Mutable types(`list`, `dict`) can be modified |


Example

# **💡 Exercise: Student Score Management System**
Create a ** function-based Python program ** to manage student scores.

# **🔹 Task Steps:**
1. ** Create a function ** `calculate_average(scores)` that takes a ** list of scores ** and returns the average.
2. ** Create another function ** `update_scores(scores, new_score)` to add a new score to the list.
3. ** Demonstrate pass by value and pass by reference ** by:
    - Passing an integer(immutable) to a function.
    - Passing a list(mutable) to a function.

---

# **✅ Starter Code (You Complete It)**
```python
# Function to calculate the average score (Pass by Value)


def calculate_average(scores):
    return sum(scores) / len(scores)

# Function to add a new score to the list (Pass by Reference)


def update_scores(scores, new_score):
    scores.append(new_score)  # Modifies the original list


# Step 1: Create a list of student scores
student_scores = [85, 90, 78]

# Step 2: Calculate average score
average = calculate_average(student_scores)
print("Initial Average Score:", average)

# Step 3: Add a new score
update_scores(student_scores, 95)

# Step 4: Recalculate average after updating the list
new_average = calculate_average(student_scores)
print("Updated Average Score:", new_average)

# Step 5: Check if list is modified (Pass by Reference effect)
print("Updated Student Scores:", student_scores)
```

---

# **🔹 Expected Output:**
```
Initial Average Score: 84.33
Updated Average Score: 87.0
Updated Student Scores: [85, 90, 78, 95]
```

---

# **✅ What You Will Learn**
✔ **Using Functions**
✔ **Passing Lists(Mutable) by Reference**
✔ **Passing Values(Immutable) by Copy**

Try running the code and modifying it! 🚀 Let me know if you need hints. 🔥
