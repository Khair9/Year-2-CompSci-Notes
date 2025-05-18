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





  
