[![Build Status](https://travis-ci.org/mthx/pollem.svg?branch=master)](https://travis-ci.org/mthx/pollem)

# Poll'Em

Toy Django/Vue polls app as a tech stack exploration.

The Django app uses Django REST framework and has no non-admin UI.

## Development quick start

Development setup with frontend's webpack dev server proxying to the backend API.

Frontend:

```bash
$ cd frontend
$ yarn
$ yarn serve
```

Backend:

```bash
$ cd backend
$ pipenv shell
$ pipenv install --dev
$ python manage.py migrate
$ python manage.py runserver
```
