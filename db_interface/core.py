import peewee
import config


db = peewee.PostgresqlDatabase(
    'd3vsbi489vb566',
    user='upjndjitgbddxp',
    password=config.DB_PASSWORD,
    host='ec2-54-228-209-117.eu-west-1.compute.amazonaws.com',
    port=5432
)
