import peewee
import config


db = peewee.PostgresqlDatabase(
    database='main',
    user='admin',
    password=config.DB_PASSWORD,
    host='5.63.155.152',
    port=5432
)
