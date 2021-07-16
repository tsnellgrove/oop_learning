# Dark Castle - Minimum Viable Exampe
# Demonstrates Marshmallow duplication issue
# July 16, 2021

# imports
from marshmallow import Schema, fields, post_load
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


# objects
front_gate = Door('front_gate', "An imposing iron front gate", False)
entrance = Room('entrance', "You are at the castle entrance.", [front_gate])


# marshmallow schemas
class DoorSchema(Schema):
		name = fields.String()
		desc = fields.String()
		open_state = fields.Boolean()

		@post_load
		def create_door(self, data, **kwargs):
				return Door(**data)

class RoomSchema(Schema):
		name = fields.String()
		desc = fields.String()
		room_doors = fields.List(fields.Nested(DoorSchema), allow_none=True)

		@post_load
		def create_room(self, data, **kwargs):
				return Room(**data)


# check initial Door object count
print("Initial list of door objects:")
for obj in gc.get_objects():
		if isinstance(obj, Door):
				print(obj, obj.open_state, id(obj))


# serialize to text file


