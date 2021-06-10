To Do List - Dark Castle v3
June 8, 2021



##########################
### VERSION 3.20 START ###
##########################

TBD: 3.20 to be all about DB integration and main / interpreter separation

IN-PROC: Watch YouTube vid on SQLAlchemy: https://youtu.be/51RpDZKShiw
	TBD: Create practice file


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
