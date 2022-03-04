# {{ cookiecutter.project_name }}

## Setup

Preferred `python 3.10`.

Create virtual environment using `venv` module (yes I prefer more control):

```sh
cd server

# If installed using `pyenv` (but not set as global)
~/.pyenv/versions/3.10.0/bin/python -m venv .venv
```

Update pip and install development dependencies (for local environment):

```sh
cd server

pip install -U pip
pip install -r requirements/dev.txt
```

Build docker images:

```sh
docker compose -f compose.dev.yml build
docker compose -f compose.dev.yml up
```
