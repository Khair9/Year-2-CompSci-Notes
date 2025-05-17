# [CSS - Cascading Style Sheets](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
It controls how HTML elements look — colors, fonts, layouts, spacing, etc.

[The full list of properties can be found](http://www.w3.org/TR/CSS22/propidx.html)

[Compact CSS Cheatsheets are useful](http://www.lesliefranke.com/files/reference/csscheatsheet.html)

### Inline CSS
style directly in the HTML element

```HTML
<p style="color: red; font-size: 20px;">Hello, world!</p>
```
###### Result:
![image](https://github.com/user-attachments/assets/77308d30-5c8e-4a65-b573-9bee676e1eea)

### Internal CSS 
in a <style> tag inside the HTML <head>
``` HTML
<head>
  <style>
    p {
      color: green;
      font-size: 18px;
    }
  </style>
</head>
```

### External CSS
In a separate .css file
- style.css
```HTML
p {
  color: purple;
  font-weight: bold;
}
```
- HTML file
```HTML
<link rel="stylesheet" href="style.css">
```

### A complete file using internal and external css

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Demo Page</title>

  <!-- External CSS link -->
  <link rel="stylesheet" href="styles.css">

  <!-- Internal CSS -->
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }

    h1 {
      text-align: center;
      color: darkblue;
    }

    .highlight {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <h1>Welcome to My Page</h1>

  <p>This is a <span class="highlight">CSS demonstration</span> using both internal and external styles.</p>

  <div class="card">
    <h2>Card Title</h2>
    <p>This is a styled card using external CSS.</p>
  </div>

</body>
</html>

```

```CSS
/* External CSS */
.card {
  background-color: white;
  padding: 20px;
  margin: 20px auto;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}
```
-----------------------
## More advanced stuff
### Positioning
| Value      | Behavior Description                                                          | Scrolls with Page       | Takes up Space | Stays Fixed?      |
| ---------- | ----------------------------------------------------------------------------- | ----------------------- | -------------- | ----------------- |
| `static`   | Default position (no special positioning)                                     | ✅                       | ✅              | ❌                 |
| `relative` | Positioned **relative to its normal spot**                                    | ✅                       | ✅              | ❌                 |
| `absolute` | Positioned **relative to the nearest positioned ancestor**                    | ❌ (unless inside)       | ❌              | ❌                 |
| `fixed`    | Positioned **relative to the browser window** (stays put when scrolling)      | ❌                       | ❌              | ✅                 |
| `sticky`   | Acts like `relative`, then sticks to a point on scroll (like a sticky header) | ✅ → ❌ (at scroll point)| ✅              | ✅ (conditionally) |



### ID Selector
Syntax:
```css
#my-id {
  /* styles */
}
```
Example

```css
#main-title {
  color: blue;
}
```

```html
<h1 id="main-title">This is blue</h1>
```

#### Rules about IDs:
 - id must be unique on a page (only one element should have that ID)

 - Use `#` in CSS to reference an ID

---------------
## Further CSS
<img width="604" alt="image" src="https://github.com/user-attachments/assets/9aab38dd-76e4-4d01-bae8-331b37bde774" />

### **Class selectors** 
 - work on a set of specified elements through the class attribute
 - The **dot (.)** operator is used to define the class 
```CSS
<style>
.warning {font-weight: bold;}
</style>
<p class="warning">This text will be displayed in bold.</p>
<p>This text will NOT be displayed in bold.</p>
<p class="warning">Bold again here.</p
```
### ID selector 
 - provide a way to stylise unique elements through the id attribute
 - The hash symbol (#) is used to specify a unique ID
``` CSS
<style>
#first-para { font-weight: bold; }
</style>
<p id="first-para">This paragraph will be bold-faced.</p>
<p>This will not be bold.</p>
<p id="third-para">This will not be bold.</p>
```
### Decendant Selector
A descendant selector targets elements that are nested inside another element, at any level of depth.
```css
parent child {
  /* styles */
}
```

Example:
```css
div p {
  color: green;
}
```

This targets every `<p>` that is inside a `<div>`, even if it’s deeply nested:

```html
<div>
  <p>This is green</p> <!-- ✅ matches -->
  <span>
    <p>This is also green</p> <!-- ✅ still matches -->
  </span>
</div>
```

### Restricted Class and ID Selectors
In web development, the term "restricted selectors" usually refers to CSS selectors that apply styles only under certain conditions or in specific contexts — rather than globally.
##### Example code
###### Element inside a class
```CSS
.red h2 {
  color: red;
}
```
 - This restricts the style to `<h2>` elements inside an element with the class `red`.
###### Element with a specific class
```CSS
h2.red {
  color: red;
}
```
- This restricts the style to `<h2>` elements that have the `red` class directly on them.

###### Element inside an ID
```CSS
#red h2 {
  color: red;
}
```

### [Example](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/cssExample.md)

## CSS specificity
When multiple CSS rules apply to the same HTML element, and they set conflicting styles (e.g., different colors), the browser needs a way to decide which rule wins. This is where CSS specificity comes in.

| Rule Type                    | Specificity |
| ---------------------------- | ----------- |
| Inline styles                | `1,0,0,0`   |
| ID selectors                 | `0,1,0,0`   |
| Class/attribute/pseudo-class | `0,0,1,0`   |
| Element/pseudo-element       | `0,0,0,1`   |

| Selector               | Specificity | Breakdown                            |
| ---------------------- | ----------- | ------------------------------------ |
| `h1`                   | `0,0,0,1`   | 1 element (`h1`)                     |
| `body h1`              | `0,0,0,2`   | 2 elements (`body` and `h1`)         |
| `#content h2`          | `0,1,0,1`   | 1 ID (`#content`), 1 element (`h2`)  |
| `h2.grape`             | `0,0,1,1`   | 1 class (`.grape`), 1 element (`h2`) |
| `style="color: blue;"` | `1,0,0,0`   | Inline styles always win             |

So when multiple styles apply:

- Compare specificity values (like comparing phone numbers).
- If equal, the later one in the CSS file wins.
- Inline styles trump external styles. 
- !important can override all unless there's a more specific !important.


## The box model
<img width="693" alt="image" src="https://github.com/user-attachments/assets/22adefdb-56ee-4991-9f39-8147f8bb3bfd" />
<img width="927" alt="image" src="https://github.com/user-attachments/assets/3b7347f8-20d8-461e-8e31-6cfa86f5ffae" />


