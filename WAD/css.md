# [CSS - Cascading Style Sheets](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
It controls how HTML elements look — colors, fonts, layouts, spacing, etc.
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






