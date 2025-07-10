Here’s a structured explanation of **"Introduction to JavaScript, History, and Uses"** to help you teach your students effectively.

---

## **1. Introduction to JavaScript**

JavaScript (JS) is a **high-level, interpreted programming language** primarily used for web development. It allows developers to create **interactive and dynamic** web pages.

### **Key Features of JavaScript**

- **Client-Side Execution**: Runs in the browser, making websites interactive.
- **Dynamically Typed**: No need to specify variable types (e.g., `var x = 10;`).
- **Prototype-Based Object-Oriented**: Uses prototypes instead of traditional classes (though ES6 introduced `class`).
- **Event-Driven**: Responds to user actions like clicks, keyboard inputs, etc.
- **Asynchronous Programming**: Uses callbacks, promises, and async/await for non-blocking code execution.

### **Hello World Example**

```html
<!DOCTYPE html>
<html>
  <body>
    <h2>JavaScript Example</h2>
    <button onclick="greet()">Click Me</button>
    <script>
      function greet() {
        alert("Hello, Welcome to JavaScript!");
      }
    </script>
  </body>
</html>
```

---

## **2. History of JavaScript**

JavaScript was created by **Brendan Eich** in 1995 while working at Netscape. It has evolved over time into a powerful language used across different platforms.

### **Timeline of JavaScript Evolution**

- **1995**: JavaScript (originally called Mocha, then LiveScript) was developed at Netscape.
- **1996**: Microsoft introduced JScript (Internet Explorer’s version of JS).
- **1997**: ECMAScript (ES) was standardized by ECMA International.
- **2009**: ES5 introduced features like `JSON.parse()`, `strict mode`.
- **2015 (ES6/ES2015)**: Major update with `let`, `const`, `arrow functions`, `classes`, and `modules`.
- **Present**: JavaScript continues to evolve with modern features like `optional chaining`, `async/await improvements`, and `bigint`.

---

## **3. Uses of JavaScript**

JavaScript is a **versatile** language used for multiple purposes beyond just web development.

### **1. Web Development (Front-end & Back-end)**

- **Front-end**: JavaScript powers **interactive web pages** (DOM Manipulation, animations, dynamic content).
  - Libraries: **jQuery**
  - Frameworks: **React.js, Angular, Vue.js**
- **Back-end**: Node.js enables JavaScript to run on servers.
  - Frameworks: **Express.js, Nest.js**

### **2. Mobile App Development**

- JavaScript can be used to create **mobile apps** using frameworks like:
  - **React Native** (for Android & iOS)
  - **Ionic** (hybrid apps)

### **3. Game Development**

- **Phaser.js** and **Three.js** help build browser-based and 3D games.

### **4. Machine Learning & AI**

- Libraries like **TensorFlow.js** allow JavaScript to run AI models directly in the browser.

### **5. Internet of Things (IoT)**

- JavaScript can control hardware devices using **Johnny-Five.js**.

---

## **Conclusion**

JavaScript is a powerful and widely used language in web development, mobile apps, gaming, and even AI. Understanding its **history and uses** helps students appreciate its importance in modern technology.

## **Types of JavaScript**

JavaScript itself is a **single language**, but it can be categorized based on how and where it is used. Here are the key types:

---

### **1. Client-Side JavaScript (Browser JavaScript)**

- Runs directly in the **web browser**.
- Used for **DOM manipulation, animations, form validation, and dynamic content**.
- **Example:**
  ```html
  <button onclick="greet()">Click Me</button>
  <script>
    function greet() {
      alert("Hello, this is Client-Side JavaScript!");
    }
  </script>
  ```
- Libraries: **jQuery**, **React.js**, **Vue.js**, **Angular**.

---

### **2. Server-Side JavaScript**

- Runs **outside the browser** on a server.
- Uses **Node.js** to handle back-end operations, databases, and APIs.
- **Example (Node.js Express Server):**

  ```javascript
  const express = require("express");
  const app = express();

  app.get("/", (req, res) => {
    res.send("Hello from Server-Side JavaScript!");
  });

  app.listen(3000, () => console.log("Server running on port 3000"));
  ```

- Frameworks: **Express.js, Nest.js, Koa.js**.

---

### **3. Asynchronous JavaScript**

- Handles **non-blocking operations** using:
  - **Callbacks**
  - **Promises**
  - **Async/Await**
- **Example (Using Fetch API):**
  ```javascript
  async function fetchData() {
    let response = await fetch("https://api.example.com/data");
    let data = await response.json();
    console.log(data);
  }
  fetchData();
  ```

---

### **4. Object-Oriented JavaScript (OOP in JS)**

- JavaScript supports **OOP concepts** like **classes, objects, inheritance**.
- **Example:**

  ```javascript
  class Car {
    constructor(name) {
      this.name = name;
    }
    start() {
      console.log(`${this.name} is starting...`);
    }
  }

  let myCar = new Car("Toyota");
  myCar.start();
  ```

---

### **5. Functional JavaScript**

- JavaScript allows **functional programming** (FP) with functions as **first-class citizens**.
- **Example (Higher-Order Function):**

  ```javascript
  function greet(name) {
    return () => console.log(`Hello, ${name}!`);
  }

  let sayHello = greet("John");
  sayHello();
  ```

---

## **Conclusion**

JavaScript is a flexible language that can be used on both the **client-side and server-side**, supports **asynchronous operations**, and follows **OOP & Functional Programming** paradigms.

## **Brief Introduction to JavaScript Frameworks**

### **What is a JavaScript Framework?**

A **JavaScript framework** is a collection of pre-written JavaScript code that provides a **structured way** to build web applications efficiently. Instead of writing everything from scratch, developers use frameworks to **speed up development, maintain code quality, and follow best practices**.

---

## **Popular JavaScript Frameworks & Libraries**

JavaScript frameworks are mainly classified into **front-end, back-end, and full-stack** frameworks.

### **1. Front-End Frameworks (UI Development)**

These frameworks help build **interactive user interfaces** for web applications.

#### **a) React.js** (Library, but often called a framework)

- Developed by **Facebook (Meta)**
- Component-based architecture
- Virtual DOM for better performance
- Used by Facebook, Instagram, Airbnb

**Example (React Component)**:

```jsx
import React from "react";

function Hello() {
  return <h1>Hello, React!</h1>;
}

export default Hello;
```

---

#### **b) Angular** (Full-fledged Framework)

- Developed by **Google**
- Uses **TypeScript** instead of plain JavaScript
- Supports two-way data binding
- Used by Google, Microsoft, IBM

**Example (Angular Component - TypeScript)**:

```typescript
import { Component } from "@angular/core";

@Component({
  selector: "app-hello",
  template: "<h1>Hello, Angular!</h1>",
})
export class HelloComponent {}
```

---

#### **c) Vue.js**

- Lightweight framework
- Combines features of React and Angular
- Used by Alibaba, Xiaomi

**Example (Vue Component)**:

```vue
<template>
  <h1>Hello, Vue!</h1>
</template>

<script>
export default {
  name: "HelloVue",
};
</script>
```

---

### **2. Back-End Frameworks (Server-Side Development)**

These frameworks help build the **backend (server-side logic, APIs, database handling)**.

#### **a) Node.js** (Runtime, Not a Framework)

- Uses **JavaScript on the server**
- Non-blocking, event-driven architecture
- Used by Netflix, PayPal, LinkedIn

**Example (Node.js Express Server)**:

```javascript
const express = require("express");
const app = express();

app.get("/", (req, res) => res.send("Hello from Express.js!"));

app.listen(3000, () => console.log("Server running on port 3000"));
```

---

#### **b) Express.js** (Minimalist Backend Framework)

- Built on **Node.js**
- Fast, flexible, and simple
- Used for REST API development

---

### **3. Full-Stack Frameworks**

These frameworks support both **front-end and back-end** development.

#### **a) Next.js** (React-based Full-Stack Framework)

- Server-side rendering (SSR) for faster performance
- API routes for backend functionality
- Used by Netflix, Uber, TikTok

---

#### **b) Nuxt.js** (Vue-based Full-Stack Framework)

- Similar to Next.js but for Vue.js

---

## **Conclusion**

JavaScript frameworks simplify web development by providing ready-to-use structures. **React, Angular, and Vue.js** dominate the front-end, while **Node.js, Express.js, and Next.js** lead in back-end and full-stack development.

## **JavaScript Syntax**

### **What is Syntax?**

Syntax refers to the **rules and structure** that define how JavaScript code should be written and interpreted. Understanding JavaScript syntax is crucial to writing functional programs.

---

## **1. Variables (var, let, const)**

Variables store data values.

```javascript
var name = "John"; // Old way (Avoid using var)
let age = 25; // Preferred for changeable values
const PI = 3.1416; // Constant value (cannot be changed)
```

- `let` is block-scoped, while `var` is function-scoped.
- `const` cannot be reassigned after initialization.

---

## **2. Data Types**

JavaScript supports **dynamic typing**, meaning variables do not require explicit type declarations.

```javascript
let str = "Hello"; // String
let num = 42; // Number
let isActive = true; // Boolean
let items = [1, 2, 3]; // Array
let person = { name: "John", age: 30 }; // Object
```

---

## **3. Operators**

JavaScript has **arithmetic, comparison, logical, and assignment operators**.

```javascript
let a = 10;
let b = 5;

console.log(a + b); // Addition (15)
console.log(a > b); // Comparison (true)
console.log(a == "10"); // Loose equality (true)
console.log(a === "10"); // Strict equality (false)
console.log(a && b); // Logical AND (5)
```

---

## **4. Conditional Statements**

Used to execute different code blocks based on conditions.

```javascript
let num = 10;

if (num > 0) {
  console.log("Positive number");
} else if (num < 0) {
  console.log("Negative number");
} else {
  console.log("Zero");
}
```

---

## **5. Loops (for, while, do-while)**

Loops execute a block of code multiple times.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i); // Prints 0 to 4
}

let x = 1;
while (x <= 3) {
  console.log(x); // Prints 1 to 3
  x++;
}
```

---

## **6. Functions**

Functions define reusable code blocks.

```javascript
function greet(name) {
  return "Hello, " + name + "!";
}

console.log(greet("Alice")); // Hello, Alice!
```

**Arrow Function (Modern JavaScript)**

```javascript
const greet = (name) => `Hello, ${name}!`;
console.log(greet("Bob")); // Hello, Bob!
```

---

## **7. Objects & Arrays**

JavaScript follows an **object-oriented approach**.

```javascript
let car = {
  brand: "Toyota",
  model: "Camry",
  year: 2022,
};

console.log(car.brand); // Toyota
console.log(car["model"]); // Camry
```

**Array Example**

```javascript
let colors = ["Red", "Green", "Blue"];
console.log(colors[0]); // Red
```

---

## **8. Event Handling**

JavaScript interacts with the **browser** using events.

```html
<button onclick="showMessage()">Click Me</button>

<script>
  function showMessage() {
    alert("Button Clicked!");
  }
</script>
```

---

## **Conclusion**

JavaScript syntax is flexible and easy to learn. Mastering these **basics** will help in **building interactive web applications**.

### **Control Statements in JavaScript**

Control statements determine the **flow of execution** in a JavaScript program. They help in making decisions, repeating tasks, and jumping to specific sections of code.

---

## **1. Conditional Statements** (Decision Making)

Conditional statements help execute code **based on conditions**.

### **a) if Statement**

Executes a block of code **if the condition is true**.

```js
let age = 18;
if (age >= 18) {
  console.log("You are eligible to vote.");
}
```

### **b) if-else Statement**

Executes one block **if the condition is true**, otherwise executes another block.

```js
let num = 10;
if (num % 2 === 0) {
  console.log("Even Number");
} else {
  console.log("Odd Number");
}
```

### **c) if-else if-else Statement**

Checks multiple conditions in sequence.

```js
let marks = 85;
if (marks >= 90) {
  console.log("Grade A");
} else if (marks >= 75) {
  console.log("Grade B");
} else {
  console.log("Grade C");
}
```

### **d) switch Statement**

Used when multiple conditions depend on a single variable.

```js
day = "Monday";
switch (day) {
  case "Monday":
    console.log("Start of the week!");
    break;
  case "Friday":
    console.log("Weekend is near!");
    break;
  case "Sunday":
    console.log("Yeahhhh! It's a holiday!");
    break;
  default:
    console.log("Regular day.");
}
```

---

## **2. Looping Statements** (Repetition)

Loops help in **repeating a block of code** multiple times.

### **a) for Loop**

Runs a block of code **a fixed number of times**.

```js
for (let i = 1; i <= 5; i++) {
  console.log("Iteration " + i);
}
```

### **b) while Loop**

Runs **as long as a condition is true**.

```js
let x = 1;
while (x <= 5) {
  console.log("Count: " + x);
  x++;
}
```

### **c) do-while Loop**

Executes **at least once**, then continues **while the condition is true**.

```js
let y = 1;
do {
  console.log("Number: " + y);
  y++;
} while (y <= 5);
```

### **d) forEach Loop** (for Arrays)

Executes a function for **each element in an array**.

```js
let numbers = [1, 2, 3, 4, 5];
numbers.forEach((num) => console.log(num));
```

---

## **3. Jump Statements** (Control Flow)

Jump statements **alter the normal sequence of execution**.

### **a) break Statement**

Exits a loop **immediately** when a condition is met.

```js
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break; // Stops the loop when i is 5
  }
  console.log(i);
}
```

### **b) continue Statement**

Skips the **current iteration** and moves to the next.

```js
for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue; // Skips printing 3
  }
  console.log(i);
}
```

### **c) return Statement**

Used inside a function to **exit and return a value**.

```js
function add(a, b) {
  return a + b; // Exits the function and returns sum
}
console.log(add(5, 3));
```

---

### **Summary Table**

| Type            | Statement                             | Use Case                               |
| --------------- | ------------------------------------- | -------------------------------------- |
| **Conditional** | `if`, `if-else`, `switch`             | Execute code **based on conditions**   |
| **Looping**     | `for`, `while`, `do-while`, `forEach` | Repeat code **multiple times**         |
| **Jump**        | `break`, `continue`, `return`         | Alter the normal **flow of execution** |

console.log("===== Conditional Statements =====");

// if-else condition
let age = 18;
if (age >= 18) {
console.log("You are eligible to vote.");
} else {
console.log("You are NOT eligible to vote.");
}

// switch-case example
let day = "Monday";
switch (day) {
case "Monday":
console.log("Start of the week!");
break;
case "Friday":
console.log("Weekend is near!");
break;
default:
console.log("Regular day.");
}

console.log("\n===== Looping Statements =====");

// for loop (Print numbers 1 to 5)
console.log("For Loop Output:");
for (let i = 1; i <= 5; i++) {
console.log(i);
}

// while loop (Print numbers 1 to 5)
console.log("\nWhile Loop Output:");
let x = 1;
while (x <= 5) {
console.log(x);
x++;
}

// do-while loop (Executes at least once)
console.log("\nDo-While Loop Output:");
let y = 1;
do {
console.log(y);
y++;
} while (y <= 5);

console.log("\n===== Jump Statements =====");

// break statement (Stops loop when number is 3)
console.log("Break Example:");
for (let i = 1; i <= 5; i++) {
if (i === 3) {
console.log("Breaking the loop at", i);
break;
}
console.log(i);
}

// continue statement (Skips number 3)
console.log("\nContinue Example:");
for (let i = 1; i <= 5; i++) {
if (i === 3) {
console.log("Skipping", i);
continue;
}
console.log(i);
}

// return statement inside a function
console.log("\nFunction with Return Statement:");
function add(a, b) {
return a + b;
}
console.log("Sum of 5 and 3:", add(5, 3));

###############################################################################################

In JavaScript, **exception handling** is done using the `try...catch` statement. It allows you to catch and handle errors that occur during the execution of your code. The general structure looks like this:

```javascript
try {
  // Code that may throw an error
} catch (error) {
  // Code to handle the error
} finally {
  // Code that runs after the try-catch, regardless of whether an error occurred or not
}
```

### Explanation:

- **`try` block**: Contains the code that might throw an error.
- **`catch` block**: Handles the error if one occurs. The error object is passed as an argument to the `catch` block.
- **`finally` block** (optional): Contains code that will always run, regardless of whether an error occurred or not (e.g., cleanup tasks).

### Example of Basic Exception Handling:

```javascript
try {
  let result = 10 / 0; // This will throw an error, as dividing by zero is undefined
  console.log(result);
} catch (error) {
  console.log("An error occurred: " + error.message); // Handles the error
} finally {
  console.log("This will always run, no matter what.");
}
```

### Example with a Custom Error:

You can also throw custom errors using the `throw` statement, which can be useful for handling specific situations.

```javascript
try {
  let age = -5;
  if (age < 0) {
    throw new Error("Age cannot be negative");
  }
  console.log("Age is valid");
} catch (error) {
  console.log("Error: " + error.message); // Handles the custom error
} finally {
  console.log("End of validation.");
}
```

### Catching Specific Errors:

You can also catch specific types of errors, for example, `TypeError` or `ReferenceError`.

```javascript
try {
  let user = null;
  console.log(user.name); // This will cause a TypeError
} catch (error) {
  if (error instanceof TypeError) {
    console.log("TypeError occurred: " + error.message);
  } else {
    console.log("Other error: " + error.message);
  }
} finally {
  console.log("Execution finished.");
}
```

### Handling Multiple Errors:

You can handle different kinds of exceptions separately in multiple `catch` blocks using JavaScript's **multi-catch** pattern in modern versions of JavaScript.

```javascript
try {
  let result = someNonExistentFunction(); // ReferenceError
} catch (error) {
  if (error instanceof ReferenceError) {
    console.log("Reference Error: " + error.message);
  } else if (error instanceof TypeError) {
    console.log("Type Error: " + error.message);
  } else {
    console.log("Other Error: " + error.message);
  }
}
```

### Important Notes:

- **`try...catch`** blocks can help ensure your code continues running even if something goes wrong.
- Always aim to handle **expected errors** (like invalid user input) and **unexpected errors** (like network failure or API errors) gracefully.
- Using `throw` is useful for creating custom error conditions in your program.

This allows you to ensure that your program can recover from errors and continue functioning without crashing unexpectedly.

#######################################################################################################

In JavaScript, **type conversion** refers to the process of converting one data type to another. This can happen **implicitly** (automatically) or **explicitly** (manually).

### 1. **Implicit Type Conversion (Type Coercion)**

JavaScript automatically converts data from one type to another when needed. This is called **implicit conversion** or **type coercion**.

Examples:

```javascript
let num = 10; // Number
let str = "5"; // String

let result = num + str; // Implicit conversion of number to string
console.log(result); // Output: "105" (number is converted to string and concatenated)
```

In this case, the number `10` is implicitly converted into a string, and then the two strings are concatenated.

Another example of implicit conversion:

```javascript
let x = "5";
let y = 10;
let sum = x * y; // String '5' is implicitly converted to number
console.log(sum); // Output: 50
```

Here, the string `'5'` is automatically converted to a number because the multiplication operation expects numbers.

### 2. **Explicit Type Conversion**

You can manually convert between data types using various built-in JavaScript functions or methods.

#### a) **To String (String Conversion)**

You can convert a value to a string using methods like `String()`, `.toString()`, or string concatenation.

Examples:

```javascript
let num = 100;
let str = String(num); // Using String() function
console.log(str); // Output: "100"

let bool = true;
let str2 = bool.toString(); // Using toString() method
console.log(str2); // Output: "true"
```

You can also convert values to strings by simply concatenating them with an empty string:

```javascript
let value = 123;
let strValue = value + ""; // Using concatenation with empty string
console.log(strValue); // Output: "123"
```

#### b) **To Number (Number Conversion)**

You can convert values to numbers using `Number()`, `parseInt()`, `parseFloat()`, or the unary plus (`+`).

Examples:

```javascript
let str1 = "123";
let num1 = Number(str1); // Using Number()
console.log(num1); // Output: 123

let str2 = "123.45";
let num2 = parseFloat(str2); // Using parseFloat()
console.log(num2); // Output: 123.45

let str3 = "10px";
let num3 = parseInt(str3); // Using parseInt()
console.log(num3); // Output: 10 (parses the integer part)

let bool = true;
let num4 = +bool; // Using unary plus
console.log(num4); // Output: 1 (true is converted to 1)
```

#### c) **To Boolean (Boolean Conversion)**

You can convert a value to a boolean using `Boolean()` or by using double negation (`!!`).

Examples:

```javascript
let str = "hello";
let bool1 = Boolean(str); // Using Boolean()
console.log(bool1); // Output: true (non-empty string is truthy)

let num = 0;
let bool2 = Boolean(num); // Using Boolean()
console.log(bool2); // Output: false (0 is falsy)

let value = 5;
let bool3 = !!value; // Using double negation
console.log(bool3); // Output: true (non-zero number is truthy)
```

### 3. **Falsy and Truthy Values**

In JavaScript, values are implicitly converted to `true` or `false` when used in logical contexts. Values that are considered **falsy** will convert to `false`, and all other values are considered **truthy**.

#### Falsy Values:

- `false`
- `0`
- `""` (empty string)
- `null`
- `undefined`
- `NaN`

#### Truthy Values:

- All non-zero numbers
- Non-empty strings
- Objects, arrays, functions, etc.

Examples:

```javascript
let x = "";
if (!x) {
  console.log("Falsy value"); // Output: Falsy value
}

let y = "Hello";
if (y) {
  console.log("Truthy value"); // Output: Truthy value
}
```

### Summary of Type Conversions:

- **Implicit Conversion**: JavaScript automatically converts types when necessary (e.g., adding a number to a string results in string concatenation).
- **Explicit Conversion**: You manually convert values using functions like `String()`, `Number()`, `Boolean()`, `parseInt()`, `parseFloat()`, or by using methods like `.toString()` and unary `+`.

Type conversions are an essential part of JavaScript, allowing the language to handle a wide variety of data types flexibly.

###############################################################################################################################

// Function definition
function greet(name) {
return "Hello, " + name + "!";
}

// Calling the function
greetingMessage = greet("Alice");
greetingMessage1 = greet("Sachin");
a = greet("Sachin111");
console.log(greetingMessage);
console.log(greetingMessage1

);// Output: Hello, Alice!

###############################################################################################################

Great! You’ve written four **independent functions** (`add`, `sub`, `multi`, `divide`) — which is a **procedural programming** approach. Now let's **transform and explain** this using **OOP (Object-Oriented Programming)** concepts in JavaScript. We'll wrap these functions inside a **class**, then create an object of that class to access them.

---

## 🔄 Convert Your Code to OOP (Using Class)

```javascript
class Calculator {
  add(a, b) {
    return a + b;
  }

  sub(a, b) {
    return a - b;
  }

  multi(a, b) {
    return a * b;
  }

  divide(a, b) {
    return a % b;
  }
}

// Creating an object (instance) of the Calculator class
const calc = new Calculator();

// Calling methods using the object
const obj1 = calc.add(10, 7);
const obj2 = calc.sub(40, 30);
const obj3 = calc.multi(5, 8);
const obj4 = calc.divide(10, 5);

// Displaying results
console.log("Addition of a and b is : " + obj1);
console.log("Subtraction of a and b is : " + obj2);
console.log("Multiplication of a and b is : " + obj3);
console.log("Division of a and b is : " + obj4);
```

---

## 🔍 OOP Concepts in This Code

### 1. **Class**

A `class` is a blueprint for creating objects. Here, `Calculator` is a class that groups all math operations.

```javascript
class Calculator { ... }
```

---

### 2. **Object**

An object is an instance of a class. You create an object like this:

```javascript
const calc = new Calculator();
```

This `calc` object now has access to all the methods in the class.

---

### 3. **Encapsulation**

You encapsulate (wrap) all related logic (add, sub, multi, divide) inside a class so it’s organized and reusable.

---

### 4. **Abstraction**

The user of the `Calculator` class doesn’t need to know **how** the add/subtract/multiply/divide work internally — they just **call the methods**. This hides complexity.

---

### 5. ✅ Optional Improvements (for Real World)

#############################################################################################3

const person = {
name: "John",
age: 30,
isStudent: false
};

console.log(person.name); // Output: John
console.log(person["age"]); // Output: 30

class Person {
constructor(name, age) {
this.name = name; // this.name is a property
this.age = age; // this.age is a property
}

greet() {
console.log(`Hi, I'm ${this.name} and I'm ${this.age} years old.`);
}
}

const p1 = new Person("Alice", 25);
p1.greet(); // Output: Hi, I'm Alice and I'm 25 years old.

const user = {};

// Add property
user.name = "Raj";

// Modify property
user.name = "Ravi";

// Delete property
delete user.name;

const key = "email";
const user = {
[key]: "example@gmail.com"
};

console.log(user.email); // Output: example@gmail.com

// Object
const person = {
name: "John",
age: 25
};
console.log(person.name);

// String
let str = "Hello, world!";
console.log(str.toUpperCase());

// Number
let num = 42.567;
console.log(num.toFixed(2));

// Date
let today = new Date();
console.log(today.toDateString());

// Math
console.log(Math.sqrt(16));
console.log(Math.random());

// Array
let fruits = ["apple", "banana", "mango"];
console.log(fruits[1]);

// Boolean
let isLoggedIn = true;
console.log(isLoggedIn);

// Function
function greet() {
console.log("Hello!");
}
greet();

// RegExp
let pattern = /hello/i;
console.log(pattern.test("Hello World"));

// Error
try {
throw new Error("Something went wrong!");
} catch (e) {
console.log(e.message);
}

// Alert box
window.alert("Welcome to the site!");

// Confirm box
let userConfirmed = window.confirm("Do you want to proceed?");
console.log("User confirmed:", userConfirmed);

// Prompt box
let userName = window.prompt("Enter your name:");
console.log("User name:", userName);

// Access window dimensions
console.log("Width:", window.innerWidth);
console.log("Height:", window.innerHeight);

// Access URL info
console.log("Current URL:", window.location.href);

// Redirect to another page
// window.location.href = "https://example.com";

// Set a timeout
window.setTimeout(() => {
console.log("This message appears after 2 seconds");
}, 2000);

// Set an interval
let counter = 0;
let intervalId = window.setInterval(() => {
console.log("Interval count:", ++counter);
if (counter === 3) window.clearInterval(intervalId);
}, 1000);

// alert box
alert("This is an alert box!");

// confirm box
let result = confirm("Are you sure?");
console.log(result);

// prompt box
let name = prompt("What is your name?");
console.log("User entered:", name);

// Select an element
const button = document.getElementById("myButton");

// Add a click event listener
button.addEventListener("click", function () {
alert("Button clicked!");
});

// Mouseover event
button.addEventListener("mouseover", function () {
console.log("Mouse is over the button");
});

// Keydown event on the whole window
window.addEventListener("keydown", function (event) {
console.log("Key pressed:", event.key);
});

// Form submit example
const form = document.getElementById("myForm");
form.addEventListener("submit", function (e) {
e.preventDefault(); // Prevents form from refreshing the page
console.log("Form submitted!");
});

###################################################################################################

<!-- File: 01-window-object.html -->
<!DOCTYPE html>
<html>
<head><title>Window Object</title></head>
<body>
  <h2>Window Object Demo</h2>
  <script>
    // The window object is the global object in the browser
    console.log("Window Width:", window.innerWidth);
    console.log("Window Height:", window.innerHeight);
    console.log("Current URL:", window.location.href);
  </script>
</body>
</html>

<!-- File: 02-dialog-boxes.html -->
<!DOCTYPE html>
<html>
<head><title>Dialog Boxes</title></head>
<body>
  <h2>Dialog Boxes Demo</h2>
  <script>
    alert("This is an alert box");
    let confirmResult = confirm("Do you want to continue?");
    console.log("User confirmed:", confirmResult);
    let userInput = prompt("Enter your name:");
    console.log("User input:", userInput);
  </script>
</body>
</html>

<!-- File: 03-event-listener.html -->
<!DOCTYPE html>
<html>
<head><title>Event Listener</title></head>
<body>
  <h2>Click the Button</h2>
  <button id="myBtn">Click Me</button>
  <script>
    const btn = document.getElementById("myBtn");
    btn.addEventListener("click", function() {
      alert("Button clicked!");
    });
  </script>
</body>
</html>

<!-- File: 04-event-propagation.html -->
<!DOCTYPE html>
<html>
<head><title>Event Propagation</title></head>
<body>
  <div id="parent" style="padding: 20px; background-color: lightblue;">
    Parent
    <button id="child">Child Button</button>
  </div>
  <script>
    document.getElementById("parent").addEventListener("click", function() {
      alert("Parent clicked");
    }, true); // useCapture = true

    document.getElementById("child").addEventListener("click", function(e) {
      alert("Child clicked");
      e.stopPropagation(); // stops bubbling
    });

  </script>
</body>
</html>

<!-- File: 05-browsing-methods.html -->
<!DOCTYPE html>
<html>
<head><title>Browsing Methods</title></head>
<body>
  <h2>Browsing Methods</h2>
  <button onclick="location.reload()">Reload Page</button>
  <script>
    console.log("Location HREF:", window.location.href);
    console.log("History Length:", window.history.length);
  </script>
</body>
</html>

<!-- File: 06-hoisting.html -->
<!DOCTYPE html>
<html>
<head><title>Hoisting</title></head>
<body>
  <h2>JavaScript Hoisting</h2>
  <script>
    // Function hoisting
    hoistedFunction();
    function hoistedFunction() {
      console.log("This function is hoisted");
    }

    // Variable hoisting
    console.log(a); // undefined
    var a = 10;

  </script>
</body>
</html>

<!-- File: 07-regex.html -->
<!DOCTYPE html>
<html>
<head><title>Regular Expressions</title></head>
<body>
  <h2>RegExp Demo</h2>
  <script>
    let text = "JavaScript is amazing!";
    let pattern = /script/i;
    console.log("Pattern match:", pattern.test(text));
  </script>
</body>
</html>

<!-- File: 08-form-validation.html -->
<!DOCTYPE html>
<html>
<head><title>Form Validation</title></head>
<body>
  <h2>Form Validation</h2>
  <form onsubmit="return validateForm()">
    <input type="text" id="name" placeholder="Enter name">
    <input type="submit" value="Submit">
  </form>
  <script>
    function validateForm() {
      const name = document.getElementById("name").value;
      if (name === "") {
        alert("Name must be filled out");
        return false;
      }
      return true;
    }
  </script>
</body>
</html>

<!-- File: 09-dom-bom.html -->
<!DOCTYPE html>
<html>
<head><title>DOM and BOM</title></head>
<body>
  <h2>DOM & BOM Demo</h2>
  <p id="demo">Hello</p>
  <script>
    // DOM
    document.getElementById("demo").innerText = "Updated with DOM";

    // BOM
    console.log("Screen Width:", window.screen.width);
    console.log("Navigator Language:", window.navigator.language);

  </script>
</body>
</html>

<!-- File: 10-ajax.html -->
<!DOCTYPE html>
<html>
<head><title>AJAX Example</t

#######################################################################################################
