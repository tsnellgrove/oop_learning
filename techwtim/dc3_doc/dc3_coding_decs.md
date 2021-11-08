Coding Decisions File - Dark Castle v3
Nov 2, 2021


TRIGGER PRINCIPLES:
- Would like Room Events to be somehow linked to the Room obj so that you can inspect obj and know there will be a CE
- field in each object for associated conditional event
- Conditional Events could be warnings - not hard stops (e.g. 'eat biscuits')
- In theory could have order of operations considerations:
- (e.g. what if a monster causes darkness but you have a sword that glows around monsters?)
- I don't think these will be a common problem that I need to code for - but worth thinking about
- presently my creatures are not mobile but maybe someday?
- What about timers? Maybe timers are associated with events and creatures and switches? Presumably they need to be triggered somehow?
- For machines, the 'trigger' just sets the value... the machine holds the logic and takes the action
- Can (should) I make the program work without external triggers... can the obj just interact on their own?
	Perhaps the key is to make creatures behave as state machines... 
	each has conditions under which they will guard, attack, gift, etc..
	Also room 'events' with conditionals?
	IDEA: avoid external triggers - create classes / state-machines
		Examples: conditional_cutscenes (moat, ending), antagonistic_guard (goblin), hungry_guard (hedgehog1), trader (hedgehog2)[introduce "give" verb, dispenser (throne), lever, button


VARIABLE DECLARATION:
- Std solution for declaring obj variables with reciprocal properties (e.g. writing)
	IDEA: Objects only aware of what is "inside" of them. Examples:
		1) A room knows about the door on its north wall but not the room beyond the door.
		2) An item knows what is written on it but the "writing" knows nothing about the object it is written on
		3) A container knows its contents but items know nothing about the container they are in


CODING SPECIFICS:

- The value of the Item class:
	- Now that I have eliminated the 'takable' attribute from Item there is no attribute difference between Item and ViewOnly
	- the key functional difference is that Item has the take() and drop() methods
	- this is occasionally inconvenient because it makes it hard for me to give clear errors to reasonable requests (e.g. 'take water')
	- however, most of the time this is handy because it eliminates the need to handle all sorts of crazy requests (e.g. 'take castle')
	- Further, someday, I may want to add attributes to Items (e.g. some measure of carrying capacity)
	- So, in summary, I think it makes snese to keep Item and ViewOnly as separate classes - at least for now (10/23/2021)

- Standardizing obj-not-in-hand error (with error message) as a method of GameState:
	- Tried this and ended up going back to original "custom" approach with a simple boolean method
	- Was very conflicted re balance between less repitition vs. less readible & less customizable; Pondering
	- The code was more readable & customizable before; maybe implement a simple boolean function instead

- Moving the help() function to interpreter()
	- The macro organization of the program is for interpreter() to interpret the players intent and for cmd_exe() to execute it
	- However, at the module level, the idea is that the interpreter() module is uniquely focussed on language semantics
	- The help() function is also (mostly) focussed on language semantics - specificly exposing them to the player
	- Moving help() to interpreter() also enables us to make all the static lists and dictionaries local to interpreter()
	- The balance between module-level structure and macro-program flow seems best served by moving the help() function to interpreter()


MODULE FLOW:
- Idea is that Interpreter returns standard_command and noun_obj to wrapper
- wrapper checks for noun_obj.event_lst > 0 and sends to event checker routine which returns event_output if appropriate
- (could be more than one event so likely a for loop here)
- if no relevant event then output gets standard_output (generated from interpreter command)
- How should modules be inter-related
	 - minimally - there should be a clear flow with each sizable atomic bit of work having its own module

