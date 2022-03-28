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

- [x] Https in development + error debugging

- [x] React building and serving from django (docker compose in dev/prod)

- [ ] HTTPs in production (self signing, let's encrypt)

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

Options for deploying Django/React project:

1. Small project: PaaS

   - hosting services: heroku + netlify
   - https is managed by: heroku and netlify subdomains
   - backend static files: whitenoise
   - backend: git+slug / docker+runtime/manifest
   - database: heroku postgres

2. Medium project: VPS + PaaS

   - hosting: digitalocean + netlify
   - backend: docker + docker compose + ubuntu
   - static files: whitehoise / nginx
   - backend https certificate: self-signed (standalone) or letsencrypt (nginx)
   - frontend https certificate: netlify subdomain
   - database: self-hosted postgres container

3. Big project: VPS/IaaS

   - hosting: digitalocean
   - backend: docker compose
   - frontend: built into static files (+served from backend)
   - proxying: nginx (/nginx-proxy/nginx-proxy-manager)
   - static files management: nginx (/ CDN service (s3))
   - https certificate: letsencrypt (nginx) / service (cloudflare)
   - database: container (/ managed service Amazon RDS)
   - redis: self-hosted / managed service

4. Large project: VPS + AWS services

   - compute: Amazon EC2
   - object storage: Amazon S3
   - database: Amazon RDS (PostgreSQL)
   - caching/broker: Amazon MQ/Amazon MemoryDB
   - domains: Amazon
   - serverless?
   - ...

For any options:

- domains: pornbun
- transactional email service: mailgun
- database: postgres

## HTTPs

Sometimes you may want to run your API server under HTTPs in development. For
this case self-signed certificates will be the best way to go.

Backend:

- development: self-signed certificate
- production: authority issued certificate (Let's Encrypt)
