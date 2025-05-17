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
