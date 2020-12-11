from peewee import *
from database.core import db
# from engine.parsers.interface import ParserInterface


class MyModel(Model):
    class Meta:
        database = db


class Platform(MyModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class User(MyModel):
    id = AutoField(primary_key=True)
    user_id = IntegerField(null=True)
    platform = ForeignKeyField(Platform, null=True)


class Site(MyModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class Check(MyModel):
    id = AutoField(primary_key=True)
    user = ForeignKeyField(User)
    site = ForeignKeyField(Site)
    url = TextField()
    price = FloatField()

    @property
    def price_verbose(self):
        return f'{self.price}₽'
