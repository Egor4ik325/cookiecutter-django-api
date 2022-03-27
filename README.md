# cookiecutter-django-api

Cookiecutter template for creating Django-backed API or SPA

## Features

- maintained as long as I enjoy doing projects

- up-to-date dependency versions

- based on the working experience

- contains best practices developed over a long time

- production-ready initial setup

- initial docker configuration

- suitable for remote machine/container development (save host resources)

For any other features go to https://github.dev/cookiecutter/cookiecutter-django
and copy & pase.

## Checklist

- [ ] React building and serving from django (docker compose in dev/prod)

- [ ] HTTPs in development and production (self signing, let's encrypt)

## Features

Features included (CONSIDERED MUST-HAVE): django, postgres, api docs, rest
framework, vscode specific, admin, allauth

Optional features: testing

Additional features: ...

## Setup

```sh
pipx install cookiecutter
```

Create a project from template:

```sh
cookiecutter cookiecutter-django-api
# > Super Project
# > super_project

# `mkdir super-project` if needed

# Move files into version controlled repository
move -r super_project/. super-project
rmdir super_project
```

Customize project:

- comment/uncomment dependencies (`base.txt`, `dev.txt`, `prod.txt`)

- configure settings (`base.py`)

- add authentication method (packages, configuration, urls)

Add version control (Git):

```sh
# Clone empty repository under version control
git clone https://github.com/user/super-project


# Commit project setup
git add .
git commit -m "Setup project"
git branch -M main
git push -u origin main
```

or initialize and add remote repo

```sh
git init
git remote add origin https://github.com/user/super-project

# Commit project setup
git add .
git commit -m "Setup project"
git branch -M main
git push -u origin main
```

## Customize

- Authentication

  - backend (allauth/token + ...)
  - method
  - profile model
  - urls

## File structure

- server (API for backend/microservice)
- app (frontend for backend)
- proxy (proxy for backend and frontend or microservice)

## Frontend

```sh
cd super_project

cookiecutter ../cookiecutter-react-spa
# > Super Project
# > app
```

## Manual configuration

- Cloud: Heroku/DigitalOcean/AWS

- CI: Github Actions/GitLab/Travis

- Mail: MailGun/SendGrid/SES

- Addons: Postgres, Celery, Redis, Whitenoise, Celery Beat, Anymail backend,
  Nginx, Flower, React

## Deployment

Options:

1. For small project (Django & React): Heroku + Netlify + Whitenoise + Mailgun +
   Porkbun

2. For bigger project (Django & React): DigitalOcean + Nginx + Let's Encrypt +
   Mailgun + Porkbun
