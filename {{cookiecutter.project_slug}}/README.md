# {{ cookiecutter.project_name }}

## 1. Git

Initialize:

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
git clone https://github.com/user/thisproject.git
git commit -m "Setup project"
git branch -M main
```

## 2. Local setup

Setup locally, on host (e.g. for VS Code) using `venv` module:

```sh
# Create .env.dev environment variables file based on .env.dev.example
# ...

cd server

# Create env using using python-3.10.0 (pyenv )
~/.pyenv/versions/3.10.0/bin/python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Update pip and install development dependencies:
pip install -U pip
pip install -r requirements/dev.txt
```

## 3. Docker

Create/start a server:

```sh
# Build image, create containers and attach
docker compose -f compose.dev.yml up --build

docker compose -f compose.dev.yml up
```

Stop/remove a server:

```sh
docker compose -f compose.dev.yml down
# or docker-compose -f compose.dev.yml stop

# Remove containers, networks, in-use images, dangling images, named volumes, anonymous volumes
docker compose -f compose.dev.yml down --rmi local \
    --volumes  # remove mounted volumes (eg. source code)
```

> To check, run: `docker container ls --all`, `docker network ls`, `docker image ls --all`, `docker volume ls`

## 4. Frontend

```sh
cd app

npm install
npm start
```

## Install a new package:

Locally:

```sh
pip install package

# Add `package==version` to requirements.txt
# ..
```

Docker:

```sh
docker compose -f compose.dev.yml down --rmi local
docker compose -f compose.dev.yml up --build
```

## Migrations

Make migrations:

```sh
# See if there are changes to the models
./manage.py makemigrations --dry-run
# Make migration files
./manage.py makemigrations
```

Apply migrations:

```sh
# See if there are unapplied migrations
./manage.py showmigrations
# Apply all migrations
./manage.py migrate
```

## Features

-   admin interface
-   swagger ui api docs
-   development/production separation
-   docker compose setup
-   pre-defined authentication

## Configuration

All sensitive configuration settings should be specified through environment variable fields (`.env.dev` and `.env.prod`).

## Server URLs

To get a complete list of all server URLs (admin routes + API endpoints) run
`./manage.py show_urls`.

## Registration

To turn registration on/off use boolean `DJANGO_ACCOUNT_ALLOW_REGISTRATION`
environment variable set in `.env.xxx` file.

## Administration

To create admin user run `./manage.py createsuperuser`.

Admin interface is served from `/admin/`.

## Documentation

OpenAPI 3.0 YAML schema is accessible from `/api/schema/` URL. Can be generated
by running `./manage.py spectacular --file schema.yml`.

Swagger UI is served from `/swagger/`.

## Testing

To execute tests run `pytest` in `server` folder if they are available.

## Production

Create `.env.prod` based on `.env.prod.example` in `server` folder.

Run a production compose:

```sh
docker compose -f compose.prod.yml up --build
```

Run commands inside created django container:

```sh
docker compose -f compose.prod.yml run --rm django bash
```
