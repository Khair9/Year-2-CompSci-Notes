# [XML & JSOM](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
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
  
  
