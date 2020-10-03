from peewee import *
from database.core import db
from engine.parsers.interface import ParserInterface


class MyModel(Model):
    class Meta:
        database = db


class User(MyModel):
    id = AutoField(primary_key=True)


class Site(MyModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)

    @property
    def parser(self) -> ParserInterface:
        for p in ParserInterface.__subclasses__():
            if p.site_name == self.name:
                return p()


class Check(MyModel):
    id = AutoField(primary_key=True)
    user = ForeignKeyField(User)
    site = ForeignKeyField(Site)
    url = TextField()
    price = FloatField()

    @property
    def price_verbose(self):
        return f'{self.price}₽'


class Text(MyModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)
    text = TextField()

    def __str__(self):
        return f'<{self.name}>: {self.text}'
