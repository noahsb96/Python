create a virtual environment

```
$ python3 -m venv venv
```

---> this will create a directory `venv`

activating the virtual environment

```
$ . venv/bin/activate
```

```
$ source venv/bin/activate
```

deactivate the virtual environment

```
deactivate
```

you should .gitignore `venv` folder (analogous to gitignore your node_modules)

---

install flask

```
$ touch reqirements.txt
```

```
$ pip3 install flask
```

```
$ pip3 freeze > requirements.txt
```

----> this creates a file `requirements.txt` for us. This is where our dependencies are listed, similar to `package.json`

To install packages from the requirements file and tell pip to install all of the packages in this file -r flag
NOTE: Make sure your virtual environment is activated

```
$ python3 -m pip3 install -r requirements.txt
```

OR

```
$ python3 -m pip install -r requirements.txt
```

---

after configuring your server, run it with `$ python3 app.py`

you will see "NOT FOUND..." this is good

this is analogous to `Cannot GET/` in express

take a look at the terminal output -- notice the sweet development server that is running for you with automatic restarts and logs of when someone maskes a request to your server

access server at http://localhost:8000 (localhost is the same as 127.0.0.1)

---

When building your server, you must have your models sorted out first
we just installed modules that will serve a similar purpose to what mongoose did express

psycopg2
psycopg2-binary

- lets our application connect to a DATABASE

peewee - ORM (Object Relational Mapping) -- like an ODM -- allows us to create models -- allows to query or DB in the Flask app

!! REMEMBER TO pip3 freeze > requirements.txt` manually!! -- pip (pip3) will not do this for you

if you need to clone a Flask app and get it setup and install everything in requirements.txt
