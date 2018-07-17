# Poll'Em

Toy Django/Vue polls app as a tech stack exploration.

## Stack

The Django app uses Django REST framework and has no non-admin UI.

The Vue app is a `vue` cli created app. For development run the `vue` app
separately via `yarn start`. It uses webpack dev server to proxy to the Django
REST API.

A production setup could use nginx/haproxy to glue the two together (and
potentially also terminate SSL).

Serving the Vue app from Django is also an option, but seemed more painful if
you go all in with a Vue SPA.
