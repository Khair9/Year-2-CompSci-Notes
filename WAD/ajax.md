# [AJAX](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
 - AJAX	eliminates	the	need	to	reload	a	web	page	in order	to	get	new	content	from	the	server	
 - This	removes	the	start-stop interaction	where	a	user	has	to	wait	for	new	pages	to	load	
 - An	intermediate	layer	(AJAX	Engine)	is	introduced	into	the	communication	chain	between	client	and	server	
 - Improves	the	interactive	experience	in	web	apps

### XHR - XMLHttpRequest object
 - The	XHR	is	an	object	that	is	part	of	the	DOM	and	is	built	into	most	modern	browsers
 - It	can	communicate	with	the	server	by	sending	HTTP	requests	(much	like	normal	client/server	communication)

<img width = "500" alt="image" src="https://github.com/user-attachments/assets/1ae418d1-c5fe-47dc-b7a7-439fbf67a28b" />

<img width = "500" alt="image" src="https://github.com/user-attachments/assets/353d37e4-2051-49da-8bf6-3950e0eee0ec" />

1. An	event	occurs	in	a	web	page	(the	page	is	loaded,	a	button	is	clicked)	
2. An	XMLHttpRequest	object	is	created	by	JavaScript	
3. The	XMLHttpRequest	object	sends	a	request	to	a	web	server	
4. The	server	processes	the	request	
5. The	server	sends	a	response	back	to	the	web	page	
6. The	response	is	read	by	JavaScript	
7. Proper	action	(like	page	update)	is	performed	by JavaScript

#### XHR properties
 - **readyState** property	
 – Holds	the	status	of	the	XMLHttpRequest
      - 0:	request	not	initialized		
      - 1:	server	connection	established	
      - 2:	request	received		
      - 3:	processing	request		
      - 4:	request	finished	and	response	is	ready	
- **onreadystatechange** property	
     -  accepts	an	EventListener	value,	specifying	the	method	that	the	object	will	invoke	whenever	the	readyState value	changes	
     - status	property
-  The	**status**	property	represents	the	HTTP	status	code	and	is	of	type	short	(e.g.	200	=	OK,	404	=	Not	Found)

-  If the server sends back XML, this holds the XML data.
    - Works only if:
          - readyState is 4 (done), and
          - The response is labeled as XML (like text/xml, application/xml, or ends with +xml).
- responseText Property
    - This contains the full response as plain text.
    - You can use it whether the data is XML, JSON, or plain HTML.


    
