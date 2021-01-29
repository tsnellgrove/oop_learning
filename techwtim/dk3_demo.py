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
# TBD: Description of new room on change rooms
# TBD: Enforce room.examine() based on location
# TBD: Fix read_writing => read
# TBD: Think through writing attribute for ViewOnly
# TBD: Link room inventory and player inventory


# At this point, STOP(!!!), and start researching how others have implemented OOP text adventures

hand = []
backpack = []
room = 'entrance'


class ViewOnly(object):
		def __init__(self, name, desc):
				self.name = name
				self.desc = desc

		def examine(self):
				print(self.desc)
		
		def change_desc(self, new_desc):
				self.desc = new_desc

		def add_writing(self, text_desc, text):
				self.desc = self.desc + " On the " + self.name + " there is " + text_desc + "."
				self.text = text

		def read_writing(self):
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
				
		def examine(self):
				print(self.name)
				print(self.desc)
				print("The room contains: " + ', '.join(self.room_objects))
				
		def go(self, direction):
				if direction not in self.valid_paths:
						print("You can't go that way.")
				elif direction in self.door_paths:
						door_open = eval(self.door_paths[direction]).open_state
						if not door_open:
								print("The " +  self.door_paths[direction] + " is closed.")
				else:		
						next_room = self.valid_paths[direction]
						eval(next_room).examine()
						room = next_room


class Item(ViewOnly):
		def __init__(self, name, desc, takeable):
				super().__init__(name, desc)
				self.takeable = takeable
				
		def take(self):
				if self.name in eval(room).room_objects and self.takeable:
						if len(hand) == 0:
								hand.append(self.name)
								eval(room).room_objects.remove(self.name)
								print('taken')
						else:
								print('Your hand is full.')
				else:
						print("There's no " + self.name + " to take here!")

		def drop(self):
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
				
		def unlock(self):
				if self.unlock_state == False:
						if self.key in hand:
								print("Unlocked")
								self.unlock_state = True
						else:
								print("You aren't holding the key.")
				else:
						print("The " + name + " is already unlocked.")

		def open(self):
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


dark_castle = ViewOnly('Dark Castle', 'The evil Dark Castle looms above you')
entrance = Room('Entrance', 'You stand before the daunting gate of Dark Castle. In front of you is the gate', ['rusty_key', 'gate'], {'north' : 'main_hall'}, {'north' : 'gate'})
main_hall = Room('Main Hall', 'A vast and once sumptuous chamber. The main gate is south. There is a passage going north.', ['sword', 'gate'], {'south' : 'entrance', 'north' : 'antichamber'}, {'south' : 'gate'})
rusty_key = Item('rusty_key', 'The key is rusty', True)
sword = Item('sword','The sword is shiny.', True)
gate = Door('Front Gate', 'The front gate is massive and imposing', False, False, 'rusty_key')
gate.add_writing('rusty letters', "The Rusty Letters read: 'Abandon Hope All Ye Who Even Thank About It'")
sword.change_desc(sword.desc +' On the sword blad you see Dwarven Runes.')
sword.add_writing('Dwarven Runes', "Goblin Wallopper")
chest = Container('chest', 'An old wooden chest', False, True, 'brass_key', False, 'potion')
giftbox = Container('giftbox', 'A pretty gift box', False, True, 'none', True, 'necklace')

entrance.examine()

while True:
    user_input = input('Type your command: ')
    lst = []
    lst.append(user_input)
    user_input_lst = lst[0].split()
    word1 = user_input_lst[0]
    if len(user_input_lst) > 1:
        word2 = user_input_lst[1]
    else:
        word2 = "blank"
    if word1.lower() == 'quit':
        break
    elif word1 == 'go':
        room_obj = eval(room)
        getattr(room_obj, word1)(word2)
    else:
        try:
            word2_obj = eval(word2)
        except:
            print("There's no " + word2 + " here.")
        try:
            getattr(word2_obj, word1)()
        except:
            print("You can't " + word1 + " with the " + word2 + ".")



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

