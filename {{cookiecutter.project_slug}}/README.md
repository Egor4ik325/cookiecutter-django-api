# {{ cookiecutter.project_name }}

## Git

If version control is needed do:

```sh
git init
git add .
git commit -m "Setup project"
git branch -M main
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

or clone:

```sh
git clone https://github.com/user/repo.git
```

## Setup

Setup locally (for VS Code):

```sh
cd server

# Python-3.10.0 using pyenv
~/.pyenv/versions/3.10.0/bin/python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Create .env.dev based on .env.dev.example
# ...

# Update pip and install development dependencies:
pip install -U pip
pip install -r requirements/dev.txt
```

Setup docker:

```sh
# Build image, create containers and attach
docker compose -f compose.dev.yml up --build
```

## Migrate

```sh
# 1. Make migrations
./manage.py makemigrations --dry-run  # see if there are changes to the models
./manage.py makemigrations  # make migration files

# 2. Apply migrations
./manage.py showmigrations  # see if there are unapplied migrations
./manage.py migrate  # apply all migrations
```

## Install a new package:

Install on local machine:

```sh
pip install package
# add "package==version" to requirements.txt...
```

Add new package to the image:

```sh
# Stop container + remove container, anonymous volume and image
# (to prevent taking a lot of memory)
docker compose -f compose.dev.yml rm --stop --volumes django
docker image rm {{ cookiecutter.project_slug }}_dev_django

# Rebuild image and recreate a container
docker compose -f compose.dev.yml up --build django
```

## Start/stop a server

```sh
docker compose -f compose.dev.yml up
docker compose -f compose.dev.yml down # or stop
```

## Create/remove a server

```sh
docker compose -f compose.dev.yml up --build
# Remove containers, networks, in-use images, dangling images, named volumes, anonymous volumes
docker compose -f compose.dev.yml down --rmi all --volumes
```

Check:

```sh
docker container ls --all
docker network ls
docker image ls --all
docker volume ls
```

## Server URLs

To get a complete list of all server URLs (admin routes + API endpoints) run
`./manage.py show_urls`.

## Registration

To turn registration on/off use boolean `DJANGO_ACCOUNT_ALLOW_REGISTRATION`
environment variable set in `.env.xxx` file.

## Documentation

OpenAPI 3.0 YAML schema is accessible from `/api/schema/` URL. Can be generated
by running `./manage.py spectacular --file schema.yml`.

Swagger UI is served from `/api/swagger/`.

## Testing

To execute tests run `pytest` in `server` folder.

## Frontend

```sh
cd app

npm install
npm start
```
