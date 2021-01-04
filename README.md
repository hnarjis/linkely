# linkely
Keep track of shared articles

## Getting started

Prerequisites:

* Docker
* docker-compose

Clone the repo, then run:

```
$ cp example.env .env
$ docker-compose up
```

Now you should have the application running on [localhost](http://localhost).

You can log in with username 'root' and password 'root'.

## Set up a local environment

A local environment is needed to run tests and debug the application.

Prerequisites:

* Python 3
* [Poetry][poetry]


```
$ poetry install
$ poetry shell
```

### Run tests

Start docker-compose and configure the app to use the database running in Docker:  

```
$ docker-compose up -d
$ cd linkely
$ POSTGRES_HOST=localhost ./manage.py test
$ docker-compose down
```

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


# API

See [the API docs][apidocs]


[poetry]: https://python-poetry.org/
[apidocs]: api.md
