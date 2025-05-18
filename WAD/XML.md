# [XML & JSOM](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
[a useful video on xml schema](https://www.youtube.com/watch?v=1BjmZHRHDv0)
## XML
### Background of XML
 - **XML**	stands	for	**“eXtensible	Markup Language”**
Why	did	the	W3C	design	XML?
 - Mark-up	for	the	web	was	not	being	properly supported
 - Standard	Generalized	Mark-up	Language	(SGML)	was	too	complex	
 - While,	HTML	was	too	limited	and	mixed	format	with structure

##### [Sample XML script](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/sampleXML.xml)

The	structure	of	XML	is	tightly	controlled:

- Tags	are	case	sensitive	and	variable	values	must	be	quoted	
- If	there	is	a	start	tag,	there	must	be	an	end	tag
- A	hierarchical	structure	of	elements	is	enforced	
- These	are	not	strictly	enforced	in	the	case	in	HTML

### XML document anatomy
<img width = "700" alt="image" src="https://github.com/user-attachments/assets/7b636a58-1aed-4e6d-8620-4dcf38a41be7" />

#### XML attributes and values
- Attributes	are	characteristics	of	elements	
- Attributes	are	case	sensitive	
- Attributes	have	values	–	they	must	be	in	quotes!	
- All	values	are	text	strings
```XML
<ResultSet type="web" totalResultsAvailable="211000000"
totalResultsReturned="10" firstResultPosition="1" > … </ResultSet>
```

#### XML tree structure
<img width = "700" alt="image" src="https://github.com/user-attachments/assets/9e21e3f7-ad14-427a-8546-881bb4cf9bec" />


#### Predefined and Valid XML
 - To	share	XML	a	pre-defined	structure	can	be	used:	
 - These	describe	the	tags	which	can	appear,	and	can	be	done	using:	
    1. Document	Type	Definitions	(DTD),	or		
    2. XML	Schemas	and	XML	Namespaces

XML Schemas and DTDs (Document Type Definitions) are both used to define the structure and rules of an XML document. However, they have significant differences in terms of features, syntax, and capabilities.

| Feature         | DTD           | XML Schema (XSD)          |
| --------------- | ------------- | ------------------------- |
| Syntax          | Not XML       | XML-based                 |
| Data Types      | Limited       | Rich set + Custom types   |
| Namespaces      | Not supported | Supported                 |
| Extensibility   | Limited       | High                      |
| Object-Oriented | No            | Yes (inheritance, etc.)   |
| Readability     | Simpler       | More complex but powerful |
| Tool Support    | Basic         | Extensive                 |

### in summary
 - XML	was	designed	to	transport	and	store	data	
 - HTML	was	designed	to	display	data	
 - Carrying	information	vs displaying	information

## JSON - Java Script Object Notation

- Lightweight	data	interchange	format	
    - “Easy”	for	humans	to	read	and	write	
    - Easy	for	machines	to	parse	and	generate	
    - Less	boilerplate,	so	more	information	per	byte	
- JSON	is	built	on	two	universal	data	structures	
   - A	collection	of	name/value	pairs	
       - Often	realized	as	a	object,	record,	struct,	dictionary,	hash.
   - An	ordered	list	of	values	
       - Often	realized	as	an	array,	vector,	list.
### comparision of XML and JSON
<img width = "500" alt="image" src="https://github.com/user-attachments/assets/635e7edc-703b-4e71-8b03-1680de7a479c" />
<img width = "500" alt="image" src="https://github.com/user-attachments/assets/3aeef86a-5c03-4485-a7dc-cb949cc06a2a" />

| **Similarities between JSON and XML**                         | **Differences between JSON and XML**  |
| ------------------------------------------------------------- | ------------------------------------- |
| Both are **self-describing** (human-readable)                 | JSON doesn't use end tags             |
| Both are **hierarchical** (values within values)              | JSON is **shorter**                   |
| Both can be **parsed and used by many programming languages** | JSON is **quicker to read and write** |
| Both can be **fetched with XMLHttpRequest** (used in AJAX)    | JSON can **use arrays**               |

------------------------

# Processing  XML
### PROCESSING XML
#### Programming and XML
##### DOM	(The	Document	Object	Model)
   - **Definition:** "The	W3C	Document	Object	Model	is	a	platform and	language-neutral	interface	that	allows	 programs	and	scripts	to dynamically	access	and	update	the	content,	structure,	and	style	of	a	document
   - builds	an	**in-memory	hierarchical	model**	of	the	XML	elements	
   - appropriate	if	you	need	the	**whole	document**	or	need	to	**move	about	it	freely**
   - DOM	is	separated	in	three	main	parts	
        - Core	DOM:	standard	model	for	any	structured	doc	
        - HTML	DOM:	standard	model	for	HTML	docs	
        - XML		DOM:	standard	model	for	XML	docs
  ###### XML DOM
   - It	defines	objects	and	properties	of	all	XML	elements	along	with	the	methods	to	access	them	
   - DOM	defines	everything	in	an	XML	document	as	a	node	
   
  ##### **SAX	(The	Simple	API	for	XML)**
   - provides	an	**event	driven	parser**	for	XML
   - appropriate	for	using	**parts	of	the	data** in	the	order	they	appear	in	the	file,	or	if	there	are	memory	constraints
<img width = "500" alt="image" src="https://github.com/user-attachments/assets/accac72e-bd44-4a2c-ac35-34c08c738050" />


### DOM PARSING
In	whichever	language	or	environment	you	are	working,	the	technique	is	basically	the	same:	
1. load	the	XML	document	object	
2. locate	the	root	element	or	some	other	element	that	is	of	interest	
    - either	traverse	the	tree
    - or	search	for	the	desired	element		
3. for	the	given	element	
    - extract	the	attributes	and	their	values	
    - extract	the	element	data	
    - and/or	add/modify/remove	elements	or	attributes	
4. Go	to	step	2	and	repeat	until	all	processing	is	done
##### Example of DOM parsing
```html
<htm1>
   <body>
      <p id="demo"></p>
      <script>
          var text, parser, xmIDoc;
          text = "<bookstore><book>" +
          "<title>Everyday Italian</title>" +
          "<author>Giada De Laurentiis</author>" +
          "‹year›2005</year>" +
          "</book></bookstore>";
          parser = new DOMParser);
          xm1Doc = parser-parseFromString (text, "text/xmI");
          document.getElementById("demo").innerHTML = xmlDoc.getElementsByTagName("title")[0].childNodes [0].nodeValue;
      <script>
   </body>
</html>  
```
(Processing XML example)
<Br>
<img width = "250" alt="image" src="https://github.com/user-attachments/assets/86f9b04a-d090-421e-a3eb-c6612babb8ff" />

### SAX PARSING - Simple API for XML
What is SAX --> It's a way to read and process XML documents using an event-based, streaming approach.
- SAX works like this:
- You give it an XML file.
- As the file is read line by line, SAX triggers events like:
     - "Hey! I found a start tag!"
     - "Here’s some text!"
     - "This element just ended!"
- You write event handler methods (callback functions) to react to these events.
### How it works
3 Main Steps:
1. Create your own object model
   - Like a Book, Order, or Customer class to store extracted data.
2. Create a SAX parser
   - Use a parser from a library (e.g., Python's xml.sax or Java's SAXParser).
3. Create a Handler class
   - You define what happens on events: start of an element, end, or text.

### important SAX handler interfaces
| **Handler**      | **What It Does**                                       |
| ---------------- | ------------------------------------------------------ |
| `ContentHandler` | Main interface – handles most XML document events      |
| `DTDHandler`     | Deals with Document Type Definitions (if present)      |
| `EntityResolver` | Resolves external entities (e.g., links to other XMLs) |
| `ErrorHandler`   | Handles errors and warnings                            |
| `DefaultHandler` | A convenience class that implements all the above      |

### SAX Handler Methods You Write
| **Method**                       | **When It’s Called**                                          |
| -------------------------------- | ------------------------------------------------------------- |
| `startDocument()`                | When the document starts                                      |
| `endDocument()`                  | When the document ends                                        |
| `startElement(name, attributes)` | When an opening tag (like `<book>`) is found                  |
| `endElement(name)`               | When a closing tag (like `</book>`) is found                  |
| `characters(ch)`                 | When text (like a book title or author) is found between tags |




 
### SAX VS. DOM 

| Feature          | **DOM (Document Object Model)**                    | **SAX (Simple API for XML)**                            |
| ---------------- | -------------------------------------------------- | ------------------------------------------------------- |
| **How it works** | Loads the **entire XML** into memory as a **tree** | Parses XML **line by line**, triggering **events**      |
| **Memory use**   | **High** – good for small/medium XML               | **Low** – great for **large** XML files                 |
| **Navigation**   | Can freely move around the tree                    | One-way reading only – **no going back**                |
| **Use case**     | When you need to **manipulate or access all data** | When you just want to **read and process data quickly** |
| **Ease of use**  | Easier to understand; more intuitive               | Requires more code, but **faster and efficient**        |
  
