# Dark Castle - Minimum Viable Example 2
# Will attempt to solve Marshmallow to json object duplication issue w/ pickle
# July 24, 2021

# imports
import pickle
import gc

# classes
class Door(object):
		def __init__(self, name, desc, open_state):
				self.name = name
				self.desc = desc
				self.open_state = open_state # True if door is open

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

class Room(object):
		def __init__(self, name, desc, room_doors):
				self.name = name
				self.desc = desc
				self.room_doors = room_doors # list of door objs in room

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

# object instantiation
front_gate = Door('front_gate', "An imposing iron front gate", False)
entrance = Room('entrance', "You are at the castle entrance.", [front_gate])
obj_lst = [front_gate, entrance]

# check initial Door object count
print("Initial list of door objects:")
for obj in gc.get_objects():
		if isinstance(obj, Door):
				print(obj, obj.open_state, id(obj))
print()


# serialize to pickle file
with open('obj_pickle', 'wb') as f:
		pickle.dump(obj_lst, f)

# delete objects
del obj_lst
del front_gate
del entrance

# check Door object count post delete
print("Door objects have been deleted:")
for obj in gc.get_objects():
		if isinstance(obj, Door):
				print(obj, obj.open_state, id(obj))
print()

# de-serialize from pickle file
with open('obj_pickle', 'rb') as f:
		obj_lst_2 = pickle.load(f)
front_gate = obj_lst_2[0]
entrance = obj_lst_2[1]

# check initial Door object count post de-serialize:
print("de-serialized Door objects:")
for obj in gc.get_objects():
		if isinstance(obj, Door):
				print(obj, obj.open_state, id(obj))

