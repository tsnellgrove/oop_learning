# dark castle 3 demo to-dos

# NEXT: Tom Example
# inheritance
# Create Door as child of Item [DONE]
# Create ViewOnly as parent to Item [DONE]
# Create Container as child to door [DONE]
# Create take & drop methods for Item [DONE]
# Create unlock method for Door & Container [DONE]
# Create open method for Door [DONE]
# Create a Room child class of view_only... focus on inventory only - not movement [DONE]
# Exercise inventory management using Room.room_objects and hand and take and drop [IN-PROC]
	# Update Room examine, take, and drop [DONE]
	# DONE: Test implementation
	#DONE: add takability to the 'take item' method
# DONE: More tutorials before this gets out of hand!
# Note: I think I'm doing something wrong... 
#		inventory management with objects is not as elegant as I was expecting

# DONE: Too many calsses already... think about consolidation
# Decision: Inheritance is complicated, Multi-Inheritance is more complicated, 
#		and multi inheritance from inherited classes... is just right out!
# DONE: So => make 'takable' a local attribute of container

# Idea: Rooms are really just conneectd containers...
# DONE: Link travel to doors or to rooms? For now deciding on rooms
# DONE: Troubleshooting movement
# DONE: Implemnt doors in rooms

# DONE: Implement While True input loop
# DONE: Fix input conversion
# DONE: Fix go command - interpreter
# DONE: Description of new room on change rooms
# DONE: Enforce room.examine() based on location
# DONE: Implement 'look'
# DONE: Update room based on go (try global room)
# DONE: Pass room variable to class methods (state_dict)
#	DONE: Troubleshoot "examine gate"... maybe implemnt room across all methods first??

# DONE: Think through writing attribute for ViewOnly 
#		(i.e. should be read dwarven_runes instead of read sword)
# IDEA: Maybe what I want to do is create a method that can put one item *on* another... 
#		so that I can put the writing *on* the item?
# IDEA: Similar problem to a container... need a list of things that can be *on* the item - 
# IDEA: should be at the ViewOnly level since many objects can have writing on them...
# IDEA: nead a name... maybe 'features'
# IDEA: this could also be used for control panel

# DONE: Extend examine() for class Door to include open or close state
# DONE: Fix read_writing => read
# DONE: Implement 'close'
# DONE: Implement 'lock'

# DONE: Implement features
# DONE: Writing as class
# DONE: Implement read for ViewOnly class
# DONE: Extend examine method for classes Room and Door (vs. replace)
# DONE: Test read for Door class
# DONE: Move 'features' to Room class (since we only examine room features)
# DONE: Re-add 'features' to ViewOnly class - 
#		because otherwise there is no way to include it in examine_lst
# DONE: Add presence checking for examine on Door and Room classes

# DONE: Implement containers
# DONE: Decide how container contents should be presented and added to examine and take scope
# DEC: Show container contents with hasattr upon open and then add to room objects
# DONE: Implement 'open' case for containers (troubleshoot and implement case of empty containers)
# DONE: Implement / Troubleshoot 'close' case for containers
# NOTE: Implemented close reduction of room_objects via sets which leads to re-order

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
# DONE: I think this in turn means 
#		that the *item* needs to know what container it's in (like writing)?...
#		No... let's keep items 'dumb'... 
#		it's the room's job to know what's in the room 
#		and it's the container's job to know what's in the container... 
#		to implement this we just reverse the take scope process... 
#		we start with a for loop of open containers and remove from there if possible
#		else remove from room_objects
# NOTE: I didn't have these issues in the old Dark Castle 
#		because I had no 'close' command... 
#		so I could safely dump the contents of any container 
#		into room_obj the moment the container was openned. 
#		Now that containers can be closed I need to actually solve this problem.
# NOTE2: Should writing work this same way?
#		No - I think it makes sense for writing to know what it's on..
#		Because the two are entwined... 
#		the writing on one object can never move to another
# DONE: Add 'the container is empty' description for empty containers
# DONE: Can't examine items in open containers... 
#		need to add open container contents to examine_lst

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

*** Interpreter and Origanizational Coding ***
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
DONE: 0.6) time to implement backpack?
0.63) Every scope search happens in a room, and every room has a feature list - so why are features different in scope function?
0.65) review dkv2 verb methods... maybe move fail statements to top??
0.7) convert to true flask vs. app structure
	0.73) fix 'quit'
	0.76 fix 'start'
1) Every noun as an obj_name, full_name, root_name
2) All one_word commands => 1_word function
3) use lists to identify words as nouns, verbs, adjectives, articles, and prepositions
4) if sentence does not start with a verb => please start with a verb
5) if multiple nouns, verbs, articles, or preps in a row => I don't undderstand that setence error
6) Convert adjectives + noun => obj_name
7) If no prep => verb_noun function
8) If prep: Identify direct object and => prep_sentence function
NOTE: All room-based validation happens in the method - the Interpreter just converts English to method calls

TBD: Interpreter review!!!
TBD: Put command
TBD: Implement formal flask code vs. app separation

TBD: How to handle a container in a container?
	IDEA: Only closed containers allowed in containers?
	IDEA: You can't open a container in a container?

TBD: Put client-server structure in place early!!

Expert Questions:
TBD: Std solution for declaring obj variables with reciprocal properties (e.g. writing)
TBD: Can (should) I make the program work without external triggers... can the obj just interact on their own?
	Perhaps the key is to make creatures behave as state machines... 
	each has conditions under which they will guard, attack, gift, etc..
	Also room 'events' with conditionals?


Some Day Maybe
TBD: Implment container.put(item) ???
TBD: Is the Item class worth having???
TBD: room.room_stuf => room.room_obj_lst ??


