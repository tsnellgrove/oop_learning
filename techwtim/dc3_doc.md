dark castle 3 demo to-dos

NEXT: Tom Example
inheritance
Create Door as child of Item [DONE]
Create ViewOnly as parent to Item [DONE]
Create Container as child to door [DONE]
Create take & drop methods for Item [DONE]
Create unlock method for Door & Container [DONE]
Create open method for Door [DONE]
Create a Room child class of view_only... focus on inventory only - not movement [DONE]
Exercise inventory management using Room.room_objects and hand and take and drop [IN-PROC]
	Update Room examine, take, and drop [DONE]
	DONE: Test implementation
	DONE: add takability to the 'take item' method
DONE: More tutorials before this gets out of hand!
Note: I think I'm doing something wrong... 
	inventory management with objects is not as elegant as I was expecting

DONE: Too many calsses already... think about consolidation
Decision: Inheritance is complicated, Multi-Inheritance is more complicated, 
	and multi inheritance from inherited classes... is just right out!
DONE: So => make 'takable' a local attribute of container

Idea: Rooms are really just conneectd containers...
DONE: Link travel to doors or to rooms? For now deciding on rooms
DONE: Troubleshooting movement
DONE: Implemnt doors in rooms

DONE: Implement While True input loop
DONE: Fix input conversion
DONE: Fix go command - interpreter
DONE: Description of new room on change rooms
DONE: Enforce room.examine() based on location
DONE: Implement 'look'
DONE: Update room based on go (try global room)
DONE: Pass room variable to class methods (state_dict)
DONE: Troubleshoot "examine gate"... maybe implemnt room across all methods first??

DONE: Think through writing attribute for ViewOnly 
	(i.e. should be read dwarven_runes instead of read sword)
IDEA: Maybe what I want to do is create a method that can put one item *on* another... 
	so that I can put the writing *on* the item?
IDEA: Similar problem to a container... need a list of things that can be *on* the item - 
IDEA: should be at the ViewOnly level since many objects can have writing on them...
IDEA: nead a name... maybe 'features'
IDEA: this could also be used for control panel

DONE: Extend examine() for class Door to include open or close state
DONE: Fix read_writing => read
DONE: Implement 'close'
DONE: Implement 'lock'

DONE: Implement features
DONE: Writing as class
DONE: Implement read for ViewOnly class
DONE: Extend examine method for classes Room and Door (vs. replace)
DONE: Test read for Door class
DONE: Move 'features' to Room class (since we only examine room features)
DONE: Re-add 'features' to ViewOnly class - 
	because otherwise there is no way to include it in examine_lst
DONE: Add presence checking for examine on Door and Room classes

DONE: Implement containers
DONE: Decide how container contents should be presented and added to examine and take scope
DEC: Show container contents with hasattr upon open and then add to room objects
DONE: Implement 'open' case for containers (troubleshoot and implement case of empty containers)
DONE: Implement / Troubleshoot 'close' case for containers
NOTE: Implemented close reduction of room_objects via sets which leads to re-order

DONE: Reconsider restricting 'features' to class Room using hasattr
DONE: dis-allow locking when Door / Container object is open?
DONE: Represent container elements as sub elements of container in room
NOTE: Now I have a few more container problems:
DONE: First I need to make items in containers takable... 
	but not list them in the room_objects inventory... 
	perhaps I have an open_container_obj list? 
	Or perhaps better yet, 
	dynamically add contents of open containers to takeable scope? [YES!!]
IDEA: Next, when I take the item from the container,
	I need to remove it from <container>.contains
DONE: I think this in turn means 
	that the *item* needs to know what container it's in (like writing)?...
	No... let's keep items 'dumb'... 
	it's the room's job to know what's in the room 
	and it's the container's job to know what's in the container... 
	to implement this we just reverse the take scope process... 
	we start with a for loop of open containers and remove from there if possible
	else remove from room_objects
NOTE: I didn't have these issues in the old Dark Castle 
	because I had no 'close' command... 
	so I could safely dump the contents of any container 
	into room_obj the moment the container was openned. 
	Now that containers can be closed I need to actually solve this problem.
NOTE2: Should writing work this same way?
	No - I think it makes sense for writing to know what it's on..
	Because the two are entwined... 
	the writing on one object can never move to another
DONE: Add 'the container is empty' description for empty containers
DONE: Can't examine items in open containers... 
	need to add open container contents to examine_lst

DONE: Redirect prints to buffer
DONE: Create stateful_dict['out_buff']
DONE: Create buffer() helper function
DONE: "Bufferize" classes ViewOnly and Writing
DONE: "Bufferize" classes Room and Item
DONE: "Bufferize" class Door method examine
DONE: "Bufferize" class Door remaining methods

DONE: functionalize interpreter
DONE: "Bufferize" interpreter

DONE: Added open containers to read scope 
DONE: Functionalize container scan, perhaps look in room first


At this point, STOP(!!!), and start researching how others have implemented OOP text adventures
	DONE: Watch this non-oop text adventure tutorial: https://youtu.be/miuHrP2O7Jw
		Basic but good start
	DONE: OOP text adv tut: https://youtu.be/VxhZZHnig8U
		I can't stand this instructor's code style - more lessons after this one but can't face them
	DONE: 2013 advanced OOP Txt Adv: https://youtu.be/8CDePunJlck
		Great lesson! But all about console so need to pick and choose ideas
	NOTE: Did a bit of research - looks like cmd can be used with Flask; need to learn more about NLTK
	DONE: NLTK vid: https://youtu.be/1taCGR3_jlA
	DONE: Found Jeffery Armstrong from 2013 PyOhio Text Adv: https://github.com/ArmstrongJ?tab=overview&from=2021-03-01&to=2021-03-06
	NEXT: Understand robotadventure code better... learn about interpreter, DB, and JSON descriptions

new ideas:
	use a display_intro function
	import pprtint from pprint | pprint(vars(<object>))
	check https://github.com/ArmstrongJ/pyohio2013
	get to know cmd module - can cmd be used with flask??
	rooms to have lists of neighbors, objects, characters
	store rooms in json using json module? (import json) [see adv OOP at 15:30]
	room descriptions in json but then json-based rooms in sql DB??
	read through 2013 code in detail!!!
	make a copy of game DB for each player - enables "saved game"... 
	but will still need to differentiate static from stateful?
	modules for making file copy: tempfile, shutil
	curses module for status bar ??
	"nltk" (?) for interpreter??
	sqlite3 for DB?
	check out "robotadventure" from end of 2013 presentation
	how to eliminate eval()

Decisions:
	No need for curses in a flask app
	Don't use nltk - is overkill (and besides, I want to write me own interpreter)
	For now, don't use cmd - want more practice with classes
	Do figure out how to avoid using eval()

To Decide:
	Rooms in JSON?
	How to use DB??
		- Since I'm designing a web game, I need to separate stateful and static

Next to dos
DONE: Figure out how to replace eval() w/ getattr() => use str_to_class() snippet
DONE: Replace eval() usage w/ str_to_class()
DONE: 'take' is broken post eval() remove
DONE: 'take' removal logic doesn't check for item_obj being in container before attempting to remove it
DONE: Why does close need to remove container items from room_obj? Old legacy logic
DONE: Wouldn't it be a lot simpler if we just stored room_obj in stateful_dict rather than room_str ?
	DONE: Try using .name property of Room instead of tracking room in stateful_dict
DONE: Simplify open_cont_scan

DONE: new naming convention to clarify between room_obj and room_objects ?? Need a new term for "objects"
	DONE: Sort out whole naming convention of name_type vs. name_objects (containter too)
	DONE: room_objects => room_elements
	DONE: items in room_elements loop => elements
	DONE: room_element => objects?
		DONE: Initial troubleshooting in entrance
		DONE: unlock, lock, open, close
		DONE: Containers
		DONE: What about directions / doors
		DONE: Testing & Clean-up
		DONE: Should hand and room_objects also contain actual objects instead of text? 

DONE: if type() => hasattrib
DONE: Can I buffer at the end of each method?? // Buffer to one line
DONE: Naming convention for lst, dict, and obj?
	DONE: Thinking about this more... I don't want to type post-fix my primary variables... just my local ones
	DONE: Variable renames for stateful_dict and helper functions
	DONE: Variable renames for methods for ViewOnly and Writing
	DONE: Variable renames for methods for class Room
	DONE: Variable renames for methods for class Item
	DONE: Variable renames for methods for class Door
DONE: am I testing class Door methods (unlock, lock, open, close) for door in room?
DONE: Create separate doc file for to-do notes
DONE: Make examine scope check a function (include hand_lst, container_lst, room_obj_lst, & features_lst ?) (boolean for buffer)
DONE: drop => scope_check function
DONE: for Door class examine and open and Room class examine - functionalized container code
DONE: take => check room_stuff first
DONE: Extend use of open_cont_scan to all methods (how?)
DONE: Std solution for null for writing (vs. text 'null') => None

*** Interpreter Basics ***
DONE: 0) Functionalize Interpreter and use out_buff
DONE: 0.2) Should burt be an object??? (for now, No)
DONE: 0.3) Create a list of true one-word commands from dkv2:
	DONE: simple, true one-word commands: 'score', 'version'
	DONE: complex, true, one-word commands:	'inventory', 'look'
DONE: 0.31) Concept of 'universal scope' variables which should always be viewable - check dkv2
	Things burt always has with him: 'backpack', 'burt', 'hand', 'conscience' 
	Meta-game entities that should always be available: 'credits', 'help' 
DONE: 0.315) think through synonyms (e.g. 'n' == 'north' == 'go north' ) (n, s, e, w, i = inventory)
DONE: 0.32) one-word commands to be converted to two words
	simple: 'help', 'credits', 'north', 'south', 'east', 'west'
DONE: 0.33: first handle true one-word commands, then dict lookup word 2 for converted words and pass to 2-word code
DONE: 0.4) handle articles (a, an, the)

*** Time for some code maintenance / plubming ***
DONE: 0.6) time to implement backpack?
DONE: 0.63) Every scope search happens in a room, and every room has a feature list - so why are features different in scope function?
DONE: 0.65) review dkv2 verb methods... maybe move fail statements to top??
		DONE: Door Class
		DONE: Item Class
		DONE: Room Class
		DONE: Other Classes
DONE: 6.7) Remove buffer from scope_check function... reads more clearly inline in method
DONE: 0.7) convert to true flask vs. app structure (but don't worry about passing yet) [see version 2.1.4 for ideas]
	DONE: 0.71) introduce end function
	DONE: introduce move counter
	DONE: 0.73) fix 'quit' and add 'q' abreviation
	DONE: 0.76 fix 'start'
	DONE: add github remote
	DONE: email Franco to ask about pythonic approach to storing objects with multi-line string attributes; maybe store as JSON and import?

Structure Big Picture:
A-1) Create Helper module
A-2) Create Class module
A-3) Object Instantiation module
B) Refine main Interpreter function
C) Sort out prepositions
D) Create interpreter function module

*** Interpreter Adjectives & Preposistions ***
Fini 1-word commands
DONE: 1) Sort out 1 word vs. 2 word commands and error out all non-defined one-word commands

Word commands:
DONE: 3) use lists to identify words as verbs; (adjectives and prepositions later; nouns never?)
DONE: 4) if sentence does not start with a verb => please start with a verb

Adjectives:
IDEA: Every noun as an obj_name, full_name, root_name
	DONE: 5) add adjective to all items, doors, and containers => Extend to view_only
	DONE: 5.5) add full_name for all items, doors, and containers => Extend to view_only
	DONE: 5.7) Update to buffer full_name
	DONE: 6) Handle special cases of 3 words by converting adj + noun (word2 & 3) => obj_name and handle as 2-word case

IDEA: Enable use of root nouns? With error code if multiple same root in scope?
	DONE: 6.5) add root name for all items, doors, and containers => Extend to view_only
	DONE: 6.55) Restructure Interpreter 2-word processing for clarity
	DONE: 6.6) for 2 word commands, test to see if word2 is a known obj_name - if not, test for root_word
	DONE: 6.7) Create function that returns # of instances of root_word in scope and obj_name of last intance
	DONE: 6.8) if returned value = 1 then word2 = obj_name
	DONE: 7.5) If value > 1 Error code could be "I see more than one root_name. Please use the object's full name" (moves - 1)
	DONE: 7.6) if value < 1 then "I don't see a word2 here"
	DONE: Solve for special case of read / writing (is not currently in scope list)

IDEA: Introduce modules
	DONE: Helper functions
	DONE: Research config modules
IDEA: Change approach: class definitions, object instantiation, and helper functions are modules - Interpreter calls them
	DONE: Undo Interpreter module approach
	DONE: Classes module
	DONE: Create config moduel to instantiate object variables
	DONE: Clean up modules

Preposistions
NOTE: All room-based validation happens in the method - the Interpreter just enforces language roles and converts English to method calls
DONE: 7.7) Restructure interpreter to call functions
DONE: 7.8) create put method for container
IN-PROC: 8) in interpreter use lists to identify words as prepositions  ("put")
	DONE: 8.05) Convert noun_handling section into function
	DONE: Create a special handling case for word1 == "put"
	DONE: 8.1) if "in" not in user_input_lst => "I don't see the word 'in' in that sentence"
	DONE: 8.2) send input list between "put" and "in" to noun handling
	DONE: 8.3) send input list from "in" to "end" to noun handling
	DONE: 8.6) try calling put method of container; error out on except
	DONE: Troubleshooting - carefully map out class to getattr in working cases
	DONE: detailed testing - still haven't figured out why trying to put object not in hand doesn't trigger class error??
		DONE: maybe issue is use of hand_lst.remove instead of stateful_dict['hand'] ??
		DONE: Still don't understand problem... put not currently working
		DONE: All that trouble over in hand_lst == False vs. not in hand_lst !!
	DONE: Clean up intpreter
		DONE: noun handling returns too much
		DONE: word2 declaration only for go
	DONE: Create module for most interpreter functions
		DONE: create interp_helper module
		DONE: Test noun_handler in interp_helper - this worked!!

DONE: How to handle a container in a container?
	REJECTED: Only closed containers allowed in containers?
	DONE: You can't open a container in a container?

DONE: 10) Learn what import sys does! (well, I read about it at least)
DONE: 11) error on take of something you already have in hand
DONE: 11.5) maybe need a function to reduce move count on error?
DONE: 11.7) Need a better place to call end... ideally part of a loop independent of main module??
	- No: end as a function called during end condition is fine
DONE: Created static_dict and added it to helper() module
DONE: 11.8): Consider moving 'if hasattr(contains) code to container class?? (e.g. Door examine & open methods)
DONE: 12) Help subsystem: 
		IDEA: The one-word command "help" gives you a list of 2-word help commands: 
		IDEA: "basics", help abreviations", "help verbs", "help one-word-commands", "help preposistions", adjectives, articles
		DONE: Implement 1-word command
		DONE: Implement as 2-word special case call to help function
		DONE: help() function created; 'basics' option written & tested
		DONE: 'verbs' and 'one-word-commands' options written & tested
		DONE: articles & adjectives
		DONE: abreviations, prepositions 
IN-PROC: move stateful_dict['universal'] to static_dict['universal'] ???
	IDEA: This will be harder than I thought - because I am not passing static_dict everywhere
	IDEA: Either I need to start packing variables or I need to stuff everything in stateful_dict???
TBD: Centralize all descriptions into a description_dict declared in a dedicated module


To Do Next:

### Data Strustures ###
IDEA: descriptions in separate descript_dict to be loaded from static text (isolate data & code) ???								
	TBD: Resolve use of descript_dict
	IDEA: static_dict ??
TBD: Implement formal flask code vs. app separation
TBD: Put client-server structure in place early!!

### Cutscene ###
IDEA: Conditional Cutscene Class
IDEA: Conditional_events (a class similar to dcv2 triggers??) => implement for moat ????
	- default, default description, default method
	- special event first time, seft_description, seft_method, count
	- special event additional times, seat_description, seat_method, count

### Score System ###
- Figure out best implementation for scoring


### Creature Class ###


### Switch Classes (button & lever) ###


TBD: Integrate advice from Franco!
	TBD: I think it’s fine to have a big string in your class.  I think it’s also fine to have a separate dictionary or file or db or whatever for big static strings and just put the key into your class.  Or put each object in its own module so you can define a constant nearby but not in the class
	TBD: Use more modules; I would definitely move object instantiation out of the module where the classes are defined.
	TBD: You may also benefit from a single function that takes the object type (Door, etc) as well and instantiates the correct class.	
	TBD: Once you've done that, you might want to have an entire object description in some string format on disk.   I personally kind of like using standard python objects (tuples of strings, mainly) instead of JSON, but YMMV.
	TBD: Try tupples for descript_dict
		Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
	TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )

Expert Questions:
TBD: Std solution for declaring obj variables with reciprocal properties (e.g. writing)
TBD: Can (should) I make the program work without external triggers... can the obj just interact on their own?
	Perhaps the key is to make creatures behave as state machines... 
	each has conditions under which they will guard, attack, gift, etc..
	Also room 'events' with conditionals?


Some Day Maybe
TBD: Is the Item class worth having???
TBD: room.room_stuf => room.room_obj_lst ??


