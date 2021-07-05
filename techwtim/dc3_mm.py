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


# mm schemas
class WritingSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()

class ViewOnlySchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema)

class ItemSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema)
		takable = fields.Boolean()

class DoorSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema)
		open_state = fields.Boolean()
		unlock_state = fields.Boolean()
		key = fields.Nested(ItemSchema)

class RoomSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema)
		takable = fields.Boolean()
		features = fields.List(fields.Nested(ViewOnlySchema))	
		room_stuff = fields.List(fields.Nested(ItemSchema)) # temp wrong
		door_paths = fields.Dict(keys=fields.String(), values=fields.Nested(DoorSchema))

class StatefulSchema(Schema):
		hand = fields.Nested(ItemSchema)
		backpack = fields.Nested(ItemSchema)
		universal = fields.List(fields.Nested(ItemSchema))
		room = fields.Nested(RoomSchema)
		out_buff = fields.String()
		score = fields.Integer()
		end_of_game = fields.Boolean()
		current_score = fields.Integer()
		move_counter = fields.Integer()
		game_ending = fields.String()
		paths = fields.String() # temp wrong

def mm_serialize(stateful_dict):
		print(stateful_dict)
		print()
##		stateful_json = json.dumps(stateful_dict)
		schema_stateful = StatefulSchema()
		stateful_json = schema_stateful.dumps(stateful_dict)
		print(stateful_json)


