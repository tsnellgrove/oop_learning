Done List - Dark Castle v3
June 7, 2021



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

##############################
### VERSION 3.01 COPMPLETE ###
##############################



