# all of our models will go in this file
# http://docs.peewee-orm.com/en/latest/

# peewee in our flask app is like mongoose in our express app

from enum import unique
from peewee import *  # import * means import everything
import datetime  # built into python
# in python you often need to import things that would
# already be there in other languages (this JS date())
# this keeps it lightweight
from flask_login import UserMixin

# in particular
# SqliteDatabase -- adapter that lets us connect to sqlite database
# and
# Model -- this Model() class is what we will inherit from when
# defining our model(similar to what we did with mongoose in Unit 2 and in our model files)

# sqlite is a way to have a "database" that is just stored in a file
# great for development bc you can have portable data (e.g. git)
# https://www.sqlite.org/index.html
# later when we deploy we will change this to postgres
DATABASE = SqliteDatabase('dogs.sqlite')
# analogous to MONGO_DB_URL = mongod://localhost/dogs, {...) in Unit 2
# there will be a file in our project called 'dogs.sqlite'


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

# define our Dog Model
# http://docs.peewee-orm.com/en/latest/peewee/models.html


class Dog(Model):
    name = CharField()  # string
    owner = CharField()  # string for now, later this can be a relation
    breed = CharField()
    # this is how you specify default values
    created_at = DateTimeField(default=datetime.datetime.now)

    # special constructor that gives our model/class instructions on
    # how to connect to a DB & where to store its data
    class Meta:
        database = DATABASE  # use the db defined above as DATABASE

# define a method that will get called when the app starts
# (in app.py) to setup our databse connection
# similar to how we did require our db configuration in server.js in Unit 2


def initialize():  # NOTE: we are making this up
    DATABASE.connect()  # analogous to mongoose.connect(....)

    # we need to explixitly create tables based on our schema
    # definitions above
    # use.create_tables()
    # first arg: is a List of tables to create
    # second arg: -- safe=True -- only create tables if they don't already exist
    DATABASE.create_tables([User, Dog], safe=True)
    print("Connected to the DB and created tables if they don't already exist")
    # with SQL, don't leave DB connection open, we don't want to hog space in our connection Pool
    DATABASE.close()
