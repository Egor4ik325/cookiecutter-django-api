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

## File structure

- server (API for backend/microservice)

## Manual configuration

```json
{
  "cloud_provider": ["AWS", "GCP", "None"],
  "mail_service": ["Mailgun"],
  "use_compressor": "n",
  "use_sentry": "n",
  "use_whitenoise": "n",
  "use_heroku": "n",
  "ci_tool": ["None", "Travis", "Gitlab", "Github"]
}
```
