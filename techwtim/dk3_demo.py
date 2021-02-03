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
# Note: I think I'm doing something wrong... inventory management with objects is not as elegant as I was expecting

# DONE: Too many calsses already... think about consolidation
# Decision: Inheritance is complicated, Multi-Inheritance is more complicated, and multi inheritance from inherited classes... is just right out!
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

# DONE: Fix read_writing => read
# TBD: Think through writing attribute for ViewOnly (i.e. should be read dwarven_runes instead of read sword)


# At this point, STOP(!!!), and start researching how others have implemented OOP text adventures


#		hand = []
#		backpack = []
#		room = 'entrance'


stateful_dict = {
		'hand' : [], 
		'backpack' : [],
		'room' : 'entrance'
		}

class ViewOnly(object):
		def __init__(self, name, desc):
				self.name = name
				self.desc = desc

		def examine(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
#				print(room)
				examine_lst = eval(room).room_objects
				examine_lst = examine_lst + hand
#				print(examine_lst) # used for troubleshooting
#				print(str(self.name))
				if str(self.name) in examine_lst:
						print(self.desc)
				else:
						print("You can't see a " + self.name + " here.")
		
		def change_desc(self, new_desc):
				self.desc = new_desc

		def add_writing(self, text_desc, text):
				self.desc = self.desc + " On the " + self.name + " there is " + text_desc + "."
				self.text = text

		def read(self, stateful_dict):
				try:
						print(self.text)
				except:
						print("There's nothing to read!")

class Room(ViewOnly):
		def __init__(self, name, desc, room_objects, valid_paths, door_paths):
				super().__init__(name, desc)
				self.room_objects = room_objects # list of items in room
				self.valid_paths = valid_paths # dictionary of {direction1 : room1, direction2 : room2}
				self.door_paths = door_paths # dictionary of {direction1 : door1}
				
		def examine(self, stateful_dict):
				print(self.name)
				print(self.desc)
				print("The room contains: " + ', '.join(self.room_objects))
				print()
				
		def go(self, direction, stateful_dict):
				room = stateful_dict['room']
				if direction not in self.valid_paths:
						print("You can't go that way.")
				elif direction in self.door_paths:
						door_open = eval(self.door_paths[direction]).open_state
						if not door_open:
								print("The " +  self.door_paths[direction] + " is closed.")
						else:
								next_room = self.valid_paths[direction]
								eval(next_room).examine(stateful_dict)
								stateful_dict['room'] = next_room

class Item(ViewOnly):
		def __init__(self, name, desc, takeable):
				super().__init__(name, desc)
				self.takeable = takeable
				
		def take(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
				if self.name in eval(room).room_objects and self.takeable:
						if len(hand) == 0:
								hand.append(self.name)
								eval(room).room_objects.remove(self.name)
								print('taken')
						else:
								print('Your hand is full.')
				else:
						print("There's no " + self.name + " to take here!")

		def drop(self, stateful_dict):
				room = stateful_dict['room']
				hand = stateful_dict['hand']
				if self.name in hand:
						hand.remove(self.name)
						eval(room).room_objects.append(self.name)
						print("Dropped")
				else:
						print("You're not holding the " + self.name + " in your hand.")	
																
class Door(ViewOnly):
		def __init__(self, name, desc, open_state, unlock_state, key):
				super().__init__(name, desc)
				self.open_state = open_state
				self.unlock_state = unlock_state
				self.key = key
				
		def unlock(self, stateful_dict):
				hand = stateful_dict['hand']
				if self.unlock_state == False:
						if self.key in hand:
								print("Unlocked")
								self.unlock_state = True
						else:
								print("You aren't holding the key.")
				else:
						print("The " + name + " is already unlocked.")

		def open(self, stateful_dict):
				if self.open_state == False:
						if self.unlock_state == True:
								self.open_state = True
								print("Openned.")
						else:
								print("The " + self.name + " is locked.")
				else:
						print("The " + self.name + " is already open.")			


class Container(Door):
		def __init__(self, name, desc, open_state, unlock_state, key, takeable, contains): # in this impplementation, containers cannot be taken
				super().__init__(name, desc, open_state, unlock_state, key)
				self.takeable = takeable
				self.contains = contains


dark_castle = ViewOnly('dark_castle', 'The evil Dark Castle looms above you')
entrance = Room('entrance', 'You stand before the daunting gate of Dark Castle. In front of you is the gate', ['rusty_key', 'gate'], {'north' : 'main_hall'}, {'north' : 'gate'})
main_hall = Room('main_hall', 'A vast and once sumptuous chamber. The main gate is south. There is a passage going north.', ['sword', 'gate'], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : 'gate'})
rusty_key = Item('rusty_key', 'The key is rusty', True)
sword = Item('sword','The sword is shiny.', True)
gate = Door('gate', 'The front gate is massive and imposing', False, False, 'rusty_key')
gate.add_writing('rusty_letters', "The Rusty Letters read: 'Abandon Hope All Ye Who Even Thank About It'")
sword.change_desc(sword.desc +' On the sword blad you see Dwarven Runes.')
sword.add_writing('dwarven_runes', "Goblin Wallopper")
chest = Container('chest', 'An old wooden chest', False, True, 'brass_key', False, 'potion')
giftbox = Container('giftbox', 'A pretty gift box', False, True, 'none', True, 'necklace')

entrance.examine(stateful_dict)
print()

while True:
    room = stateful_dict['room']
#    print(stateful_dict)
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
    elif word1 == 'look':
        room_obj = eval(room)
        room_obj.examine(stateful_dict)
        print()
    else:
        try:
            word2_obj = eval(word2)
            print()
        except:
            print("There's no " + word2 + " here.")
            print()
        try:
            getattr(word2_obj, word1)(stateful_dict)
            print()
        except:
            print("You can't " + word1 + " with the " + word2 + ".")
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

