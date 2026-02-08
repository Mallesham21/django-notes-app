# Simple Notes App for TWS Community
This is a simple notes app built with React and Django.

## Requirements
1. Python 3.9
2. Node.js
3. React

## Installation
1. Clone the repository
```
git clone https://github.com/LondheShubham153/django-notes-app.git
```

2. Build the app
```
docker build -t notes-app .
```

3. Run the app
```
docker run -d -p 8000:8000 notes-app:latest
```

## Configuration

The app defaults to SQLite for local development. To use MySQL or other databases,
set the following environment variables:

- `DB_ENGINE` (e.g. `django.db.backends.mysql`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

For security in production, set:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG` (set to `False`)
- `DJANGO_ALLOWED_HOSTS` (comma-separated list)
- `CORS_ALLOW_ALL` (set to `False`)
- `CORS_ALLOWED_ORIGINS` (comma-separated list)

## Nginx

Install Nginx reverse proxy to make this application available

`sudo apt-get update`
`sudo apt install nginx`
