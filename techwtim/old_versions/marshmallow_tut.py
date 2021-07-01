# program: marshmallow_tut in support of dark castle v3.20
# name: Tom Snellgrove
# date: June 22, 2021
# description: learn how to use marshmallow for custom object serialization

from marshmallow import Schema, fields, post_load

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

# marshmallow schema
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
###		include_fk = True
		pet = fields.Nested(PetSchema)

# post load transform with marshmallow creates instance of Class
		@post_load
		def create_person(self, data, **kwargs):
				return Person(**data)

# getting data via input dictionary
pet_data = {}
input_data = {}
person_data = {}

## pet_data['pet_name'] = input('What is your pet name? ')
## pet_data['is_a_cat'] = input('Is it True that your pet is a cat? ')

## input_data['name'] = input('What is your name? ')
## input_data['age'] = input('What is your age? ')

pet_data['pet_name'] = "Kit"
pet_data['is_a_cat'] = True

input_data['name'] = "Tom"
input_data['age'] = 50

print(pet_data)
schema_pet = PetSchema()
pet1 = schema_pet.load(pet_data)
print(pet1)

person_data = [input_data, {'pet' : pet_data}]
print(person_data)
person_data2 = {'name': 'Tom', 'age': 50, 'pet': {'pet_name': 'Kit', 'is_a_cat': True}}
print(person_data2)

schema_person = PersonSchema()
### schema_person = PersonSchema(many=True, unknown=INCLUDE)
### person3 = schema_person.load(person_data)
person3 = schema_person.load(person_data2)

## UserSchema().dump(users, many=True) # from marshmallow site
## book = BookSchema(unknown=INCLUDE).load(data ) # stackoverflow example


# load input data into complex object schema
## schema = PersonSchema()
# case2: de-serialization load - can validate data in process
#result = schema.load(input_data)
## person2 = schema.load(input_data)

# case1: simple object instantiation
# person = Person(name=input_data['name'], age=input_data['age'])

# print simple instantiation
# print(person)

# de-serialization print
# print(result)

# case3: serialization print1
## print(person2)

print(person3)

# case3: serialization
## result2 = schema.dump(person2)

result3 = schema_person.dump(person3)

# case3: serialization print of dictionary (input data has been validated)
##print(result2)

print(result3)

