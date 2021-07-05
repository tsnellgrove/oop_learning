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

class ItemSchema(Schema):
		name = fields.String()
		full_name = fields.String()
		root_name = fields.String()
		writing = fields.Nested(WritingSchema)
		takable = fields.Boolean()

def mm_serialize(stateful_dict):
		print(stateful_dict)
		stateful_json = json.dumps(stateful_dict)
		print(stateful_json)

### mm_tut schema template

# marshmallow schemas
class PetSchema(Schema):
		pet_name = fields.String()
		is_a_cat = fields.Boolean()

# post load transform with marshmallow creates instance of Class
		@post_load
		def create_pet(self, data, **kwargs):
				return Pet(**data)

class PersonSchema(Schema):
		name = fields.String()
		age = fields.Integer()
		pet = fields.Nested(PetSchema)

# post load transform with marshmallow creates instance of Class
		@post_load
		def create_person(self, data, **kwargs):
				return Person(**data)
