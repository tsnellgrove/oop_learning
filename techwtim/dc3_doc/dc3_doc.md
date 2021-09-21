To Do List - Dark Castle v3
Sept 5, 2021


##########################
### VERSION 3.42 START ###
##########################

Version 3.42 Goals
- Create methods to get & set game_state attributes

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
						- TBD: Try checking refs on problem version of obj??
						 

Someday: fix root-word var passing of master_obj_lst
Someday: Eliminate eval using class-based-dict per this link: https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
Someday: clean up *very* ugly master_obj_lst passing - really the only function that needs this is the one that converts strings to obj... and maybe I can solve that by just passing master_obj_lst and checking to see if str = the name of a member of master_obj_lst

		
##########################
### VERSION 3.45 START ###
##########################

Version 3.45 Goals
- Migrate stateful_dict to one or more game_state obj (refactor stateful_dict => object game_state(state_dict, statict_dict) )
- most helper() functions will become methods of game_state
- end() will become its own module called by wrapper

TBD: Refactor stateful_dict


##########################
### VERSION 3.48 START ###
##########################

Version 3.48 Goals
- Refactor module architecture

- IDEA: Full separation on interpreter() and cmd_execute()
- IDEA: Module architecture - separate modeule for wrapper and each wrapper component (including 'pre-trigger', 'post-trigger', & 'end')

	
##########################
### VERSION 3.50 START ###
##########################

Version 3.50 Goals
- Room Events (pre-action trigger) - maybe using exec()
- implement scoring



### Cutscene ###
IDEA: Conditional Cutscene Class
IDEA: Conditional_events (a class similar to dcv2 triggers??) => implement for moat ????
	- default, default description, default method
	- special event first time, seft_description, seft_method, count
	- special event additional times, seat_description, seat_method, count
	- track numbrer of times CE is run?
	- Or maybe just binary cond_event_exists in each obj?
	- also need to distinguish pre=action vs. post-action (e.g. 'take sword' vs. 'read lettering' or 'push button')
	- also need to distinguish 1-time events (e.g. croc) vs. every-time events ('take sword') vs. warnings (e.g. 'eat biscuits')


More ideas on Conditional Events:
- Would like Room Events to be somehow linked to the Room obj so that you can inspect obj and know there will be a CE
- field in each object for associated conditional event
- Idea is that Interpreter returns standard_command and noun_obj to wrapper
- wrapper checks for noun_obj.event_lst > 0 and sends to event checker routine which returns event_output if appropriate
- (could be more than one event so likely a for loop here)
- if no relevant event then output gets standard_output (generated from interpreter command)
-  events: conditional-command-list, conditions (list of lists; outer = AND; inner = OR), event-text, events (list); check for end of game in wrapper

Additional Creature and Conditional Event thoughts:
- Conditional Events could be warnings - not hard stops (e.g. 'eat biscuits')
- In theory could have order of operations considerations:
- (e.g. what if a monster causes darkness but you have a sword that glows around monsters?)
- I don't think these will be a common problem that I need to code for - but worth thinking about
- presently my creatures are not mobile but maybe someday?
- What about timers? Maybe timers are associated with events and creatures and switches? Presumably they need to be triggered somehow?

TBD: Scoring (probably in wrapper?)

##########################
### VERSION 3.x START ###
##########################

Version 3.x Goals
	levers, and button => and machines!
	Lever and Button objects
	Working portcullis puzzle

IDEA: Create Machine class
		- Complex machines have at least 2 inputs (vs. doors)
		- Control Panel is a machine (also throne, radio, and baking machine)
		- Have 'help machines'
		- Logic, outcomes, & descriptions live in machine - button just starts, levels just set values
		- Machine obj also includes list of 'controls' (3x levers and button)
		- (For fun, baking machine should have lever to start and buttons to set values)
		- Buttons & Levers are dumb
			- Levers only know if they are up and down and how many times pulled
			- Buttons only know if phushed this turn and how many times
		- Machine state is checked each turn in wrapper (similar to conditional events & creatures)
			- Machine checked based on room
		- Should logic be in machine or in attached conditional events??
	TBD: Create class LeverSetVal and objects left_lever, middle_lever, right_lever
		TBD: Create method pull()
			TBD: set lever value based on up or down (start down; down = 0)
	TBD: Create class ButtonToggleIfVal and object red_button
		TBD: Create method push()
			TBD: on push check value; if value then toggle state else nothing; descript text for success and fail
TBD: random responses to wrong direction commands ;-D
TBD: implement scoring


*** Someday Maybe ***
TBD: Clean up non-door 'go' method in dc3_classes Room class (avoid code reuse)
TBD: Figure out a way in web browser to show all adventure text in scrolling window
TBD: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
TBD: maybe break interpreter code into more functions within demo module (since I now have global vars)?
TBD: Normalize scope_check() for objects of class Writing?


*** How to Add Objects ***
1) If needed, create Class and methods in dc3_classes
2) Add object in dc3_init
2.5) Add object to room in dc3_init
3) Add object description in dc3_static_init
4) Add object to master_obj_lst in dc3_init
5) NO LONGER NEEDED: (Add object to master_obj_lst in dc3_startup)
6) Add object to master_obj_lst in dc3_obj_init2


##########################
### VERSION 3.xx START ###
##########################

Version 3.xx Goals:
	all about DB integration

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

### Data Structures ###
IDEA: descriptions in separate descript_dict to be loaded from static text (isolate data & code) ???								
	TBD: Resolve use of descript_dict
	IDEA: static_dict ??
TBD: Implement formal flask code vs. app separation
TBD: Put client-server structure in place early!!



### Score System ###
- Figure out best implementation for scoring


### Creature Class ###


### Switch Classes (button & lever) ###

More obj Ideas:
- score obj ?
- timers as obj
- 'warnings' as obj


TBD: Integrate advice from Franco!
	TBD: I think it’s fine to have a big string in your class.  I think it’s also fine to have a separate dictionary or file or db or whatever for big static strings and just put the key into your class.  Or put each object in its own module so you can define a constant nearby but not in the class
	TBD: Use more modules; I would definitely move object instantiation out of the module where the classes are defined.
	TBD: You may also benefit from a single function that takes the object type (Door, etc) as well and instantiates the correct class.	
	TBD: Once you've done that, you might want to have an entire object description in some string format on disk.   I personally kind of like using standard python objects (tuples of strings, mainly) instead of JSON, but YMMV.
	TBD: Try tupples for descript_dict
		Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
	TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )

Expert Questions:
DONE: Std solution for declaring obj variables with reciprocal properties (e.g. writing)
	IDEA: Objects only aware of what is "inside" of them. Examples:
		1) A room knows about the door on its north wall but not the room beyond the door.
		2) An item knows what is written on it but the "writing" knows nothing about the object it is written on
		3) A container knows its contents but items know nothing about the container they are in
TBD: Can (should) I make the program work without external triggers... can the obj just interact on their own?
	Perhaps the key is to make creatures behave as state machines... 
	each has conditions under which they will guard, attack, gift, etc..
	Also room 'events' with conditionals?
	IDEA: avoid external triggers - create classes / state-machines
		Examples: conditional_cutscenes (moat, ending), antagonistic_guard (goblin), hungry_guard (hedgehog1), trader (hedgehog2)[introduce "give" verb, dispenser (throne), lever, button
TBD: How should modules be inter-related (presumably minimally)

### Cutscene ###
IDEA: Conditional Cutscene Class
IDEA: Conditional_events (a class similar to dcv2 triggers??) => implement for moat ????
	- default, default description, default method
	- special event first time, seft_description, seft_method, count
	- special event additional times, seat_description, seat_method, count

More ideas on Conditional Events:
- field in each object for associated conditional event
- Idea is that Interpreter returns standard_command and noun_obj to wrapper
- wrapper checks for noun_obj.event_lst > 0 and sends to event checker routine which returns event_output if appropriate
- (could be more than one event so likely a for loop here)
- if no relevant event then output gets standard_output (generated from interpreter command)
-  events: conditional-command-list, conditions (list of lists; outer = AND; inner = OR), event-text, events (list); check for end of game in wrapper

More ideas on Creatures:
- Treat creatures like roving conditional events
- Wrapper checks for presence of creature in room and checks for conditionals against creature too

Additional Creature and Conditional Event thoughts:
- In theory could have order of operations considerations:
- (e.g. what if a monster causes darkness but you have a sword that glows around monsters?)
- I don't think these will be a common problem that I need to code for - but worth thinking about
- presently my creatures are not mobile but maybe someday?
- What about timers? Maybe timers are associated with events and creatures and switches? Presumably they need to be triggered somehow?

Key Creature Verbs (methods):
- show, give, attack

Some Day Maybe
TBD: Is the Item class worth having??? Particularly, do I need the "takeable" attribute
TBD: room.room_stuf => room.room_obj_lst ??
TBD: Need to dis-entangle modules better
TBD: get rid of Item takeable attribute
TBD: Sort out writing and make it more accessable by examine


### New Puzzle Ideas ###
- Can sharpen and clean sword in mouse hole - maybe only way to get past goblin
- need a non-shrunken ruby to pay for sword sharpening (turns up nose at cheese - says he never touches it because it gives him indigestion)
- mini Zork maze to get to blacksmith mouse
- maybe random mouse keeps appearing and if you give it cheese it runs off and can be followed to the blacksmith
- maybe mouse in maze is from Who Moved my Cheese
- references to grafitti in maze?? (e.g. "what would you do if you weren't afraid?")
- Potion cabinet => maze => sharpen payment; cabinet: Royal Potions Maker: Danni Igotyour , potion: 867-5 => combo
	- Give clues - mention that you hear a boppy tune in your head on description; give some lyrics after 5th attempt
- Sign on mousehole mentions royal blacksmith and royal baker
- Can only find royal baker by NOT taking the signed "exit" route from the blacksmith (easy east)
- Machine in bakery makes cheese (for mouse) or biscuits (for hedgehog) by adding ingredients and pushing correct button
	- Need to have "hatch" closed in order to run machine
	- Takes 3 turns to create food
	- if start biscuits turn after starting cheese then 5 turns later produces cheesecake! (only once - machine brakes after)
	- Everyone wants cheesecake! Can be used to solve any creature puzzle (even goblin) and takes 5 turns to eat
- potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
	- 3 turns of shrink in Main Hall; 30 turns in mouse hole
	- maybe 2 potions in cabinet
	- Need to keep the magic shrink potion from traveling... maybe have it in a basin with a chain-attached cup?
		- (don't want to code every room for being mouse sized)
- Maybe a magic radio (a machine entity like the baking machine) in the Maine Hall that plays "Danni I've got your numbrer" when tuned correctly? Gives clue for potion chest. Also maybe acts as distraction during time travel puzzel - plays over gentle lilting of harp, violins, and triange - which enables Burt to cut in and dance with princess (evil prince is off gyrating hips wildly)? Perhaps the magic radio used to live in the throne room but got moved to the main hall after the 'incident' (note could indicate this) ;-D
- Radio damaged during move from throne room (speaker out; etc)
	- Radio volume goes to 11 (crossed out?)
	- On time travel need right station & full volume to distract prince (learn songs during future time investigation; maybe "moany moany" or "old time rock and roll"?)
	- Perhaps wearing Hedgehog brooch (and smiling) are key to winning princess' trust durning time travel?

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


*** Demo Object Commands ***

# entrance.examine()
# print(entrance.valid_paths)
# entrance.go('south')
# entrance.go('north')

# entrance.examine()
# dark_castle.examine()
# gate.examine()
# gate.read_writing()
# sword.examine()
# sword.take()
# print(hand)
# sword.take()
# sword.drop()
# gate.open()
# gate.unlock()
# rusty_key.examine()
# rusty_key.take()
# print(hand)
# gate.unlock()
# gate.open()
# gate.open()
# print(eval(room).room_stuff)

# sword = Item('sword','The sword is shiny.', True, 5)
# sword.examine()
# sword.change_desc('The sword is rusty.')
# sword.examine()
# print(sword.takeable)
# print(sword.weight)
# sword.add_writing('dwarven runes', 'Goblin Wallaper')
# sword.examine()
# sword.read_writing()
# gate = Door('front gate', 'The front gate is daunting', False, False)
# gate.examine()
# gate.change_desc('The front gate is HUGE!')
# gate.examine()
# gate.read_writing()
# gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
# gate.read_writing()


### test ###
# rusty_letters.read(stateful_dict)
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
