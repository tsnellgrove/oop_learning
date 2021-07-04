# program: marshmallow_tut in support of dark castle v3.20
# name: Tom Snellgrove
# date: July 2, 2021
# description: learn how to use marshmallow for custom object serialization and de-serialization


# imports
from marshmallow import Schema, fields, post_load
import json


# classes
class Pet:
		def __init__(self, pet_name, is_a_cat):
				self.pet_name = pet_name
				self.is_a_cat = is_a_cat

		def __repr__(self):
				return f'it is { self.is_a_cat } that { self.pet_name } is a cat'

class Person:
		def __init__(self, name, age, pet):
				self.name = name
				self.age = age
				self.pet = pet

		def __repr__(self):
				return f'{ self.name } is { self.age} years old and has a pet named { self.pet.pet_name }. {self.pet}'


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


# Initial serialized data
pet_data_dict = {}
person_data = {}

## pet_data['pet_name'] = input('What is your pet name? ')
## pet_data['is_a_cat'] = input('Is it True that your pet is a cat? ')

pet_data_dict['pet_name'] = "Lunabelle"
pet_data_dict['is_a_cat'] = False

person_data = {'name': 'Tom', 'age': 50, 'pet': {'pet_name': 'Kit', 'is_a_cat': True}}


# loads & dumps

# convert dict to json
pet_data_json = json.dumps( pet_data_dict )

# pet load / de-serialize, uses post_load decorator to convert into complex object
schema_pet = PetSchema()
pet1 = schema_pet.loads(pet_data_json)

# pet dump / serialize from complex object to simple dictionary
result_pet_json = schema_pet.dumps(pet1)

# convert json to dict
result_pet_dict = json.loads(result_pet_json)

# person load de-serializes nested data and, uses post_load decorator to convert into complex object
schema_person = PersonSchema()
person1 = schema_person.load(person_data)

# dump serializes complex object into a nested dictionary
result_person = schema_person.dump(person1)


# for each data set print initial serialized data, then de-serialized object, then serialized dict

print(pet_data_dict)
print(pet_data_json)
print(pet1)
print(pet1.pet_name)
print(pet1.is_a_cat)
print(result_pet_json)
print(result_pet_dict)

print()

print(person_data)
print(person1)
print(person1.name)
print(person1.age)
print(person1.pet.pet_name)
print(person1.pet.is_a_cat)
print(result_person)

print()

pet2 = person1.pet
print(pet2)
person1.pet = pet1
print(person1.pet)


