# [HTML](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)

``` HTML
<!DOCTYPE html>
<html>
  <head>
    <title>My First Webpage</title>
  </head>
  <body>
    <h1>Welcome to My Website</h1>
    <p>This is a paragraph of text on my first HTML page!</p>
  </body>
</html>
```
 - `<!DOCTYPE html>`: Tells the browser this is an HTML5 document.
 - `<html>`: Root element of the HTML page.
 - `<head>`: Contains meta-information (title, styles, scripts, etc.).
 - `<title>`: The page title that appears in the browser tab.
 - `<body>`: All visible content goes inside here.
### Common HTML tags
| Tag                      | Description                              |
| ------------------------ | ---------------------------------------- |
| `<h1>` to `<h6>`         | Headings (h1 is largest, h6 is smallest) |
| `<p>`                    | Paragraph                                |
| `<a href="">`            | Link to another page or site             |
| `<img src="" alt="">`    | Displays an image                        |
| `<ul>` / `<ol>` / `<li>` | Unordered/ordered list and items         |
| `<div>`                  | Generic container                        |
| `<span>`                 | Inline container                         |
| `<br>`                   | Line break                               |

##### Anchor tag - link to website
```HTML
<a href="https://www.example.com">Visit Example</a>

<img src="https://via.placeholder.com/150" alt="Placeholder Image">
```

##### Hidden input
```HTML
<form action="/submit" method="post">
  <input type="hidden" name="userID" value="12345" />
  <input type="text" name="username" />
  <input type="submit" value="Submit" />
</form>
```
###### Result:
<img width="222" alt="image" src="https://github.com/user-attachments/assets/e41d7b5f-0f37-4915-bcf5-262b5516e08a" />

#### Forms and Input Types
 - `<form>, <input>, <textarea>, <select>, <button>, etc`.
 - Attributes like `name, action, method, required, placeholder`
 - Input types: `text, email, number, checkbox, radio, date, hidden`
#### Semantic HTML
- Meaningful tags like: `<header>, <nav>, <main>, <section>, <article>, <footer>`

#### Common meta tags and what they do
```HTML
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="description" content="A personal blog about travel and food.">
    <meta name="keywords" content="travel, food, blog">
    <meta name="author" content="Jane Doe">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Travel Blog</title>
  </head>
  <body>
    <!-- Page content here -->
  </body>
</html>
```
 - `<meta charset="UTF-8">` --> sets charactar encoding
 - `<meta name="description" content="Explore the best travel destinations and food experiences.">` --> Provides a **summary** of your page.
 - `<meta name="keywords" content="travel, blog, adventure, food">` --> Keywords relevant to your content (SEO-related)




