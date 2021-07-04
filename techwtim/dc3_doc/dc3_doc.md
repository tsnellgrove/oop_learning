To Do List - Dark Castle v3
July 2, 2021



##########################
### VERSION 3.20 START ###
##########################

TBD: 3.20 to be all about serialization, DB integration, and main / interpreter separation

IN-PROC: Watch YouTube vid on SQLAlchemy: https://youtu.be/51RpDZKShiw
	DONE: Create practice file
	DONE: Watch video
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
		DONE: instantiate sqlalchemy DB
				DONE: Queue huge sdk issues due to ancient version of sqlalchemy...
				DONE: Have upgraded to version 1.1.2 using Stash but still getting issues in sqlite compiler
				DONE: Think I might have to upgrade to 1.4.x to get JSON support for sqlalchemy.dialect.sqlite (installed 1.4.18)
				DONE: now requires install of importlib_metadata (installed via 'pip install')
				DONE: now I need to 'pip install typing_extensions'
				NOTE: APPEARS TO WORK!!!

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

NEXT:
	DONE: temporarily re-integrate main & interpreter
	DONE: clean up main
	DONE: introduce print options for classes
	TBD: fix object hierarchy
		TBD: Sort out object model - objects should not need to know about things outside of them
			IDEA: So writing shouldn't need 'written-on' - just search through objects for matching item (like containers)
			IDEA: And rooms shouldn't know what they're connected to... perhaps a Map class to hold room connections?
	TBD: introduce serialization and de-serialization
		TBD: start from serialized state for stateful_dict and stateful classes
			TBD: Or maybe just class_to_string as needed before export for stateful_dict??
	TBD: isolate main & interpreter using txt file loads
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
