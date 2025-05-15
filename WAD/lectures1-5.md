###### [lectures 1-5](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/WAD/wad.md)
# Lecture 1 - introduction
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
  
# Lecture 2 - Development Environment:
- It	is	good	Software	Engineering	practice	to:	
- Use	a	Version	Control	System		
   - `e.g.	Git`
- Use	a	Package	Manager		
   - `e.g.	pip	`
- Use	a	Virtual	Environment		
   - `e.g.	Anaconda`
- Use	an	Integrated	Development	Environment		
   - `e.g.	PyCharm,	IDLE`
### git
- Clone	a	repo	that	already	exists	on	a	remote	host	
- e.g.	a	project	on	GitHub	that	you	want	to	work	on	
- git	clone	https://github.com/wad2gla/demo.git
- Start	using	git	with	your	existing	code	project	
- In	main	project	directory:	
   - git init
   - git	add	*	
   - git	commit	–m	“first	commit”	
   - git	remote	add	origin	<url	you’ve	setup	on	e.g.	GitHub>	
   - git	push	–u	origin	main

### whats the point of anaconda virtual enviroment:
 - Anaconda	is	a	tool	to	keep	the	dependencies required	by	different	projects	in	separate	places	
 - It	isolates	the	different	environments	and	lets	you switch	between	them	easily	
 - Main	Advantages	
    - Separation	of	package	installation	–	you	can	use	different	package	sets	for	each	project	
    - Separation	of	Python	versions	–	you	can	use	different	Python	versions	for	each	project	
    - Virtual	environments	can	be	created/switched	between	easily	using	the	Anaconda	command	prompt
- Commands:	
   - ```conda	create	–n	<ENVNAME>	python=3.11.11```
   - Create	a	new	environment,	named	however	we	want	– replace	`<ENVNAME>`.	We	can	specify	Python	version	
   - `conda	activate	<ENVNAME>`
   - Enter	the	environment	
      - Name	of	active	env	shown	before	prompt.																														
      - e.g.			`(rango)	H:\Workspace`	
      - `conda	deactivate`	
      - Leave	the	environment	
      - `conda env	list`	
   - List	all	my	environments	
      - `conda env	remove	-n	<ENVNAME>`
      - `Delete	an	environment`
    
### simplified internal structure

  <img width="428" alt="image" src="https://github.com/user-attachments/assets/18675299-3471-4128-8da0-d6b11c615389" />
  
#### Building	Data	Models	(usually	in	models.py):		
 - The	models	specify	the	entities	and	relationships	in	the	database	–	these	provide	an	Object	Relational	Mapping	(ORM)	to	the	actual	database	tables	
 - The	framework	constructs	the	database	given	the	models	defined
 - Providing	Templates	
 - The	templates	mean	the	response	format	(html,xml,etc)	is	decoupled	from	the	data	to	be	presented	
# Lecture 4 - basics of django
### Building a `views.py`
 - Views receive HttpRequest, return HttpReponse objects
```python
from django.http import HttpResponse
def index(request):
  return HttpResponse("Hello, world")
```

### Building the `urls.py`
 - In `urls.py` in the mysite folder
```python
from django.urls import include, path
from django.contrib import admin
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

### Directory structure
<img width="129" alt="image" src="https://github.com/user-attachments/assets/b1f696cf-d197-4928-92b5-a73cc21f68f9" />

(how the directory structure is displayed in the url)

<img width="417" alt="image" src="https://github.com/user-attachments/assets/68e650ee-2f64-4bfc-bc58-ccf6c569ea5a" />

### setting up the model
 - Run `python manage.py migrate` to create database tables

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question,
    on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

