# example from statckoverflow
# https://stackoverflow.com/questions/55081806/nested-class-in-json-de-serialization-using-marshmallow

from marshmallow import Schema, fields, post_load, INCLUDE
import datetime as dt
import json

class Person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class PersonSchema(Schema):
    fname = fields.Str()
    lname = fields.Str()

    @post_load
    def make_person(self, data):
        return Person(**data)


class App(object):
    def __init__(self, appid, channel, person):
        self.appid = appid
        self.channel = channel
        self.person = person
        self.created_at = dt.datetime.now()

class AppSchema(Schema):
    appid = fields.Str()
    channel = fields.Str()
    person = fields.Nested(PersonSchema)
    created_at = fields.DateTime()

    @post_load
    def make_app(self, data):
        return App(**data)

json_data = """{
    "appid": "2309wfjwef",
    "channel": "retail",
    "person": {
        "fname": "John",
        "lname": "Doe"
        }
}"""
print(json_data)

app_data = json.loads(json_data)
print(app_data)

schema = AppSchema(many=True)
### app = schema.load(app_data)
app = schema.load(app_data, unknown=INCLUDE)


print(app.data.person.fname)
