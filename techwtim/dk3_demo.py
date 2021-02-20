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

# DONE: Reconsider restricting 'features' to class Room using hasattr
# DONE: dis-allow locking when Door / Container object is open?
# DONE: Represent container elements as sub elements of container in room
# NOTE: Now I have a few more container problems:
# DONE: First I need to make items in containers takable... 
#		but not list them in the room_objects inventory... 
#		perhaps I have an open_container_obj list? 
#		Or perhaps better yet, 
#		dynamically add contents of open containers to takeable scope? [YES!!]
# IDEA: Next, when I take the item from the container,
#		I need to remove it from <container>.contains
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

# IN-PROC: Redirect prints to buffer
# DONE: Create stateful_dict['out_buff']
# DONE: Create buffer() helper function
#	DONE: "Bufferize" classes ViewOnly and Writing
# DONE: "Bufferize" classes Room and Item
# DONE: "Bufferize" class Door method examine
# TBD: "Bufferize" class Door remaining methods
# TBD: "Bufferize" main

# TBD: functionalize main
# TBD: Does read need open containers added to examine scope? 
#		Really need to functionalize!!

# Some Day Maybe
# TBD: Implment container.put(item) ???
# TBD: Is the Item class worth having???

# At this point, STOP(!!!), and start researching how others have implemented OOP text adventures

# ****** Interpreter Thoughts #

# 0) Functionalize Interpreter and use out_buff
# 1) Every noun as an obj_name, full_name, root_name
# 2) All one_word commands => 1_word function
# 3) use lists to identify words as nouns, verbs, adjectives, articles, and prepositions
# 4) if sentence does not start with a verb => please start with a verb
# 5) if multiple nouns, verbs, articles, or preps in a row => I don't undderstand that setence error
# 6) Convert adjectives + noun => obj_name
# 7) If no prep => verb_noun function
# 8) If prep: Identify direct object and => prep_sentence function
# NOTE: All room-based validation happens in the method - the Interpreter just converts English to method calls



# stateful dictionary of persistent values
stateful_dict = {
		'hand' : [], 
		'backpack' : [],
		'room' : 'entrance',
		'out_buff' : ""
		}


# helper functions
def set_difference(a,b):
    return list(set(a)-set(b))


def buffer(stateful_dict, output):
		out_buff = stateful_dict['out_buff']
		out_buff = out_buff + output + "\n"
		stateful_dict['out_buff'] = out_buff


# classes
class ViewOnly(object):
		def __init__(self, name, desc, writing):
				self.name = name
				self.desc = desc
				self.writing = writing

		def examine(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
				room_objects = eval(room).room_objects
				out_buff = stateful_dict['out_buff']
				examine_lst = room_objects + hand
				examine_lst.append(room)
				if hasattr(eval(room), 'features'):
						features = eval(room).features
						examine_lst = examine_lst + features
#				print(examine_lst) # used for troubleshooting

				for obj in room_objects:
						if type(eval(obj)) == type(eval('chest')) \
										and len(eval(obj).contains) > 0 \
										and eval(obj).open_state == True:
								container_obj = eval(obj).contains
								examine_lst = examine_lst + container_obj

				if str(self.name) in examine_lst:
						output = self.desc
						buffer(stateful_dict, output)
						if self.writing != 'null':
								output = "On the " + self.name + " you see: " + self.writing
								buffer(stateful_dict, output)
				else:
						output = "You can't see a " + self.name + " here."
						buffer(stateful_dict, output)
		
		def change_desc(self, new_desc):
				self.desc = new_desc

class Writing(ViewOnly):
		def __init__(self, name, desc, writing, written_on):
				super().__init__(name, desc, writing)
				self.written_on = written_on

		def read(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
				out_buff = stateful_dict['out_buff']
				examine_lst = eval(room).room_objects
				features = eval(room).features
				examine_lst = examine_lst + hand + features
				if self.written_on in examine_lst:
						output = self.desc
						buffer(stateful_dict, output)

class Room(ViewOnly):
		def __init__(self, name, desc, writing, features, room_objects, valid_paths, door_paths):
				super().__init__(name, desc, writing)
				self.features = features # list of non-items in room (can be examined but not taken)
				self.room_objects = room_objects # list of items in room
				self.valid_paths = valid_paths # dictionary of {direction1 : room1, direction2 : room2}
				self.door_paths = door_paths # dictionary of {direction1 : door1}
			
		def examine(self, stateful_dict):
				super(Room, self).examine(stateful_dict)
				if stateful_dict['room'] == self.name:
						output = "The room contains: " + ', '.join(self.room_objects)
						buffer(stateful_dict, output)
						
				for obj in self.room_objects:
						if type(eval(obj)) == type(eval('chest')) \
										and len(eval(obj).contains) > 0 \
										and eval(obj).open_state == True:
								output = "The " + obj + " contains: " + ', '.join(eval(obj).contains)
								buffer(stateful_dict, output)
				
		def go(self, direction, stateful_dict):
				room = stateful_dict['room']
				if direction not in self.valid_paths:
						output = "You can't go that way."
						buffer(stateful_dict, output)
				elif direction in self.door_paths:
						door_open = eval(self.door_paths[direction]).open_state
						if not door_open:
								output = "The " +  self.door_paths[direction] + " is closed."
								buffer(stateful_dict, output)
						else:
								next_room = self.valid_paths[direction]
								stateful_dict['room'] = next_room
								eval(next_room).examine(stateful_dict)


class Item(ViewOnly):
		def __init__(self, name, desc, writing, takeable):
				super().__init__(name, desc, writing)
				self.takeable = takeable
				
		def take(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
				room_objects = eval(room).room_objects
				can_take = room_objects
				for obj in room_objects:
						if type(eval(obj)) == type(eval('chest')) \
										and len(eval(obj).contains) > 0 \
										and eval(obj).open_state == True:
								can_take = can_take + eval(obj).contains
				
				if self.name in can_take and self.takeable:
						if len(hand) == 0:
								hand.append(self.name)

								taken_from_container = False
								for obj in room_objects:
										if type(eval(obj)) == type(eval('chest')) \
														and len(eval(obj).contains) > 0 \
														and eval(obj).open_state == True:
												eval(obj).contains.remove(self.name)
												taken_from_container = True

								if taken_from_container == False:
										eval(room).room_objects.remove(self.name)
								output = "Taken"
								buffer(stateful_dict, output)
						else:
								output = "Your hand is full."
								buffer(stateful_dict, output)
				else:
						output = "There's no " + self.name + " to take here!"
						buffer(stateful_dict, output)

		def drop(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
				if self.name in hand:
						hand.remove(self.name)
						eval(room).room_objects.append(self.name)
						output = "Dropped"
						buffer(stateful_dict, output)
				else:
						output = "You're not holding the " + self.name + " in your hand."
						buffer(stateful_dict, output)

class Door(ViewOnly):
		def __init__(self, name, desc, writing, open_state, unlock_state, key):
				super().__init__(name, desc, writing)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key

		def examine(self, stateful_dict):
				super(Door, self).examine(stateful_dict)
				room = stateful_dict['room']
				room_objects = eval(room).room_objects
				if self.name in room_objects:
						if self.open_state:
								output = "The " + self.name + " is open."
								buffer(stateful_dict, output)
								if hasattr(self, 'contains'):
										if len(self.contains) == 0:
												output = "The " + self.name + " is empty."
												buffer(stateful_dict, output)
										else:
												output = "The " + self.name + "contains: "  + ', '.join(self.contains)
												buffer(stateful_dict, output)
						else:
								output = "The " + self.name + " is closed."
								buffer(stateful_dict, output)

		def unlock(self, stateful_dict):
				hand = stateful_dict['hand']
				if self.unlock_state == False:
						if self.key in hand:
								print("Unlocked")
								self.unlock_state = True
						else:
								print("You aren't holding the key.")
				else:
						print("The " + self.name + " is already unlocked.")

		def open(self, stateful_dict):
				if self.open_state == False:
						if self.unlock_state == True:
								self.open_state = True
								print("Openned.")
								if hasattr(self, 'contains'):
										if len(self.contains) == 0:
												print("The " + self.name + " is empty.")
										else:
												print("The " + self.name + " contains: " + ', '.join(self.contains))
#										room = stateful_dict['room']
#										room_objects = eval(room).room_objects
#										room_objects = room_objects + self.contains
#										eval(room).room_objects = room_objects
						else:
								print("The " + self.name + " is locked.")
				else:
						print("The " + self.name + " is already open.")			

		def close(self, stateful_dict):
				if self.open_state:
						self.open_state = False
						print("Closed.")
						if hasattr(self, 'contains'):
								if len(self.contains) > 0:
										room = stateful_dict['room']
										room_objects = eval(room).room_objects
										container_contents = self.contains
										container_closed = set_difference(room_objects, container_contents)
										eval(room).room_objects = container_closed
				else:
						print("The " + self.name + " is already closed.")			

		def lock(self, stateful_dict):
#				print(self.open_state)
				if self.open_state == False:
						hand = stateful_dict['hand']
						if self.key in hand:
								if self.unlock_state:
										print("Locked")
										self.unlock_state = False
								else:
										print("The " + self.name + " is already locked.")
						else:
								print("You aren't holding the key.")
				else:
						print("You can't lock something that's open.")

class Container(Door):
		def __init__(self, name, desc, writing, open_state, unlock_state, key, takeable, contains):
				super().__init__(name, desc, writing, open_state, unlock_state, key)
				self.takeable = takeable # can the container be taken?
				self.contains = contains # list of items in the container


# object instantiation
dark_castle = ViewOnly('dark_castle', 'The evil Dark Castle looms above you', 'null')

entrance = Room('entrance',
		'Entrance\nYou stand before the daunting gate of Dark Castle. In front of you is the gate',
		'null', ['dark_castle'], ['rusty_key', 'gate'], {'north' : 'main_hall'}, {'north' : 'gate'})
main_hall = Room('main_hall',
		'Main Hall\nA vast and once sumptuous chamber. The main gate is south. There is a passage going north.',
		'null', [], ['sword', 'gate', 'brass_key', 'chest'], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : 'gate'})

gate = Door('gate', 'The front gate is massive and imposing',
		'rusty_letters', False, False, 'rusty_key')
screen_door = Door('screen_door', "You should never be able to examine the screen_door",
		'null', False, False, 'chrome_key')

rusty_key = Item('rusty_key', 'The key is rusty', 'null', True)
sword = Item('sword','The sword is shiny.', 'dwarven_runes', True)
brass_key = Item('brass_key', 'The key is brass', 'null', True)
potion = Item('potion', 'The cork-stopperd glass vial contains a bubbly green potion', 'null', True)

rusty_letters = Writing('rusty_letters', 'Abandon Hope All Ye Who Even Thank About It', 'null', 'gate')
dwarven_runes = Writing('dwarven_runes', "Goblin Wallopper", 'null', 'sword')

chest = Container('chest', 'An old wooden chest', 'null',
		False, False, 'brass_key', False, ['potion'])
giftbox = Container('giftbox', 'A pretty gift box', 'null',
		False, True, 'none', True, ['necklace'])


# start text
entrance.examine(stateful_dict)
print("B: " + stateful_dict['out_buff'])

# gate.examine(stateful_dict) # troubleshooting text


# main loop
while True:
    room = stateful_dict['room']
#    print(stateful_dict) # troubleshooting text
    stateful_dict['out_buff'] = ""
    user_input = input('Type your command: ')
    lst = []
    lst.append(user_input)
    user_input_lst = lst[0].split()
    word1 = user_input_lst[0].lower()
    if len(user_input_lst) > 1:
        word2 = user_input_lst[1].lower()
    else:
        word2 = "blank"
    if word1 == 'quit':
        break
    elif word1 == 'go':
        room_obj = eval(room)
        getattr(room_obj, word1)(word2, stateful_dict)
        print()
        print("B: " + stateful_dict['out_buff'])
    elif word1 == 'look':
        room_obj = eval(room)
        room_obj.examine(stateful_dict)
        print()
        print("B: " + stateful_dict['out_buff'])
    else:
        try:
            word2_obj = eval(word2)
            print()
            try:
                getattr(word2_obj, word1)(stateful_dict)
                print("B: " + stateful_dict['out_buff'])
                print()
            except:
                print("You can't " + word1 + " with the " + word2 + ".")
                print()
        except:
            print("There's no " + word2 + " here.")
            print()



# entrance.examine()
# print(entrance.valid_paths)
#entrance.go('south')
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
# print(eval(room).room_objects)


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

