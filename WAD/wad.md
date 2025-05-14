# [WAD](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/tree/main)



 - [why did i choose this fuckass degree, how is this jsut one of the 6 courses i am taking this year](https://github.com/user-attachments/assets/dc23370c-0d2b-4091-a6a8-4ada49e9302a)
-------------------------------


-------------------------------
# WAD Lectures
## Lecture 1 - introduction
### High level system architecture
<img width="595" alt="image" src="https://github.com/user-attachments/assets/cf7030ba-652f-44b3-8eb4-e708e68b7652" />

### User and Client
##### The	User	could	be	human	or	machine,	which:
 - Initiates	contact	and	interacts	with	the	client
 - Ranges	in	skills	and	abilities
 - Has a	number	of	requirements	that	need	to	be	satisfied	
 
##### The	Client	is	a	program	sitting	on	a	client	device	which	
 - sends	request	messages
 - accepts	response	messages
 - acts	on	the	message	
    - either	communicating	to	the	user	   
    - or	affecting	the	environment	in	some	way
  
### Messaging
The	request	message	is	sent	from	the	client	to the	server	to:	
 - ask	for	some	information
 - send	some	information	to	be	stored
 - either	from	user	input	 or	from	some	device	(sensor)

The	response	message	is	sent	from	the	server	to a	client	to:	
 - return	the	requested	information
 - effect	some	change	in	the	environment

### Messaging Protocols
The	request	message	protocol		
- is	usually	an	HTTP	request
- embedding	any	data	to	be	sent
    - The	response	message	protocol	
- is	an	HTTP	response
- with	content	that	is	often	in	JSON/XML

### The	Middleware/Application	Server
Middleware/Application is	the	central	component	which
- accepts	request	messages	from	clients
- returns	response	messages
- co-ordinates	the	application	components

### Backend
The	Backend/Database	is	typically	on	a	separate	
node	and	
- stores	the	data	for	the	application
- provides	the	data	when	needed
- needs	to	be	scalable	and	reliable
- could	be	a	database,	an	index,	a	flat	file
  
## Lecture 2 - Development Environment 
- 
