from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField, ListField


from connect import con

c = con


class Author(Document):
    fullname = StringField()
    born_data = StringField()
    born_location = StringField()
    description = StringField()
    meta = {'allow_inheritance': True}


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'allow_inheritance': True}
