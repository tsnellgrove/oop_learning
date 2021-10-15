Done List - Dark Castle v3
Oct 15, 2021



##########################
### VERSION 3.01 START ###
##########################

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


##########################
### VERSION 3.10 START ###
##########################

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
	IDEA: how about a module that declares static_dict and is called by all other modules?
	NOTE: Right idea but still needs to be sorted out... it's turtles all the way down
	NOTE: static_dict[] holds objects... so static_init() depends on init() which depends on classes() which depends on helper() which depends on static_init() !!!!
	NOTE: The only way to resolve this dependency is to pass the variable... so I will move universal[] back to stateful_dict 
		NOTE: (to be honest, I might want to add to it durin the course of the game anyhow)
		NOTE: The fundamental rule here is that any global variable that holds objects will need to be in stateful_dict 
	DONE: create dc3_static_init
	DONE: clean up universal[] mess and move it back to stateful_dict
	DONE: clean up comments
	DONE: Move descriptions_dict to static_init
DONE: Centralize all descriptions into a description_dict declared in a dedicated module
	DONE: copy descriptions to static_init() descript_dict
	DONE: change description source from self.desc to description_dict
	DONE: clean up comments in classes()
	DONE: eliminate self.desc attribute in classes() and init()
TBD: At this point declare v3.10 done (update version, clean up files, truncate to-do)
	DONE: create dc3_done.md and move 3.01 to-dos to it
	DONE: Create old_versions and docs folders and move files to them
	DONE: Update version number to 3.10 in static_dict and comments
	DONE: move 3.10 to-dos to done
	DONE: Commit to git with version 3.10 tag	


##########################
### VERSION 3.20 START ###
##########################

NOTE: 3.20 to be all about serialization and main / interpreter separation

IN-PROC: So what data do I need to save between sessions?
	DONE: stateful_dict, Door open & lock states, room contents, container contents
	THINKING: How to load and unload data between moves? where to store it? Need to outline plan
		IDEA: Get started by saving stateful_dict to as JSON to a DB and dumping and loading it each turn
		IDEA: Then maybe programaticaly dump and load stateful object data to a dict? Then save dict as JSON in DB?
		IDEA: Now I'm passing stateful_dict between main and interpreter... but goal is to pass only session ID (end_of_game and out_buff too?)
		IDEA: So how does this actuall work... what is the order?
		IN-PROC: First step is to isolate stateful_dict to the server side...
			IDEA: main should only send user_input and input should only return out_buff and end_of_game
			IDEA: But interpreter has a *lot* of returns... 
			DONE: Maybe the answer is to create a "wrapper" function that calls interpreter?
				IDEA: This works... but now, of course, stateful_dict is always reset to starting values...
		DONE: Once they are isolated, I need to decide where to initiate stateful_dict - perhaps in wrapper?	

TOPIC: serialization
	DONE: I need to learn a lot more about how this works; Things I need to learn:
		DONE: More in general about how DBs are used (Tech with Tim Flask 7 & 8)
		DONE: JSON or Pickle serialization? Investigate Marshmallow!! (YouTube video)
			DONE: watched marshmallow video: https://youtu.be/Gl-5m1_eVjI
			IDEA: Very helpful way to serialize / de-serialize.. from complex to dict...
			IDEA: but how do I handle complex objects that *hold* complex objects???
			DONE: Test multi-level objects with Pet class attribute for Person; focus on Nested format for troubleshooting
			DONE: Can serialize and de-serialize but not to a nested object???
			DONE: Got it working by removing schema def many=True !
			DONE: rationalize tutorial code

Clean Up Code:
	DONE: temporarily re-integrate main & interpreter
		DONE: clean up main
	DONE: introduce print options for classes
	Done: fix object hierarchy
		DONE: Sort out object model - objects should not need to know about things outside of them
			DONE: So writing shouldn't need 'written-on' - just search through objects for matching item (like containers)
				DONE: Created writing_check() to search for writing on objects in scope
				DONE: Elim use of written on
				DONE: Clean up writing changes
				DONE: Make Writing the parent class of View_Only
				DONE: Clean up writing class & init changes
				DONE: create obj_scope helper routine to be used by both scope_check and writing_check
				DONE: clean up helper routine
			DONE: And rooms shouldn't know what they're connected to... perhaps a Map class to hold room connections?
				DONE: decided to implement room connections as a 'path' sub-dict in stateful_dict (no need for actual object)
				DONE: implemented path sub-dict
				DONE: Clean-up commented code
				DONE: Comment out valid_paths attribute
				DONE: Clean-up commented code

DONE: introduce serialization and de-serialization
	IDEA: start from serialized state for stateful_dict and stateful classes
	IDEA: Or maybe just class_to_string as needed before export for stateful_dict??
	DONE: Test serializing to JSON in marshmallow_tut
		DONE: import json
		DONE: convert pet_data back and forth to json
		DONE: convert person_data back and forth to json
	DONE: Start by serializing to JSON and printing stateful_dict
		DONE: Sort out path dict in stateful_dict
			DONE: made all path keys String() to sort out mm Dict requirements
			DONE: Clean up code comments
		DONE: add 'doors' and 'containers' attributes to Room class (and "look" code) to sort out polymorphism issues
				DONE: Convert room_stuff -> room_items
				DONE: Add rooom_doors
				DONE: Add room_containers
				DONE: Clean up code comments
				DONE: Test and update as needed to address room_stuff change
				DONE: Update dc3_mm room schema
				DONE: Add dc3_mm container schema
				DONE: Test dc3_mm json conversion
		DONE: after dumping dict to json, looad the json back to dict and compare to original
			DONE: Initial troubleshooting; add allow_none=True for writing
			DONE: Add post_loads
			DONE: Sort out takeable for Item and Container (changed to takable)
			DONE: Detailed before & after compare
				NOTE: identical by manual inspection but not identical by programatic comparision (i.e. stateful_dict == result_dict => False)
	IN-PROC: Serialize to JSON and print class objects
		NOTE: identical by manual inspections but not identical by programatic comparision (i.e. stateful_dict == result_dict => False)
		DONE: Saved JSON to dict
		IDEA: How reading & writing serialized json stateful_dict to file should work:
			1) If start_of_game == True: load stateful_dict from dc3_default_stateful_json.txt
				DONE: Initial coding
				DONE: troubleshootin of obj id == vs. 'is' compare issues
				DONE: clean-up of troubleshooting comments
			2) Else: load stateful_dict from save_stateful_json.txt
				DONE: Initial coding
			3) At end of wrapper(): Write stateful_dict to save_stateful_json.txt (in overwrite mode)
				DONE: Initial coding
			
ISSUE: I am creating many duplicate objects during de-serialization	
	DONE: Sent email inquiry to Franco to see if I'm taking the right general appraoch to persisting objects - he's not familiar with issue
		DONE: Troubleshoot duplicate object issue (i.e. gate reports as both open and closed)
			IDEA: I can solve the stateful_dict problem by storing only string values and converting to objects after de-serializing (loading)
			IDEA: but when I go to persist the objects themselves I think I will create many more duplicates during de-serialization :(
			DONE: Find a way to list all objects for troubleshooting
			IN-PROC: Try using child schema's in Marshmallow to reduce the count of duplicate objects?
				NOTE: Getting errors due to Nested "base" value (??); How to solve?
			DONE: Return to pre-serialization case and test object counts
				NOTE: Only 1 feront_gate
			DONE: Create stackoverflow ID
			DONE: Create an mwe (minimal workable example)
			DONE: Write up problem for stackoverflow post
			DONE: Post problem on stackoverflow
			DONE: Added pickle to question tags
			DONE: Edited post for output clarity. Read up on reputation (short answer is that I don't have enough to offer a bounty)
			DONE: A bit more research and tuned my post. If no answers soon then I need to go earn some rep and offer a bounty
			DONE: Appears that Pickle will meet my needs - but still no anwsers to my question :(
			N/A: Respond to posts as needed to get answers (no one ever answered)
			DONE: If nothing works for marshmallow, try pickle - sure enough, pickle worked
	DONE: Detailed answer:
		https://stackoverflow.com/questions/68439591/marshmallow-creating-duplicate-python-custom-objects-on-de-serialization/68510952#68510952

DONE: implement pickle for stateful text files
	DONE: comment marshmallow refs and move stateful_dict to init
	DONE: Work out the details of interp_helper declaration calls... maybe re-org interp?? Merge helper files??
		DONE: Move code around to prepare for separate merged module for interpreter and interp_helper
		DONE: clean up old code comments!!!
		DONE: merge interp_helper and interpreter
	IDEA: Approach to Serializing with pickle
		DONE: 1) Have dc3_init put all objects & stateful_dict in obj_lst and write obj_lst to default_obj_pickle file
		DONE: 2) On First Run: load default_obj_pickle; 
		DONE: 3) On finish, call routine to save obj_lst to save_obj_pickle file
		DONE: 4) On Subsequent runs: load save_obj_pickle
		DONE: As feared, obj variable declaration is a challenge... for now, just merge wrapper & interp and do it ugly
		DONE: comment out dc3_init import, comment out stateful_dict passing; Test!!!
		DONE: Still struggling with globalizing object variables... maybe make first pass a special case?? real interpreter always loads save?
			IDEA: Maybe 'if... else...' in main... 
			IDEA: call startup.py module if first pass - which loads defaul, buffers opening, and saves save file... else call interpreter
			IDEA: interpreter assumes load from save pickle and calls config module from module imports
			DONE: created startup() for initial load and then called updated object values from pickle save
			DONE: main and interpreter in separate modules
			DONE: troubleshoot "none itterable" error on "i" or "n"
			NOTE: turns out I wasn't returning values on many of the interpreter returns
		DONE: Amazingly, clode is running - but really shouldn't be - I am frequently NOT saving state on return
			DONE: Need to institute some sort of wrapper() function in interpreter module that will call interpreter and ensure state saves
			DONE: Now save_obj_pickle is not getting over-written in start_me_up() - need to sort that out
			IN-PROC: Turns out I'm not writing pickle_obj_save for some reason... need to give directory??
			IDEA: I get it now... not a directory problem
			IDEA: for some reason (probably because I import wrapper in main) obj_init2 is getting called before start_me_up()
			IDEA: This means that we are reading the OLD values of save_obj_pickle before we over-write them with defaults in start_me_up()
			DONE: How to fix???
			DONE: Got it working - just moved the import of obj_init2 to *after* start_me_up() !!
			DONE: Comment troubleshooting prints
			DONE: Comments clean up!!
	DONE: v3.20 complete!!


##########################
### VERSION 3.30 START ###
##########################

Version 3.30 Goals:
	Create antechamber room and contents
	Start of game assignment for torn note code
	Do some code housekeeping (re-instate polymorphism, elim coding duplication)
	(no creatures, state machines, or conditional events)

DONE: figure out why Working Copy isn't showing old git commits (had to upgrade to Pro)
DONE: for all objects create descript_key field
DOEN: Create base classes and objects
	DONE: create antechamber, torn_note, and messy_handwriting
	DONE: Create protcullis, alcove, and control panel
		DONE: iron_portcullis = Class Door (locked but no key)
DONE: Fix paths dictionary - can't have multiple identical keys
DONE: Eliminate start_me_up
DONE: Sort out initial print - all printing needs to happen in main!!
DONE: Clean up print sort-out comments
DONE: create random number code and attach to messy_handwriting
DONE: Change room objects back to polymorphism (will be glad I did this when switches arrive)
DONE: Clean up comments in classes, demo, & helper
DONE: Clean up double instance of scope check (helper & demo)
DONE: Comment clean-up


##########################
### VERSION 3.33 START ###
##########################

Version 3.33 Goals:
	Update first 3 rooms with full desciptions and view-only objects
	Add 4th room and contents
	Code clean-up / function isolation demo module (??)
	(no creatures, state machines, or conditional events)

DONE: Go back and update descriptions and view-only objects from DCv2
	DONE: Update Entrance and Universal descriptions
		DONE: Add moat object to entrance
		DONE: Capitalize usable nouns in the Entrance
	DONE: Update Main Hall descriptions
		DONE: Remove test objects (chest, brass key, potion)
	DONE: Update Antechamber descriptions
		DONE: How to "lock open" the Iron Portcullis? Need to alter the Class Method to check for locked on close?
	DONE: Add Throne Room and ViewOnly descriptions
		DONE: Add Throne Room items: Throne, Silver Key, Scroll, Letters
		DONE: Add throne_room container: Crystal Box and Calligraphy


##########################
### VERSION 3.35 START ###
##########################

Version 3.35 Goals
	New class for Food

DONE: New Class
	DONE: create Food Class (child of Item) with eat method
		DONE: Crete cheese_wedge obj
		DONE: create stale_biscuits obj (with Trademark)
DONE: Pull eat description from descript_dict
DONE: provide useful error on trying to examine writing (advise player to 'read')
	NOTE: Is non-trivial since 'Writing' does not have an examine method. Added guidance in 'help basic' instead


##########################
### VERSION 3.38 START ###
##########################

Version 3.38 Goals
	New class for Beverage
	random responses to wrong direction commands ;-D

IDEAS: Portcullis Door:
- For portcullis, maybe fix unlock method to say “no keyhole” in key == None ?

IDEAS: For Drink Class
	- Containers can never be taken because they are children of Doors which are children of ViewOnly
	- and we don't want container methods anyhow (open, close, lock, unlock)
	- So create new Jug class as child of Item
	- inspect container scope check… I think it just checks for ‘contains’ attribute? 

DONE: Add "no keyhole" error message on key == NONE (portcullis case)
DONE: Create Jug class to support takeable containers that can't hold anything but Beverage
DONE: Create Beverage Class (child of ViewOnly) with drink method
		DONE: Create glass_bottle obj filled with water obj
DONE: Random wrong direction responese


##########################
### VERSION 3.40 START ###
##########################

Version 3.40 Goals:
	Review interpreter code to understand flow and cases
	Extract method 'execution' and move to a separate routine called by wrapper
	Clean-up unneeded 'return's in bottome portion of interpreter
	implement unknown word random responses

IDEAS (structure):
- Naming convention: Room Events, Warnings, Machines, and Creatures are all types of Conditional Events (CEs)
- Different types of CEs (Conditional Events):
	- Room Events = always pre-action
	- Warnings = always pre-action
	- Machines = always post-action (exisitng machines = control panel, throne, kinging scroll)
	- Creatures = pre-action and post action

FINDINGS (from reviewing interpreter code (true for now at least):
- an error will never trigger a CE
- a true_one_word command will never trigger a CE
+ converted_one_word commands CAN trigger Room Events
	- Note: In this case, "north" is converted to "go north" and is then handled as special case 'go' below
* special case 'go' can trigger a Room Event
* for now at least, no CEs are triggered by special case 'put' commands (but they could be!)
- CEs are not triggered by special case 'help' commands
* final 'try' is where all non-Room Event CEs are triggered

IDEAS (implementation):
- don't need to return to wrapper command strings - could just return case (error, tru_1word, go, help, put, 2_word) and word_lst
- for case == error, tru_1word, or help no need for execution
- for case == go, put, or try - wrapper sends case and word_lst to cmd_execution()
- Check for Room Event triggers before (possibly in place of) cmd_execution()
- Check for Warning triggers before (possibly in place of) cmd_execution()
- Check for Machine triggers after cmd_execution()
- Check for Creature triggers both before and after cmd_execution()

MORE IDEAS: Maybe implement Room Events similar to paths via dictionary in each room obj?
- Still need an obj to hold data for CE and a function to execute it
- Idea is that death by croc would be the Room Event and Saved by Weapon would be a pre-action trigger?

DONE: Review interpreter code to understand flow and cases
DONE: Clean-up 'return's in interpreter to support case approach
IN-PROC: Separate 'interpret' and 'execute method' portions of interpreter()
	DONE: Return 'case' and 'word_lst' to wrapper from interpreter
	DONE: Create cmd_execution() function in demo module; pass it 'case', 'word_lst', and stateful_dict
	DONE: Comment out 'tries' in interpreter()
	DONE: Clean up comments
	DONE: Review / optimize interpreter() code
DONE: Provied 'read help' option that explains where to use examine vs. read
DONE: Improve read error
DONE: implement unknown word random responses in cmd_execute() and interpreter()
IN-PROC: Create a scope_error() function for Class socope checks (they repleat a lot!)
	DONE: put case
	DONE: clean up comments
	DONE: 2word case (non-read)
	DONE: 2word case (read)
	DONE: Fix 2word case
	DONE: Fix water scope checks in class
	DONE: Clean up comments


##########################
### VERSION 3.42 START ###
##########################

Version 3.42 Goals
- Create methods to get & set game_state attributes & introduce GameState class

IDEA (Suggestions from Franco):
- container hasattrib => method in Writing
- implement gets & sets (see Writing get_description example)
- think about implementing stateful_dict as Class = GameState; Could hold dict and create gets and sets to change / access game_state
- Franco: think about using dictionary of functions
- Make scope_check() a method of game_state (which is an obj of class GameState)
- Use gets and sets for objects (including CEs)!! => obj are black boxes
	- Maybe not needed in many cases but since I want to convert code to DB back end is a good idea for my use case
- Franco: consider having a 'game turn' across all or many objects

PRINICPLES:
- encapsulate the sets and gets of all custom object attributes
	- direct object access is a standard pythonic trait... but in my case I plan to eventually move obj attributes to a DB - so this is vital
- If a routine acts on a custom object it should be a method of the object's (or it's parent object's) class
	- Example: get_contents_str()
- if a rountine acts strictly on a Python primative class (e.g. a list) - then it should be a function. 
	- Often this is the case when a routine applies to the attribute of multiple different classes.
	- Example: obj_lst_to_str()
- make methods and functions as functional as possible while still being broadly applicable.
	- For example, if you always need to handle a case for len(list) == 0, handle it in the same function code that produces the non-0 result

IN-PROC: Simple Refactoring
	- DONE: replace hasattr() with is_container() methond [should not be inspecting obj directly]
		- DONE: Create is_container() method in class Writing
		- DONE: Replace hasattr intances
		- DONE: Clean-up comments
	- IN-PROC: search for obj method opportunities in class & demo modules - classes should be black boxes
			- DONE: @property and setters & getters for Writing & ViewOnly
				- DONE: get_full_name(), has_writing(), get_writing_full_name()
				- DONE: invetigate @properties for get_full_name()
				- DONE: convert classes and demo modules back to using full_name via @properties
				- DONE: Clean up comments
				= DONE: Try passing stateful_dict to description routine
				- DONE: Clean up comments
				- DONE: @property for descript_key
				- DONE: clean up comments
				- DONE: reamining setters for Writing & ViewOnly
					- DONE: _name
					- DONE: clean up comments
					- DONE: _root_name
					- DONE: clean up comments
			- DONE: Room class
				- DONE: @property for _features, _room_obj_lst, and _door_paths
				- DONE: clean up comments
				- DONE: container_desc() func => get_contents_str() method of Writing with is_container and is_open tests
				- DONE: clean up comments
				- DONE: obj_lst_to_str() func => obj_lst_to_str() func w/ lst test (ErrorValue) via instance(self, list) ; inlucde str convert
				- DONE: clean up comments
				- DONE: incorporate "nothing" condition into obj_lst_to_str()
				- DONE: Clean up comments
				- DONE: remove room examine scope check - already taken care of via execute scope check
				- DONE: Clean up comments
				- DONE: encapsulate room.door_path access in get methods
			- DONE: Create GameState class & game_state obj
			- DONE: attributes = dynamic_desc_dict, map_dict, static_obj_dict (holds universal), state_dict
			- DONE: implement dynamic_desc_dict
				- DROP: figure out @property usage for dicts
				- DONE: create setter & getter for dynamic_desc_dict
				- DONE: Figure out where to declare game_state and how to reference it in classes... send email to Franco
				- DONE: implement boostrap routine as suggested by Franco
				- DONE: comment clean-up
				IN-PROC: implement map_dict
					- DONE: Create getters
					- DONE: Initial troubleshooting
					- DONE: more complex troubleshooting
					- DONE: obj ID not being retained with game_state... 
					- DONE: have proven that obj start with same IDs (in dc3_init module)
					- DONE: investigate wrapper save... maybe call save module??
					- DONE: Now antechamber fails after Entrance but works after Throne Room... need review class coding carefully
						- IDEA: This happens because I am testing with game_state for 'passages' but 'stateful_dict' for open doors...
						- IDEA: so Entrance => Main Hall = open door = works
						- IDEA: Main Hall => Antechamber = passage = fails
						- IDEA: Antechamber => Throne Room = open door = works
						- IDEA: Throne Room => Antechamber = open door = works
					- DONE: setup testing to print Antechamber id vs. game_state Antechamber id every turn and figure out where they diverge
						- DONE: map out module calls
						- DONE: ensure that game_state is not declared multiple times during classes moduel calls (didn't seem to change anything)
						- IDEA: fundamentally I think I am defining all variables twice somehow... 
						- IDEA: and because game_state is declared early it is getter the first assignment and conflicting with the 2nd
						- DONE: create print statements to track pickle dumps and loads
						- DONE: Review and confirm module model
						- DONE: looks like pickle is only loaded once during wrapper import (???); try moving pickle load to wrapper loop
						- IDEA: investigated creating a separate dc3_wrapper module that would then call interpreter & cmd_execute from demo...
							- IDEA: this won't work... wrapper needs access to stateful dict...
							- NOTES: I confirmed that, by default, pickled objects don't retain their obj id
							- IDEA: I'm thinking here's what I need to do:
								- DONE: 1) return to pickle loading in wrapper at the start of every loop (and stop calling init2)
								- DONE: 2) pack obj variables and pass them to interp and cmd_exe (or maybe pass as master_obj_lst ??)
						- NOTES: I am now pickle dumping & loading every turn in wrapper and formally passing obj to interpreter - an am *still* getting dups in classes get_next_room() method... I need to double down on troubleshooting this method in ugly detail 
							- DONE: check if there is a duplicate of of game_state - there is
							- DONE: Determine when duplicate game_state is created => after init but before middle of wrapper
							- NOTE: One version of game_state keeps the same id from the start... presumably this is not the pickled version?
							- TBD: Keep troubleshooting to find out exactly where the duplicate game_state shows up; special focus on classes declaration
						- NOTES: So, the original game_state is not getting deleted, and now that I'm instantiating a new version I get 2 old game_state versions... need to dig deep into the classes bootstrap - that's where the issue lives... game_state1 never gets deleted and game_state2 gets created twice... ???
						- I fundamentally need to reconsider my bootstrap approach... I will go back to adding values....
						- NOTES: turns out I have duplicates of other obj (Doors) as well
						- DONE: figure out why delete is not working in init; also, why dups?? - learning more about gc.get_objects() and sys.refcount()
						- DONE: Try checking refs on problem version of obj?? - Both obj sets have many ref (but first static set has more)
						- NOTE: there are 2 obj sets - the initial one from init declaration that never changes id; And a 2nd set that changes every move... presumably loaded from the pickle? It appears that we don't actually need to load from pickle?
						- DONE: track problem antechamber obj id - so the PROBLEM is the FIRST set of objects... the ones that never change... perhaps they never get updated?? For some reason, game_state._paths is pointing to this first set... and when they are called no room_obj can be interacted with... ???
						- DONE: tested running dc3_init on its own (to initialize the pickle dump), commenting out the import of dc3_init, and then running main - worked great until tried to go to antechamber (key error on game_state._paths)... so this seems to be the answer!
						- DONE: check refs on gamestate at end of class (5 references)
						- DONE: Create start_of_game variable in main and pass to wrapper
						- DONE: Move initial room print to wrapper start of game routine
						- IN-PROC: Still need to figure out how to avoid game_state dup... that's my one problem case... maybe delete at end of class?
							- IDEA: maybe a custom start_of_game case where defautl_pickle doesn't include game_state (NO GAMESTATE IN DEFAULT PICKLE)
							- IDEA: game_state gets updated and added to new game pickle? then pickle is immediately loaded in main routine?
							- DONE: Create a "default pickle" file to load (and a script to gen it up)
							- DONE: in start_of_game section of wrapper, load default_obj_pickle (NO game_state included)
							- DONE: in start_of_game section of wrapper, configure game_state
							- DONE: in start_of_game section of wrapper, dump save_obj_pickle2 (WITH game_state included!)
						- NOTE: Again, there are 2 obj sets - the initial one from init declaration in the start-up section of wrapper, that never changes id; And a 2nd set that changes every move... the PROBLEM is the FIRST set of objects... the ones that never change... For some reason, game_state._paths is pointing to this first set... and when they are called no room_obj can be interacted with... ???
							- NOTE: I seem to be back where I started... I think the next step is to make wrapper "start-up" a separate module... if that doesn't work - and I don't think it will - I need to go back and re-diagram the whole thing based on what I now understand about variables and objects
							- DONE: Create start-up module (no change in duplicates)
							- IDEA: so now I have isolated the initial object declarations in start_me_up() and the every-turn declarations in wrapper() in separate modules... and I still have the duplicates issue...
							- DONE: clean up comments and trouble-shooting - need to make the code readable again
							- DONE: v1 detailed module / imports mapping
							- DONE: v2
							- DONE: Track program flow to determine order of ops
							- DONE: Analyze code run order - in what order does my code actually run? Number on diagram
							- IDEA: Maybe classes, static, and helper in memory from main?? Convert calsses to function??
							- DONE: tired converting classes to a function in a classes2 module... 
								- NOTES: this doesn't work either because the class definition remains in the scope of the classes2 module... 
								- NOTES: so start_me_up knows nothing about GameState...
							- IDEA: Instead, I need to make 2 separate modules: define_class_gs and define_class_other..
								- IDEA: then I import each in the body of start_me_up and wrapper
								- IDEA: in start_me_up, between the class definitions, I declare game_state
								- DONE: create define_class_gs and define_class_other
								- NOTES: Making progress but now define_class_other knows nothing about game_state... need to find a way to pass it in?
								- NOTES: No, issue is that game_state has not yet been defined in wrapper
								- DONE: updated description method so that game_state is not required
								- DONE: pass game_state in to go method!!! (suggested by JE)
								- NOTES: Yes - THIS WORKS!!! NO DUPS!!! 
							- DONE: full implementation of game_state._paths
							- DONE: rename game_state to active_gs
							- DONE: comment clean up
							- DONE: now that I'm passing active_gs, simplify classes => single standard import
							- DONE: Mark unused modules
							- DONE: move active_gs declaration to default_pickle
							- DONE: clean up comments
							- DONE: Declare v3.42 complete!


##########################
### VERSION 3.44 START ###
##########################

Version 3.44 Goals
- After the massive mess that was the introduction of GameState in v3.42 the goals of 3.44 are hopefully simpler
- 1. With troubleshooting messages still in place, re-architect modules
- 2. sort out efficient variable handling
- 3. eliminate bad usage (e.g. eval and global)
- 4. re-map module calls
- 5. clean-up troubleshooting prints and comments 

DONE: move wrapper() to its own module
DONE: fully comment out old wrapper within dc3_demo
DONE: sort out interpreter()
	DONE: Sort out "put" command
	DONE: Sort out interpreter master_obj_lst declaration & passing - commented out
	DONE: found and fixed small_print => small_printing error (root_name conflicted with reserved command 'print')
	DONE: move stateful_dict and active_gs to front of declarations
	DONE: sort out use of eval
	DONE: sort out noun_handling master_obj_lst declaration & passing
	DONE: clean up comments
	DONE: update word2 => word2_txt in noun_handling()
	DONE: do I really need to pass stateful_dict to interpreter() & noun_handling() if I'm already passing master_obj_lst
		- DONE: stop explicitly passing stateful_dict to interpreter()
		- DONE: clean up comments
		- DONE: stop explicitly passing stateful_dict to noun_handling()
		- DONE: clean up comments
	DONE: examine limits to declarations in start_me_up and wrapper
		- DONE: remove full obj declarations from start_me_up() and just declare stateful_dict and active_gs
		- NOTE: garbage collection still has all obj in scope once master_obj_lst is unpickled!
		- DONE: comment clean-up
		- DONE: remove full obj declarations from wapper() and just declare stateful_dict and active_gs
		- DONE: comment clean-up
	DONE: move help, error, and tru_1word case execution from interpreter() to cmd_execute()
		DONE: move help routine to cmd_execute()
			DONE: move help() call to cmd_execute()
			DONE: clean up comments
			DONE: clean up help() routine
			DONE: clean up comments
		DONE: move tru_1word routines to cmd_execute()
			DONE: move true_one_word() call to cmd_execute()
			DONE: move true_one_word() to cmd_execute() and move inventory() to dc3_helper()
			DONE: clean up comments
		DONE: move error output & turn decrementing to cmd_execute()
			DONE: exit_state => error_state in both noun_handling() and interpreter
			DONE: pass interpreter() errors to cmd_execute() and update wrapper and add move_dec()
			DONE: pass noun_handling() errors to cmd_execute()
			DONE: clean-up comments
			DONE: update wrapper
			DONE: move random routine to cmd_execute()
			DONE: clean-up comments
	DONE: move interpreter() to its own module
		DONE: create dc3_interpreter()
		DONE: migrate interpreter() routines to dc3_interpreter module
DONE: sort out cmd_execute()
	DONE: move ALL case execution to this module
	DONE: move cmd_execute() to its own module
DONE: fix any remaining 'Someday's below
DONE: make end() a module and call from wrapper()
DONE: create dc3_score() module based on stateful_dict values and call from wrapper
	DONE: create score_val_dict in dc3_static
	DONE: create points_earned_dict in stateful_dict (same key as score_val_dict)
	DONE: call score() from wrapper()
	DONE: complete and test score(
DONE: Full testing (note: there's still an extra call of helper() from main that I don't quite understand: SOLVED! artifact from helper in end)
DONE: re-map modules and var passing
DONE: clean up troubleshooting comments & prints!!!
DONE: move un-unsed modules to 'old versions' directory
DONE: finalize version

Someday: fix game_state as global
Someday: fix root-word var passing of master_obj_lst
Someday: clean up *very* ugly master_obj_lst passing 
	- really the only function that needs this is the one that converts strings to obj...
	- maybe I can solve that by just passing master_obj_lst and checking to see if str = the name of a member of master_obj_lst
	- or Someday: Eliminate eval using class-based-dict; link: https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
someday: do we really need to declare objs in wrapper??
	- can I just load master_obj_lst from the pickle and pull from it selectively?
	- the only thing I really need to use all the time out of master_obj_lst is stateful_dict and active_gs
someday: ditto for start_me_up


##########################
### VERSION 3.46 START ###
##########################

Version 3.46 Goals:
- Refactor code to migrate variables from stateful_dict => active_gs

Notes:
- Approach is to migrate variables one sub-dict at a time
- Within main dict, migrate one var at a time

DONE: Refactor stateful_dict['paths']
DONE: Refactor stateful_dict['points_earned_dict']
	DONE: add points_earned_dict to GameState vars and define active_gs values in make_default_pickle()
	DONE: pass active_gs to dc3_score
	DONE: create method to get and set score state for a given score_key
	DONE: For items - update score() to use active_gs score state
	DONE: For rooms - update score() to use active_gs score state
	DONE: comment out stateful_dict points_earned_dict
	DONE: clean up comments
DONE: "Easy" use cases = 'current_score', 'score', 'move_counter', 'end_of_game', 'game_ending'
	DONE: current_score & score
		DONE: add 'score' to active_gs.state_dict (and clean up class_deff comments & prints)
		DONE: create increase_score() method for GameState
		DONE: update score() function to call increase_score() method
		DONE: create get_score() method in GameState
		DONE: update print_score() func in helper module to call get_score() method
		DONE: comment out 'score' in stateful_dict
		NOTE: is stateful_dict['score'] even being used???
		DONE: comment out 'score'
		DONE: clean up comments
	DONE: 'move_counter'
		DONE: add 'move_counter' to active_gs.state_dict
		DONE: create 'move_inc' method in GameState to increment moves
		DONE: create 'move_dec' method in GameState to decrement moves
		DONE: update wrapper() with move_inc
		DONE: update cmd_exe() 'errors' and 'quit' with move_dec
		DONE: create 'get_moves' method in GameState
		DONE: update end() with get_moves
		DONE: comment out 'move_counter' in stateful_dict
		DONE: clean up comments
	DONE: 'end_of_game' & 'game_ending'
		DONE: add 'end_of_game' & 'game_ending' to active_gs.state_dict and run mk_default_pkl()
		DONE: create get & set 'end_of_game' in GameState
		DONE: create get & set 'game_ending' in GameState
		DONE: update 'quit' in cmd_exe() with set_game_ending
		DONE: update wrapper() with get_game_ending & get_end_of_game
		DONE: update end() with get_game_ending and set_end_of_game
		DONE: update start_me_up()
		DONE: test updates
		DONE: comment out 'end_of_game' & 'game_ending' in stateful_dict & run mk_defaul_pkl()
		DONE: clean up comments
DONE: 'universal'
	DONE: add 'universal' to active_gs.state_dict and run mk_default_pkl()
	DONE: create get_static_obj method in GameState
	DONE: in cmd_exe() '2word' and 'put' cases pass active_gs to scope_check() & writing_check()
	DONE: in helper() pass in active_gs to scope_check() & writing_check() and pass active_gs to scope_list()
	DONE: in helper() pass in active_gs to scope_list and update 'universal_lst' with get_universal_scope
	DONE: from noun_handling(), pass active_gs to root_word_count()
	DONE: from root_word_count, pass active_gs to scope_lst()
	DONE: test updates
	DONE: comment out 'universal' in stateful_dict and run mk_default_pkl()
	DONE: test updates
	DONE: clean up comments
DONE: pass active_gs to all class verb methods
	DONE: troubleshoot examine.door error
		DONE: solve bug (scope_check in examine sub for door)
		DONE: clean-up comments
	DONE: '2word' case = read
		DONE: in "try" from '2word' case create if 'read'
		DONE: add active_gs to method
		DONE: test
	DONE: '2word' case = eat
	DONE: '2word' case = drink
	DONE: '2word' case = take
	DONE: '2word' case = drop
	DONE: '2word' case = close
	DONE: '2word' case = lock
	DONE: '2word' case = unlock
	DONE: '2word' case = open (2 methods)
		NOTE: learned I need to pass active_gs in super
	DONE: '2word' case = examine (many methods!)
		DONE: Update in cmd_exe() tru_1word() too
		DONE: Update in Room 'go' method in class_def()
	DONE: remove if & try for 2-word case
	DONE: clean-up comments
	DONE 'put' case
		DONE: put => active_gs
	DONE: in cmd_exe() create rand_error() function
DONE: Refactor stateful_dict['dynamic_desc_dict']
	DONE: move dynamic_desc_dict from stateful_dict to active_gs
	DONE: comment out stateful_dict sub-dict and re-run mk_default_pkl
	DONE: clean up comments
IN-PROC: 'backpack'
	DONE: add 'backpack' to active_gs
	DONE: investigate 'backpack' usage
	DONE: create get_backpack_lst method in GameState
	DONE: create backpack_lst_append method in GameState
	DONE: create backpack_lst_remove in method GameState
	DONE: add active_gs backpack methods to modules and comment out stateful_dict
		DONE: Update scope_lst() in helper(), inventory() in helper(), take() method in Item class_def()
		DONE: comment out stateful_dict
		DONE: clean up comments
DONE: 'hand'
	DONE: add 'hand' to active_gs
	DONE: create methods: get, append, remove
	DONE: Update helper(), class_def(), & score()
	DONE: comment out stateful_dict 'hand'
	DONE: testing!!
	DONE: clean-up comments
TBD: 'room'
	DONE: add 'room' to active_gs
	DONE: create methods: get & set
	DONE: update score(), helper(), cmd_exe(), interpret(), class_def()
	DONE: comment out stateful_dict 'room'
	DONE: detailed testing: score(), helper(), cmd_exe(), interpret(), class_def()
	DONE: clean-up comments
IN-PROC: 'out_buff' & buffer()
	DONE: add 'out_buff' to active_gs
	DONE: create methods: get & buffer
	DONE: in wrapper(), get and combine both stateful_dict and active_gs buffers and pass the combined out_buff to main()
	IN-PROC: update modules:
		DONE: document N/A modules: score(), interpret(), mk_default_pkl(), wrapper(), static(), main()
		DONE: end()
		DONE: create reset_buff method in GameState and call it in wrapper()
		DONE: start_me_up()
		DONE: helper()
			DONE: print_score()
			DONE: inventory()
		DONE: cmd_exe()
			DONE: help()
			DONE: true_one_word()
			DONE cmd_exe()
		IN-PROC: class_def()
			DONE: Writing()
				DONE: print_contents_str()
				DONE: read()
			DONE: ViewOnly()
				DONE: examine()
			DONE: Room()
				DONE: examine()
				DONE: go()
			DONE: Item()
				DONE: take()
				DONE: drop()
			DONE: Door()
			DONE: Container()
			DONE: Food()
			DONE: Beverage()
	DONE: test without stateful_dict buffer being added to out_buff		
	DONE: comment out stateful_dict 'buffer'
	DONE: detailed testing
	DONE: clean-up comments
	DOEN: update version comment, version static value, and tag in repo, more doc => done

