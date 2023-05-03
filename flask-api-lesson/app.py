# this app.py file is like server.js in the express unit
# CHECK OUT THIS FLASK DOCUMENTATION: https://flask.palletsprojects.com/en/2.2.x/

from flask import Flask, jsonify  # like: const express = require('express')
# now we are importing jsonify from flask
# jsonify lets us send JSON HTTP response (like: res.json())

from flask_login import LoginManager

from resources.dogs import dogs  # import blueprint from resources.dogs

from resources.user import user

# in python when you import a file, you get everything in "global scope"
# of that file
# so this statement will import all variables and methods/functions from that
# file as properties on the models object (e.g. model.initialize() will be available in this file, etc)... we did not explicitly "export"
# anything in models.py
# google "namespacing in python" and "importing in python"
import models

from flask_cors import CORS

DEBUG = True  # print nice helpful error msgs since we are in development
PORT = 8000

login_manager = LoginManager()

# this is analogous to: const app = express()
app = Flask(__name__)  # instantiating the Flask class to create an app

# CORS -- Cross Origin Resource Sharing
# a web domain (site/port/etc) is an "origin"
# this app is localhost:8000, that's an origin
# our react app is localhost:3000, that's a different origin
# Browsers implement CORS to prevent a random JS app from sending requests
# to origins other than the one the browser originally went to, to get that JS
# configuring CORS lets our server say "here's who I'm expecting to hear from"

app.secret_key = "ASDFASDFASDFASDF"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except:
        return None


# first arg -- we are adding cors to blueprints, which blueprint to use
# second arg -- which origins are allowed
# third arg -- lets us accept requests with cookies attached (so that we use sessions for auth)
CORS(dogs, origins=['http://localhost:3000'], supports_credentials=True)

CORS(user, origin=['http://localhost:3000'], supports_credentials=True)


# use this blueprint (component/piece/section/controller of the app)
# to handle anything related to dogs
# analogous to app.use(`api/v1/dogs`, dogsController)
app.register_blueprint(dogs, url_prefix='/api/v1/dogs')

app.register_blueprint(user, url_prefix='/api/v1/user')

# here is how you write a route in Flask


# @app.route('/')  # @ symbol here means this is a decorator
# def hello():
#     # note: what will get returned from a route (sent back as a response)
#     return 'Hello, world!'

# # in Flask now you can send lists! > 2.2.x
# # If the return value is a dict or list, jsonify() is called to produce a response.
# # GET /test


# @app.route('/test')
# def get_list():
#     return ['hello', 'hi', 'hey']

# # That is why this looks the same as above in the browser.


# @app.route('/test_json')
# def get_json():
#     # here we are using jsonify to create HTTP response
#     # with Content-Type set to json
#     # analogous to res.json() in express
#     return jsonify(['hello', 'hi', 'hey'])


# @app.route('/cat_json')
# def get_cat_json():
#     # you can pass key value pairs into jsonify()
#     return jsonify(name='King Charles III', age=6)


# @app.route('/nested_json')
# def get_nested_json():
#     cat_dict = {
#         'name': 'King Charles III',
#         'age': 6,
#         'cute': True,
#         'sweet': True
#     }
#     return jsonify(name="Deja Y", age=25, cat=cat_dict)


# @app.route('/two_cats')
# def get_two_cats():
#     nikki_cat = {
#         'name': 'Mau',
#         'age': 6,
#         'cute': True,
#         'sweet': True
#     }
#     ser = {
#         'name': 'King Charles III',
#         'age': 6,
#         'cute': True,
#         'sweet': True
#     }
#     return jsonify(name="Deja Y", age=25, cats=[ser, nikki_cat])

# # URL parameters in Flask
# # like (req.params in express: app.get('hello/:name'))
# # name would be the parameter


# @app.route('/say_hello/<username>')
# def say_hello(username):
#     return f"Hello {username}"

# this is like app.listen() in express -- it goes at the bottom
# __name__ being '__main__' here means we just ran this file from the
# command line, as opposed to exporting and importing somewhere else


if __name__ == '__main__':
    # when we start the app, set up our DB/tables as defined in models.py
    models.initialize()  # remembers in express we required db before did app.listen
    app.run(debug=DEBUG, port=PORT)
