### **Introduction to CSS with Simple Code Examples**

CSS (**Cascading Style Sheets**) is used to style and format HTML documents.

---

### **1. What is CSS?**  
CSS is a language used to control the presentation (style, layout, and design) of HTML elements.

#### **Example:**
```html
<p style="color: blue;">This text is styled with CSS.</p>
```
---

### **2. Benefits of CSS**  
- **Separation of Content and Design** (HTML handles content, CSS handles design).  
- **Consistency** (Apply the same styles across multiple pages).  
- **Faster Page Load** (Less HTML code, more efficient rendering).  
- **Responsive Design** (Adapt layout for different screens).  

#### **Example (Same Style for Multiple Elements):**
```html
<style>
    p {
        color: green;
        font-size: 18px;
    }
</style>
<p>This is paragraph 1.</p>
<p>This is paragraph 2.</p>
```
---

### **3. Browser Adoption**  
All modern browsers (Chrome, Firefox, Edge, Safari) support CSS3.  

#### **Example (CSS for Different Screen Sizes - Media Query):**
```html
<style>
    body {
        background-color: lightgray;
    }
    @media (max-width: 600px) {
        body {
            background-color: lightblue;
        }
    }
</style>
```
---

### **4. CSS Syntax**  
A CSS rule consists of **selector**, **property**, and **value**.

#### **Example:**
```css
selector {
    property: value;
}
```
For example:
```css
h1 {
    color: red;
    text-align: center;
}
```

---

### **5. Inline Styles**  
CSS written directly in an HTML tag.

#### **Example:**
```html
<p style="color: red; font-weight: bold;">This is inline styling.</p>
```
---

### **6. Embedded Style Sheet**  
CSS is placed inside a `<style>` tag in the HTML `<head>` section.

#### **Example:**
```html
<head>
    <style>
        h1 {
            color: blue;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1>This is styled using an embedded style sheet.</h1>
</body>
```
---

### **7. External Style Sheet**  
CSS is written in a separate `.css` file and linked to HTML.

#### **CSS File (styles.css)**
```css
h1 {
    color: purple;
    font-size: 26px;
}
```
#### **HTML File**
```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>This is styled using an external CSS file.</h1>
</body>
```
---
### **CSS Selectors Explained with Code Examples**  

CSS **selectors** define which HTML elements a style should be applied to. 
Below are different types of selectors with **simple examples**.

---

## **📌 1. ID Selector (`#id`)**
Used to style a **specific** element with a unique ID.  
```html
<p id="special">This is a unique paragraph.</p>
```
```css
#special {
    color: red;
    font-weight: bold;
}
```

---

## **📌 2. Group Selector (`,`)**
Used to apply the same style to multiple elements.  
```html
<h1>Heading</h1>
<p>Paragraph</p>
```
```css
h1, p {
    color: blue;
}
```

---

## **📌 3. Universal Selector (`*`)**
Applies styles to **all** elements.  
```css
* {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
```

---

## **📌 4. General Sibling Selector (`~`)**
Selects all **siblings** after the specified element.  
```html
<div>
    <h2>Main Title</h2>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
</div>
```
```css
h2 ~ p {
    color: green;
}
```

---

## **📌 5. Adjacent Sibling Selector (`+`)**
Selects the **immediate** next sibling.  
```html
<h2>Title</h2>
<p>First paragraph</p>
<p>Second paragraph</p>
```
```css
h2 + p {
    color: orange;
}
```

---

## **📌 6. Child Selector (`>` )**
Selects **direct** children only.  
```html
<div>
    <p>Direct child</p>
    <span>
        <p>Nested child</p>
    </span>
</div>
```
```css
div > p {
    color: purple;
}
```

---

## **📌 7. Descendant Selector (``)**  
Selects **all** matching elements inside another.  
```html
<div>
    <p>Inside div</p>
</div>
```
```css
div p {
    color: brown;
}
```

---

### **✨ Conclusion**
- `#id` → **Unique element**
- `,` → **Multiple elements**
- `*` → **All elements**
- `~` → **All next siblings**
- `+` → **Next immediate sibling**
- `>` → **Direct child only**
- `` → **All inside elements**

That's a lot of topics! I'll provide a brief explanation for each along with an example. Let me know if you need any part expanded.

---

### **1. Attribute Selectors**
Used to select elements based on their attributes.

**Example:**
```html
<input type="text" placeholder="Enter Name">
<style>
    input[placeholder] {
        border: 2px solid blue;
    }
</style>
```

---

### **2. Background**
Controls the background properties of elements.

**Example:**
```html
<style>
    body {
        background-color: lightgray;
    }
</style>
```

---

### **3. CSS Text Styling**
Used to style text (color, size, alignment, etc.).

**Example:**
```html
<p style="color: red; font-size: 20px; text-align: center;">Hello, World!</p>
```

---

### **4. CSS Tables**
Styling tables using CSS.

**Example:**
```html
<table border="1">
    <tr><th>Name</th><th>Age</th></tr>
    <tr><td>Alice</td><td>25</td></tr>
</table>
<style>
    table { border-collapse: collapse; }
    th, td { padding: 10px; text-align: left; }
</style>
```

---

### **5. CSS Lists**
Styling lists.

**Example:**
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
<style>
    ul { list-style-type: square; }
</style>
```

---

### **6. Pseudo-Element and Pseudo-Class Selectors**
Used for styling specific parts of elements or selecting elements in specific states.

**Example:**
```html
<p>Hover over me!</p>
<style>
    p:hover { color: red; }
    p::first-letter { font-size: 30px; font-weight: bold; }
</style>
```

---

### **7. Contextual Selectors**
Used to target elements based on their parent.

**Example:**
```html
<div>
    <p>Inside Div</p>
</div>
<p>Outside Div</p>
<style>
    div p { color: blue; }
</style>
```

---

### **8. Image Gallery**
Creating an image gallery layout.

**Example:**
```html
<div>
    <img src="image1.jpg" width="100">
    <img src="image2.jpg" width="100">
</div>
<style>
    div { display: flex; gap: 10px; }
</style>
```

---

### **9. Borders**
Styling borders.

**Example:**
```html
<p style="border: 2px solid black;">Bordered Text</p>
```

---

### **10. Margins and Padding**
Controls spacing.

**Example:**
```html
<p style="margin: 20px; padding: 10px; border: 1px solid black;">Hello</p>
```

---

### **11. Box Model**
Defines how elements are sized.

**Example:**
```html
<p style="width: 100px; padding: 10px; border: 5px solid red; margin: 20px;">Box Model</p>
```

---

### **12. Positions, Display, Overflow, z-index**
Used for positioning elements.

**Example:**
```html
<div style="position: absolute; top: 50px; left: 50px;">Positioned Box</div>
```

---

### **13. Outline**
Adds an outline around elements.

**Example:**
```html
<p style="outline: 2px dashed blue;">Outlined Text</p>
```

---

### **14. Float, Clear, Alignment**
Used for layout adjustments.

**Example:**
```html
<div style="float: left; width: 50px; height: 50px; background: red;"></div>
```

---

### **15. Opacity and Media Types**
Used for transparency.

**Example:**
```html
<p style="opacity: 0.5;">Transparent Text</p>
```

---

### **16. CSS Gradients**
Applies gradient backgrounds.

**Example:**
```html
<div style="width: 100px; height: 100px; background: linear-gradient(red, yellow);"></div>
```

---

### **17. 2D and 3D Transformations**
Used for rotating, scaling elements.

**Example:**
```html
<p style="transform: rotate(45deg);">Rotated Text</p>
```

---

### **18. Transition and Animation**
Adds animations.

**Example:**
```html
<p style="transition: color 1s;" onmouseover="this.style.color='red'">Hover me!</p>
```

---

### **19. Working with External CSS**
Using external stylesheets.

**Example:**
```html
<link rel="stylesheet" href="style.css">
```

---

### **20. Flexbox**
Flexible layout.

**Example:**
```html
<div style="display: flex;">
    <div style="background: red; width: 50px;">1</div>
    <div style="background: blue; width: 50px;">2</div>
</div>
```

---

### **21. CSS Navigation Bar**
Creates a navbar.

**Example:**
```html
<ul style="display: flex; background: black; padding: 10px;">
    <li style="margin-right: 10px;"><a href="#" style="color: white;">Home</a></li>
    <li><a href="#" style="color: white;">About</a></li>
</ul>
```

---

### **22. CSS Menus and Submenus**
Dropdown menu.

**Example:**
```html
<div>
    <button>Menu</button>
    <div style="display: none;">Submenu</div>
</div>
```
---

Here’s a detailed explanation and basic design code for each of the topics you listed:

---

### **1. Box Model**
The box model consists of margins, borders, padding, and the actual content.

**Example:**
```html
<div style="width: 200px; padding: 20px; border: 5px solid red; margin: 10px; background-color: lightgray;">
    Box Model Example
</div>
```

---

### **2. Positions, Display, Overflow, z-index**
- `position`: Defines how elements are positioned (static, relative, absolute, fixed).
- `display`: Controls how an element is displayed (`block`, `inline`, `flex`).
- `overflow`: Manages content that exceeds the container (`hidden`, `scroll`, `auto`).
- `z-index`: Controls the stack order of elements.

**Example:**
```html
<div style="position: absolute; top: 50px; left: 50px; background: yellow; padding: 10px;">
    Positioned Element
</div>
```

---

### **3. Outline**
The outline is similar to a border but does not take up space.

**Example:**
```html
<p style="outline: 3px dashed blue; padding: 10px;">Outlined Text</p>
```

---

### **4. Float, Clear, and Alignment**
- `float`: Allows elements to be placed left or right.
- `clear`: Prevents elements from wrapping around floated elements.

**Example:**
```html
<img src="image.jpg" style="float: left; margin-right: 10px;" width="50">
<p>This text wraps around the floated image.</p>
```

---

### **5. Opacity and Media Types**
- `opacity`: Adjusts the transparency of elements.

**Example:**
```html
<p style="opacity: 0.5;">This text is semi-transparent.</p>
```

---

### **6. CSS Gradients**
- `linear-gradient`: Creates a smooth transition between colors.

**Example:**
```html
<div style="width: 200px; height: 100px; background: linear-gradient(to right, red, blue);">
</div>
```

---

### **7. 2D and 3D Transformations**
- `transform`: Allows scaling, rotating, and translating elements.

**Example:**
```html
<p style="transform: rotate(30deg);">Rotated Text</p>
```

---

### **8. Transition and Animation**
- `transition`: Smoothly changes a property over time.
- `@keyframes`: Creates animations.

**Example:**
```html
<button style="background: blue; color: white; transition: background 1s;" onmouseover="this.style.background='red'">
    Hover me!
</button>
```

---

### **9. Working with External CSS**
External stylesheets allow separating design from HTML.

**Example:**
```html
<link rel="stylesheet" href="styles.css">
```

**styles.css**
```css
body { background-color: lightgray; }
```

---

### **10. Flexbox**
Flexbox provides a flexible way to arrange elements.

**Example:**
```html
<div style="display: flex; gap: 10px;">
    <div style="background: red; padding: 10px;">Item 1</div>
    <div style="background: blue; padding: 10px;">Item 2</div>
</div>
```

---

### **11. CSS Navigation Bar**
A simple horizontal navbar.

**Example:**
```html
<ul style="display: flex; background: black; padding: 10px;">
    <li style="margin-right: 10px;"><a href="#" style="color: white;">Home</a></li>
    <li><a href="#" style="color: white;">About</a></li>
</ul>
```

---

### **12. CSS Menus and Submenus**
Dropdown navigation menu.

**Example:**
```html
<div style="position: relative;">
    <button>Menu</button>
    <div style="display: none; position: absolute; background: lightgray;">
        <a href="#">Submenu 1</a><br>
        <a href="#">Submenu 2</a>
    </div>
</div>
```

### **23. Layouts**
Defines webpage structure.

**Example:**
```html
<div style="display: grid; grid-template-columns: 1fr 2fr;">
    <div>Sidebar</div>
    <div>Main Content</div>
</div>
```

---

### **24. Responsive Design and Media Queries**
Used for mobile-friendly design.

**Example:**
```html
<style>
    @media (max-width: 600px) {
        body { background-color: yellow; }
    }
</style>
```

---

### **25. Complete Web Page Designing**
Full HTML page.

**Example:**
```html
<!DOCTYPE html>
<html>
<head><title>My Page</title></head>
<body>
    <h1>Welcome</h1>
</body>
</html>
```

---

### **26. Loading Webpage Symbol Design**
CSS loader animation.

**Example:**
```html
<div style="border: 4px solid gray; border-top: 4px solid blue; border-radius: 50%; width: 20px; height: 20px; animation: spin 1s linear infinite;"></div>
<style>
    @keyframes spin { 100% { transform: rotate(360deg); } }
</style>
```

---
