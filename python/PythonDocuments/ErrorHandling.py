# **1️⃣ File Handling in Python**
File Handling is used to ** read**, **write**, **append**, and **modify ** files in Python.

# **🔹 Example: Writing & Reading a File**
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
```
✅ **Explanation: **
- `"w"` mode opens the file for writing(creates it if it doesn’t exist).
- `"r"` mode reads the file content.
- `with open(...)` ensures the file is closed automatically.

---

# **2️⃣ Error Handling (Exception Handling) in Python**
Python provides `try -except ` blocks to handle runtime errors.

# **🔹 Example: Handling Division by Zero**
```python
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input! Please enter numbers.")
finally:
    print("Execution completed.")
```
✅ **Explanation: **
- `try ` block contains code that may cause an error.
- `except ZeroDivisionError` catches division by zero errors.
- `except ValueError` catches invalid inputs(like entering text instead of numbers).
- `finally ` runs whether an exception occurs or not .

---


## 🧮 NumPy: Numerical Python

**NumPy** is a Python library used for working with arrays. It also has functions for working in the domain of linear algebra, Fourier transform, and matrices. 

### 🔧 Key Features:

- **Efficient Arrays**: NumPy provides the `ndarray` object, which is a fast and space-efficient multidimensional array.
- **Mathematical Functions**: It offers a wide range of mathematical operations, including linear algebra, statistical operations, and more.
- **Broadcasting**: Allows arithmetic operations on arrays of different shapes.
- **Integration**: Serves as the foundation for many other libraries, including Pandas.

### 🧪 Example:

```python
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Perform element-wise operations
squared = arr ** 2
print(squared)  # Output: [ 1  4  9 16 25]
```

---

## 📊 Pandas: Data Analysis Library

**Pandas** is a Python library used to analyze data. 

### 🔧 Key Features:

- **Data Structures**: Provides two primary data structures:
  - `Series`: One-dimensional labeled array.
  - `DataFrame`: Two-dimensional labeled data structure with columns of potentially different types.
- **Data Handling**: Simplifies data cleaning, manipulation, and analysis.
- **File I/O**: Supports reading from and writing to various file formats like CSV, Excel, JSON, etc.
- **Integration with NumPy**: Built on top of NumPy, allowing for efficient numerical operations.

### 🧪 Example:

```python
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Access data
print(df['Name'])       # Output: Series of names
print(df.iloc[0])       # Output: First row as a Series
```

---

## 🔍 Differences Between NumPy and Pandas

| Feature             | NumPy                              | Pandas                                 |
|---------------------|------------------------------------|----------------------------------------|
| Primary Structure   | ndarray (n-dimensional array)      | Series (1D), DataFrame (2D)            |
| Data Handling       | Numerical data                     | Heterogeneous data (numeric, string)   |
| Indexing            | Integer-based                      | Label-based and integer-based          |
| Use Case            | Mathematical computations          | Data analysis and manipulation         |
| Built On            | Low-level operations               | Built on top of NumPy                  |

---

## 📚 Recommended Resources

- **W3Schools Pandas Tutorial**:  ([Pandas Tutorial - W3Schools](https://www.w3schools.com/python/pandas/default.asp?utm_source=chatgpt.com))
- **W3Schools NumPy Introduction**:  ([Introduction to NumPy - W3Schools](https://www.w3schools.com/python/numpy/numpy_intro.asp?utm_source=chatgpt.com))
- **10 Minutes to Pandas**:  ([10 minutes to pandas — pandas 2.2.3 documentation](https://pandas.pydata.org/docs/user_guide/10min.html?utm_source=chatgpt.com))

---

Would you like a beginner-friendly mini project using NumPy and Pandas to practice these concepts? 