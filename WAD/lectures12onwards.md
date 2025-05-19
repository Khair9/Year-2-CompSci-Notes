###### [Lecture 12-?](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
# Lecture 12 - Client Side Enviroment
### Client	Tier	
<img width="691" alt="image" src="https://github.com/user-attachments/assets/e8e668ca-86e5-49b8-acd7-cabc8761b7a4" />

### Document	Object	Model	(DOM)	
In	the	HTML	DOM	(Document	Object	Model),	everything	is	a	node:
- The	document	itself	is	a	document	node	
-  All	HTML	elements	are	element	nodes	
-  All	HTML	attributes	are	attribute	nodes									
-  Text	inside	HTML	elements	are	text	nodes	
-  Comments	are	comment	nodes
##### properties
(values	you	can	get	or	set,	like	changing	the	content	of	an	HTML	element)
- `someElement.innerHTML` -	the	text	value	
- `someElement.nodeName`	-	the	name	
- `someElement.nodeValue`	-	the	value	(null	for	elements)	
- `someElement.parentNode`	-	the	parent	node	
- `someElement.childNodes`	-	the	child	nodes	
- `someElement.attributes`	-	the	attributes	nodes	

#### DOM advantages
 -  XML	/	Tree	structure	makes	the	DOM	easy	to	traverse
 -  Elements	can	be	accessed	one	or	more	times	
 - XML	/	Structure	of	the	Tree	is	modifiable		
 - Values/Elements/Structure	can	be	added,	changed	and	modified	
 - It’s	a	standard	of	the	W3C			
 - i.e.,	the	unofficial/official	law	of	the	jungle
#### DOM disadvantages
 - Resource	intensive,	consuming	lots	of	memory
 -  it	needs	to	be	fully	loaded	in	main	memory
 -  Can	be	slow
 -  depends	on	the	size	and	complexity	of	the	tree
 -  May	not	be	the	best	choice	for	all	devices/apps
 -  i.e.,	a	graphics	intensive	application	or	game	may	well	not	be	suited	to	this	model
 - A	better	alternative	might	be	to	use	the	Canvas directly
 - i.e.,OpenGL

### Event	Handling
#### Event flow
Each	event	object	has	an	‘Event	Target’,	e.g.,	any	node	in	the	DOM	tree	from	where	an	event	originated	
##### There	are	two	main	types	of	event	flow	
 - event	capture	(global	handling)	
 - event	bubbling	(local	handling)	
 - Eventflow	follows	a	“RoundTrip”	pattern/model

<img width="500" alt="image" src="https://github.com/user-attachments/assets/f5ef0be7-8abf-49c5-a959-3a54621f426b" />

##### Event capture

<img width="500" alt="image" src="https://github.com/user-attachments/assets/d74bf475-1c45-46d4-a13b-dfbeceb8a6bf" />

##### Event bubbling

<img width="500" alt="image" src="https://github.com/user-attachments/assets/647b3e0a-b243-4e19-b73c-6aea662d7dcb" />


#### An example event handling script
```html
<htm1> ‹head>
‹link rel="stylesheet" type="text/css" href="EventHandling.css"/>
‹/head> ‹body>
‹div>1
‹div>2
‹div>3
‹div>4
‹div>5</div> </divs
</div> </div>
</div> ‹p id="log"›</p> ‹script type="text/javascript" src="EventHandling.js"›‹/script>
</body> </html>
```

```js
var node = document.getElementById("log");
var divs = document. getElementsByTagName("div");
function append(line) {
var text = node.innerHTML;
node. innerHTML = text + "‹p›" + line + "</p>";
}
function capture() {
append("capture: " + this.firstChild.nodeValue);
}
function bubble() {
append("bubble: " + this.firstChild.nodeValue);
}
for (var 1 = 0; i < divs.length; i++) {
/ "click" is event type, capture/bubble are funcs from above,
// bool is useCapture mode (don't have to include - defaults to false)
divs[il.addEventListener("click", capture, true); divs^ii.addEventListener("click", bubble, false);
```

-----------------------

# Lecture 18 - Messaging
### System Architecture & Messaging
When building web apps, we need to send messages between systems (e.g., client ↔ server). These messages need to follow a certain format and protocol depending on what you're trying to do.
### Application Communication
1. HTTP (Hypertext Transfer Protocol)
    - A common protocol used to request and send data on the web.
    - Follows a Request-Response pattern (you ask → it answers).
1. Two popular request types: GET and POST.
    - User Agent Specific Protocols (UASP)
    - Defines how the data is structured, e.g., JSON, XML, XHTML.
### Request-Response Pattern
- A user/browser makes a request (e.g., clicking a link).
- The server sends a response (e.g., a webpage).
- This usually happens synchronously (immediate response), but newer versions like HTTP/2 can be asynchronous.
### How It All Happens (Step-by-Step)
- User clicks a link.
- Browser asks DNS for the IP address.
- DNS replies with the server's IP.
- Browser connects to server on port 80 (HTTP) or 443 (HTTPS).
- Browser sends an HTTP request (e.g., "get me the homepage").
- Server sends back a response (e.g., HTML content).
- Browser displays the page.

### Sequence Diagrams
- These diagrams show message flow in detail (who talks to who, and when).
- Useful to map out interactions like:
     - Requesting a page
     - Loading stylesheets, scripts, and images
     - Talking to the database

<img width="500" alt="image" src="https://github.com/user-attachments/assets/1eeba44a-6168-452b-be7c-ae2378207b77" />

### GET vs. POST
**Idempotent**: doing it once or many times gives the same result.
##### GET:
- Sends data in the URL.
- Visible, bookmarkable, good for read-only requests.
- Example: `GET /search?query=chatgpt`
- GET = safe and idempotent (won't change anything).

##### POST:
- Sends data in the message body (hidden from URL).
- Used for submitting forms, file uploads, or anything that changes data.
- Supports larger and more complex data.
- POST = used when something might change (e.g., database update).

### Other HTTP Methods
- **HEAD**: like GET but only gets headers
- **PUT**: upload or update data
- **DELETE**: delete a resource
- **OPTIONS**: find out what methods are supported
- **TRACE / CONNECT**: used for debugging or proxy connection

### Statelessness & Sessions
- HTTP doesn’t remember you — every request is independent.
- Solutions to "remember" users:
- **Cookies**: small text files stored in the browser
- **Session IDs** in URLs
- **Hidden form fields** (used in POST requests)

-----------------

# Web Application Frameworks
### Why Web frameworks exist
When building web apps from scratch:
- You repeat a lot of the same code (like database access, user login).
- It gets tedious and inefficient.
- You want to separate concerns – structure your code better for reuse and debugging.
### MVC – Model-View-Controller
- **Model**: Deals with the data (e.g., what’s in the database).
- **View**: What the user sees (HTML, templates).
- **Controller**: Handles input and decides what to do with it.

#### MVC workflow
 - User clicks a button → controller figures out what to do.
 - Controller updates model → model updates data.
 - Model notifies view → view updates the UI.

Benefits:|Drawbacks:
---------|----------
Easier testing and debugging.|More files and setup (overhead) for small projects.
Code is modular and reusable.|Harder to understand at first.
Multiple views can use the same model.|

### Web Application Framework (WAF)
Think of a WAF like a building frame or car chassis – it gives you the structure and tools to build with, faster and more reliably.

Key Features Often Included:
- User login and permissions
- Database access (via ORM)
- Templates
- Session handling
- AJAX support
- Security features

#### Characteristics of Frameworks
- **Inversion of Control**: The framework calls your code (not the other way around).
- **Default Behavior**: Comes with helpful built-in functions.
- **Extensibility**: You can customize what you need.
- **Non-modifiable Core**: You usually use the framework as-is (unless contributing).


#### Frameworks vs. Libraries
- Framework: Controls the flow and calls your code.
- Example: Django decides when your view function runs.
- Library: You call it when you need it.
- Example: You use a date formatting library in your code.

#### Common WAF features
- **Templating systems**: Combine HTML with dynamic data.
- **Caching**: Speed up pages.
- **Security**: Login systems, permissions.
- **URL mapping**: Nice, clean URLs.
- **AJAX support**: Interactive, fast web pages.
- **Form handling**: Easy form building and validation.

#### Framework Caveats
- You must invest time to learn the framework.
- You trade flexibility for speed.
- Skills might not transfer between frameworks.
- Ecosystem is still evolving – lots of choices, not all will survive.

