To Do List - Dark Castle v3
July 11, 2021


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

IN-PROC: implement pickle for stateful text files
	DONE: comment marshmallow refs and move stateful_dict to init
	IN-PROC: Work out the details of interp_helper declaration calls... maybe re-org interp?? Merge helper files??
		DONE: Move code around to prepare for separate merged module for interpreter and interp_helper
		TBD: clean up old code comments!!!
		TBD: Move merged_interp to dedicated module separate from wrapper and main
	IDEA: Approach to Serializing with pickle
		TBD: 1) Have dc3_init put all objects & stateful_dict in obj_lst and write obj_lst to default_obj_pickle file; comment out dc3_init import
		TBD: 2) On First Run: load default_obj_pickle; 
		TBD: 2.1) On First Run: Pass list to module to declare obj from list; call same module from interp_helper (?)
		TBD: 3) On finish, call routine to save obj_lst to save_obj_pickle file
		TBD: 4) On Subsequent runs: load save_obj_pickle
		TBD: 4.1) On Subsequent runs: Pass list to module to declare obj from list; call same module from interp_helper (?)
		



TBD: Once stateful_dict is solved, extend txt file saves to object instantiation
	TBD: serialize to JSON and save class objects to text file
	TBD: Change to saving to lists so that list of lists can dump and load using correct schema ??
	TBD: Import class objects from JSON
	TBD: On start, import class objects from default_obj text file; on following runs save and load from save_obj text file

TBD: isolate main & interpreter using txt file loads
	TBD: stop passing stateful_dict
	TBD: move main to d3_main.py




##########################
### VERSION 3.30 START ###
##########################

NOTE: 3.30 to be all about DB integration

DONE: Watch YouTube vid on SQLAlchemy: https://youtu.be/51RpDZKShiw
	DONE: Create practice file
	DONE: Watch video

DONE: instantiate sqlalchemy DB
	DONE: Queue huge sdk issues due to ancient version of sqlalchemy...
	DONE: Have upgraded to version 1.1.2 using Stash but still getting issues in sqlite compiler
	DONE: Think I might have to upgrade to 1.4.x to get JSON support for sqlalchemy.dialect.sqlite (installed 1.4.18)
	DONE: now requires install of importlib_metadata (installed via 'pip install')
	DONE: now I need to 'pip install typing_extensions'
	NOTE: APPEARS TO WORK!!!

TBD: now start working with sqlalchemy again in place of txt files
	TBD: How do I setup a DB that continues to persist independent of an app running??
	TBD: Before returning values, Interpreter must save stateful_dict to DB
	TBD: Before running code, must load the value of stateful_dict from DB
	IDEA: default object values should start as a DB entry (or txt files) and be loaded on new game
		
		


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
	IDEA: avoid external triggers - create classes / state-machines
		Examples: conditional_cutscenes (moat, ending), antagonistic_guard (goblin), hungry_guard (hedgehog1), trader (hedgehog2)[introduce "give" verb, dispenser (throne), lever, button
TBD: How should modules be inter-related (presumably minimally)

Some Day Maybe
TBD: Is the Item class worth having???
TBD: room.room_stuf => room.room_obj_lst ??
TBD: Need to dis-entangle modules better


### New Puzzle Ideas ###
- Can sharpen and clean sword in mouse hole - maybe only way to get past goblin

5.x Additional rooms
	Have portait of Willie revealed in throne room and give player mouse hole and time travel quest
	5th room
		mouse hole - to exercise existing capabilities (e.g. "food" that can be eaten)
		copper key opens cabinet which holds potion
		find a use for 'close' verb; maybe potion refill
		possibly create 'return' verb to put things back (or maybe 'swap')
		potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
		enter mouse hole
		maybe fight mouse?
		silver key in mouse trap; need to swap with copper key
		find a use for close command?
		would be fun to use every verb ;-D
		maybe a guard mouse that only lets you past if you're wearing the hedgehog_broach
		Indiana Jones reference for mouse trap and ball chasing you out ;-D
		make hedgehog_broach wearable
		link puzzle to total number of moves? Or to score?
		repeat option like 'again' / 'g' in Zork (JE request)
	Possibly add a room 6 with time travel??
		find a use for the word "griffonage" (illegible handwriting)
		Opportunity to include princess in game - perhaps have Willie give her the hedgehog_broach to time travel
		Depict future (opportunity but challenges) by painting to portrait
		Also get key from time travel - put in container and then refind 100 years later
		loose brick in dark_alcove - "appears not to have been disturbed for 100 years"
		guard with key_detector in main hall
		trade keys with princess? give her the hedgehog broach? maybe during dance in throne room
		dungeon down stairs from throne room
		in throne room 3 paintings of past and 1 blank space for future
		key to open dungeon?
		keys same colors as ready player 1

5.x Future Ideas:
	fun idea - small creature - like a mouse - as an item
	more directions
	landscape / path changes
	create 'win' test routine with checksum
