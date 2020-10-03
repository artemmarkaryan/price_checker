from peewee import *
from db_interface.core import db


class MyModel(Model):
    class Meta:
        database = db


class User(MyModel):
    id = AutoField(primary_key=True)


class Site(MyModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class Check(MyModel):
    id = AutoField(primary_key=True)
    user = ForeignKeyField(User)
    site = ForeignKeyField(Site)
    url = TextField()
    value = FloatField()


class Texts(MyModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)
    text = TextField()
