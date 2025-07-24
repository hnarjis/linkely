# linkely
Keep track of shared articles

## Technical overview

`linkely` is a Django-based web application that allows users to share and track articles. The main components are:

- **Backend**: Django application using Django ORM to interact with PostgreSQL and Elasticsearch for full-text search.
- **API**: RESTful endpoints documented in [API docs](api.md) built with Django REST Framework.
- **Frontend**: Semantic UI-powered interface, source files located under `frontend/semantic`, built with Gulp.
- **Data ingestion**: Scraper and management commands to fetch and process articles.
- **Containers**: Docker Compose configuration orchestrates services: web, database, and Elasticsearch.
- **Dependencies**: Python dependencies managed with Poetry; Node dependencies with npm.

## Getting started

Prerequisites:

* Docker
* docker-compose

Clone the repo, then run:

```
$ cp example.env .env
$ docker-compose up
```

Now you should have the application running on [localhost](http://localhost:8000).

You can log in with username 'root' and password 'root'.

If you make changes to files locally, the server should reload and
reflect the changes. Sometimes it's easier to debug things if you run
things locally, see next section.

## Set up a local environment

A local environment is needed to run tests and makes it easier to debug the application.

Prerequisites:

* Python 3
* [Poetry][poetry]


Install dependencies using `poetry`, and start a poetry shell (a
virtual environment with the dependencies loaded):

```
$ poetry install
$ poetry shell
```

You can now use `manage.py` like in a regular Django application. The
easiest way to run service dependencies is to start docker-compose
(see above). The web server will now run both locally (outside Docker)
and in Docker, so a different port needs to be used for the local
server, `8080` for example:

```
$ docker-compose up -d  # if it's not already running
$ poetry shell          # if you're not already in a shell
$ ./linkely/manage.py runserver 8080
```

If the server doesn't start, check that your `.env` file has the
correct `POSTGRES_HOST` and `ES_HOST` set, in this case they should
point to `localhost` normally.

Other useful manage.py commands are:

- `createsuperuser` - make a new admin user (root/root is there by default)
- `shell` - open a Python shell with Django already loaded, useful for
  playing around with models etc.
- `test` - run tests
- `rescrape` - run scraper on all non-scraped articles
- `remove_duplicates` - remove any duplicated articles and keep the oldest copy


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
