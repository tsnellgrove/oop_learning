# program: dark castle v3.11
# name: Tom Snellgrove
# date: July 3, 2021
# description: serialization for a zork-like text adventure game


# imports
from marshmallow import Schema, fields, post_load
import json
from dc3_static_init import *
from dc3_classes import *
from dc3_init import *
from dc3_helper import *
from dc3_interp_helper import *


# demo
## class UserSchema(Schema):
##    name = fields.String()
##    email = fields.Email()
##    created_at = fields.DateTime()


## class BlogSchema(Schema):
##		title = fields.String()
##		author = fields.Nested(UserSchema)


# mm schemas
class WritingSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		
		@post_load
		def create_writing(self, data, **kwargs):
				return Writing(**data)

class ViewOnlySchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema, allow_none=True)

## class ViewOnlySchema(Schema):
##		name_info = fields.Nested(WritingSchema)
##		writing = fields.String(allow_none=True)

		@post_load
		def create_viewonly(self, data, **kwargs):
				return ViewOnly(**data)

class ItemSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema, allow_none=True)
##		view_only = fields.Nested(ViewOnlySchema)
		takable = fields.Boolean()

		@post_load
		def create_item(self, data, **kwargs):
				return Item(**data)

class DoorSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema, allow_none=True)
		open_state = fields.Boolean()
		unlock_state = fields.Boolean()
		key = fields.Nested(ItemSchema)

		@post_load
		def create_door(self, data, **kwargs):
				return Door(**data)

class ContainerSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema, allow_none=True)
		open_state = fields.Boolean()
		unlock_state = fields.Boolean()
		key = fields.Nested(ItemSchema)
		takable = fields.Boolean()
		contains = fields.List(fields.Nested(ItemSchema), allow_none=True)

		@post_load
		def create_container(self, data, **kwargs):
				return Container(**data)

class RoomSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema, allow_none=True)
##		takable = fields.Boolean()
		features = fields.List(fields.Nested(ViewOnlySchema), allow_none=True)
		room_items = fields.List(fields.Nested(ItemSchema), allow_none=True)
		room_doors = fields.List(fields.Nested(DoorSchema), allow_none=True)
		room_containers = fields.List(fields.Nested(ContainerSchema), allow_none=True)
		door_paths = fields.Dict(keys=fields.String(), values=fields.Nested(DoorSchema))

		@post_load
		def create_room(self, data, **kwargs):
				return Room(**data)

### class PathSchema(Schema):
###		direction = fields.Nested(RoomSchema)

class StatefulSchema(Schema):
		hand = fields.List(fields.Nested(ItemSchema))
		backpack = fields.List(fields.Nested(ItemSchema))
		universal = fields.List(fields.Nested(ViewOnlySchema))
		room = fields.Nested(RoomSchema)
		out_buff = fields.String()
		score = fields.Integer()
		end_of_game = fields.Boolean()
		current_score = fields.Integer()
		move_counter = fields.Integer()
		game_ending = fields.String()
		paths = fields.Dict(keys=fields.String(), values=fields.Dict(keys=fields.String(), values=fields.Nested(RoomSchema)))

def mm_serialize(stateful_dict):
		print(stateful_dict)
		test_dict = stateful_dict
		print()

##		stateful_json = json.dumps(stateful_dict)
		schema_stateful = StatefulSchema()
		stateful_json = schema_stateful.dumps(stateful_dict)
		print(stateful_json)
		print()

		result_dict = schema_stateful.loads(stateful_json)
		print(result_dict)
		print()

		print(stateful_dict == result_dict)
		print(stateful_dict == test_dict)
		print()
		
def print_obj():
		json_dict = {}
		schema_lst = [WritingSchema(), ViewOnlySchema(), ItemSchema(), ContainerSchema(), DoorSchema(), RoomSchema()]
		count = 0
		for lst in obj_lst_lst:
				schema = schema_lst[count]
				count += 1
				for obj in lst:
						key = obj.name
						print(obj)
						json_obj = schema.dumps(obj)
						print(json_obj)
						value = json_obj
						json_dict[key] = value
						result_dict = schema.loads(json_obj)
						print(result_dict)
						print (obj == result_dict)
						print()
		print(json_dict)
	
def mm_stateful_default_load():
		with open('dc3_default_stateful_json.txt') as f:
				data = f.read()
		schema_stateful = StatefulSchema()
		stateful_dict = schema_stateful.loads(data)
		return  stateful_dict

def mm_stateful_save(stateful_dict):
		schema_stateful = StatefulSchema()
		stateful_json = schema_stateful.dumps(stateful_dict)
		with open('dc3_save_stateful_json.txt', 'w') as outfile:
				outfile.write(stateful_json)

def mm_stateful_save_load():
		with open('dc3_save_stateful_json.txt') as f:
				data = f.read()
		schema_stateful = StatefulSchema()
		stateful_dict = schema_stateful.loads(data)
		return  stateful_dict
