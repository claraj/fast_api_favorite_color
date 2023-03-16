from peewee import * 
import db_config
import schema

# db = MySQLDatabase(
#     db_config.db_name,
#     host = db_config.host,
#     port = db_config.port,
#     user = db_config.user,
#     password = db_config.password )


db = SqliteDatabase('tmp.db')

class Color(Model):
    name = CharField()

    class Meta:
        database = db

db.connect() 
db.create_tables([Color])


def add_color(color: schema.ColorCreate):
    color = Color(name=color.name)  # making a peewee model
    color.save()
    return color


def get_all_colors():
    colors = list(Color.select())
    return colors
