# [JavaScript](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
## [The java script power point](https://moodle.gla.ac.uk/pluginfile.php/9699472/mod_resource/content/1/L13-Client-Side-Scripting.pdf)
JavaScript is a programming language used to make **web pages interactive**

### Basic HTML script with JavaScript embedded
```html
<!DOCTYPE html>
<html>
  <head>
    <title>JS Example</title>
  </head>
  <body>
    <h1 id="greeting">Hello</h1>
    <button onclick="changeText()">Click Me</button>

    <script>
      function changeText() {
        document.getElementById("greeting").innerText = "You clicked the button!";
      }
    </script>
  </body>
</html>
```
##### Result:
<img width="655" alt="image" src="https://github.com/user-attachments/assets/8de5e33d-7dc2-45e5-b60e-3060441d94c1" />

<img width="655" alt="image" src="https://github.com/user-attachments/assets/239881fa-79a0-4715-b31b-20a8c394fd9a" />

### Variables
```js
let name = "John";
const age = 25;
var isHappy = true;
```
 - `let` = can change

 - `const` = cannot change

 - `var` = old version (still works, but let/const is better)

### Data Types
```js
let text = "hello";      // string
let number = 42;         // number
let isTrue = false;      // boolean
let list = [1, 2, 3];    // array
let person = { name: "Alice", age: 30 }; // object
```
### Function
```js
function greet(name) {
  console.log("Hello, " + name);
}

greet("Alice");
```
### Conditional
```js
let age = 20;
if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```
### Loops
```
for (let i = 1; i <= 5; i++) {
  console.log("Number: " + i);
}
```
### DOM Manipulation (change HTML)
```js
document.getElementById("myHeading").innerText = "Changed!";
```
You can:
- Change text, HTML, or styles
- Add/remove elements
- Respond to user actions (click, hover, type)

### Events
```js
document.getElementById("btn").addEventListener("click", function() {
  alert("You clicked the button!");
});
```
### plugging in an external java file
```js
<script src="script.js"></script>
```
------------------------
## jQuery
- jQuery is a JavaScript library that simplifies tasks like:
- Selecting elements (document.querySelector → easier)
- Changing styles/content
- Handling events (clicks, form submissions)
- Animations
- AJAX (sending/receiving data without reloading the page)

### How to use jQuery
You include jQuery in your HTML file using a <script> tag.
```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```




