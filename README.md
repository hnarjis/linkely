# linkely
Keep track of shared articles

## Running with docker-compose

Make sure docker and docker-compose are installed.

Create an `.env` file in the same directory as this file, for example
by copying example.env. The settings in example.env allows you to run
the application locally.

Run `docker-compose build`, then `docker-compose up`.

## Getting started

Prerequisites:

* Docker and docker-compose
* Python 3
* Python virtualenv

```
$ virtualenv -p PATH_TO_PYTHON3_BINARY env
$ source env/bin/activate
$ pip install -r requirements.txt
$ docker-compose up
$ cd linkely
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

Now you should have the application running on [localhost:8000](http://localhost:8000)


## Build front-end requirements

See [Semantic UI - Getting started](https://semantic-ui.com/introduction/getting-started.html) for further instructions.

Install gulp and semantic-ui

```
cd frontend
sudo npm install -g gulp
npm install semantic-ui --save
```

Then build semantic

```
cd semantic
gulp build
```
