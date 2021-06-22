# program: marshmallow_tut in support of dark castle v3.20
# name: Tom Snellgrove
# date: June 22, 2021
# description: learn how to use marshmallow for custom object serialization

from marshmallow import Schema, fields, post_load

class Person:
		def __init__(self, name, age):
				self.name = name
				self.age = age

		def __repr__(self):
				return f'{ self.name } is { self.age} years old.'

# marshmallow schema
class PersonSchema(Schema):
		name = fields.String()
		age = fields.Integer()


# creating schema for complex object with marshmallow
		@post_load
		def create_person(self, data, **kwargs):
				return Person(**data)

# getting data via input dictionary
input_data = {}

input_data['name'] = input('What is your name? ')
input_data['age'] = input('What is your age? ')

# load input data into complex object schema
schema = PersonSchema()
# case2: de-serialization load - can validate data in process
#result = schema.load(input_data)
person2 = schema.load(input_data)

# case1: simple object instantiation
# person = Person(name=input_data['name'], age=input_data['age'])

# print simple instantiation
# print(person)

# de-serialization print
# print(result)

# case3: serialization print1
print(person2)

# case3: serialization
result2 = schema.dump(person2)

# case3: serialization print of dictionary (input data has been validated)
print(result2)


