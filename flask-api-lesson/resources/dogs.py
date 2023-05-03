# this is analogous to dogController.js
from flask-api-lesson.resources.user import login
import models

# https://flask.palletsprojects.com/en/2.2.x/tutorial/views/
# https://flask.palletsprojects.com/en/2.2.x/blueprints/
# we will use Blueprints to create basically a "controller"
from flask import Blueprint, request, jsonify
# request -- data from the client's request is sent to the global object
# we can use this request object to get the json or form data or whatever else is in the request
# the request global variable will be reassigned everytime a request comes in that has a body

# there are some useful tools that come with peewee
from playhouse.shortcuts import model_to_dict

from flask_login import login_required

# create our blueprint
# first argument is the blueprint's name
# second argument is its import_name
# similar to create a router in express
dogs = Blueprint('dogs', 'dogs')


@dogs.route('/', methods=['GET'])
@login_required
def dogs_index():
    result = models.Dog.select()
    print('result of dog select query')
    print(result)

    # 🤔 hmmm we need a list of dictionaries

    # use a loop to populate the list -- note you can loop over this

    # convert each model to a dict using model_to_dict

    # this seem helpful
    # for dog in result:
    #     print(dog.__data__)

    # or we can do it manually
    # dog_dicts = []
    # for dog in result:
    #     dog_dict = model_to_dict(dog)
    #     dog_dicts.append(dog_dict)

    # or use a list comprehension
    dog_dicts = [model_to_dict(dog) for dog in result]

    return jsonify({
        'data': dog_dicts,
        'message': f"Successfully found {len(dog_dicts)} dogs",
        'status': 200
    }), 200

# dog create route
# POST /api/v1/dogs/
#


@dogs.route('/', methods=['POST'])
def create_dogs():
    payload = request.get_json()  # this is like req.body in express
    print(payload)
    new_dog = models.Dog.create(
        name=payload['name'], owner=payload['owner'], breed=payload['breed'])
    print(new_dog)  # just print the ID -- check sqlite3 to see the data
    # run sqlite3 dogs.sqlite and run SQL queries in the CLI

    # print(new_dog.__dict__)
    # this might be useful, sometimes it gives you better info
    # dict is a class attribute automatically added to the python class

    # print(dir(new_dog)) # look at all of the models' stuff and pretty methods!!

    # you can't jsonify new_dog directly because it's not a dictionary or
    # other jsonifiable things
    # so when we get this error TypeError: Object of type Dog is not JSON serializable
    # when we try to jsonify
    # to convert the .... wait for it ... model to dict
    dog_dict = model_to_dict(new_dog)

    return jsonify(
        data=dog_dict,
        message='Successfully created dog!',
        status=201
    ), 201

# COMBINED ROUTES
# GET, PUT, DELETE api/v1/dogs/<dog_id>


@dogs.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_one_dog(id):
    if request.method == 'GET':
        try:
            dog = models.Dog.get_by_id(id)
            print(dog)
            return jsonify(
                data=model_to_dict(dog),
                message='Success!!! 🎉',
                status=200
            ), 200
        except:
            return jsonify(
                message=f'{request.method} FAILED: The dog with the id of {id} does not exist',
                status=404
            ), 404

    payload = request.get_json() if request.method == 'PUT' else None
    query = models.Dog.update(**payload).where(models.Dog.id ==
                                               id) if payload else models.Dog.delete().where(models.Dog.id == id)
    query_return = query.execute()
    if query_return == 0:
        return jsonify(
            message=f'{request.method} FAILED: The dog with the id of {id} does not exist',
            status=404
        ), 404
    data = model_to_dict(models.Dog.get_by_id(id)) if payload else [
        model_to_dict(dog) for dog in models.Dog.select()]
    return jsonify(
        data=data,
        message='Dog Updated Successfully' if payload else 'Dog Deleted Successfully',
        status=200
    ), 200


# SHOW ROUTE
# GET api/v1/dogs/<dog_id>
# in express it looked something like this
# router.get('/:id')
@dogs.route('/<id>', methods=['GET'])
def get_one_dog(id):
    dog = models.Dog.get_by_id(id)
    print(dog)
    return jsonify(
        data=model_to_dict(dog),
        message='Success!!! 🎉',
        status=200
    ), 200


@dogs.route('/<id>', methods=["PUT"])
def update_dog(id):
    payload = request.get_json()
    query = models.Dog.update(**payload).where(models.Dog.id == id)
    query.execute()
    return jsonify(
        data=model_to_dict(models.Dog.get_by_id(id)),
        status=200,
        message='resource updated successfully'
    ), 200


@dogs.route('/<id>', methods=['DELETE'])
def delete_dog(id):
    query = models.Dog.delete().where(models.Dog.id == id)
    query.execute()
    return jsonify(
        data=model_to_dict(models.Dog.get_by_id(id)),
        message='resource successfully deleted',
        status=200
    ), 200
