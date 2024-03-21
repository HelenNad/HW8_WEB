from mongoengine import Document
from mongoengine.fields import StringField,BooleanField


from connect import con

c = con


class Contact(Document):
    completed = BooleanField(default=False)
    name = StringField()
    phone = StringField()
    email = StringField()
    address = StringField()
    meta = {'allow_inheritance': True}



