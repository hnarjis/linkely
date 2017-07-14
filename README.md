# linkely
Keep track of saved articles

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
$ ./manage.py runserver
```

Now you should have the application running on [localhost:8000](http://localhost:8000)