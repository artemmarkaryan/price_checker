from peewee import *
from db_interface.core import db


class User(Model):
    class Meta:
        database = db
    id = AutoField(primary_key=True)


class Site(Model):
    class Meta:
        database = db
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class Check(Model):
    class Meta:
        database = db
    id = AutoField(primary_key=True)
    user = ForeignKeyField(User)
    site = ForeignKeyField(Site)
    url = TextField()
    value = FloatField()


# if __name__ == '__main__':
#     db.connect()
#     db.create_tables(User, Site, )