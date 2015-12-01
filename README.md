# CFPB Django App

CFPB Django App is an attempt to make it easy to create a standard
Django app for CFPB projects. It contains a script, `cfpb-django-app`,
which will create the starter app, a standalone Django project for
testing, starter CFPB front-end assets, and everything needed to package
both the Python and the front-end assets. It is intended to give us a
common starting point for future projects.

## Usage

```
pip install git+http://github.com/willbarton/cfpb-django-app
cfpb-django-app -d path/to/destination myapp
```

This will populate the contents of `path/to/destination` with the
following files and directories:

| File/Directory          | Purpose                                  |
|-------------------------|------------------------------------------|
| `app_name/`             | The Django app itself                    |
| `app_name_proj/`        | A Django project in which to run the app |
| `local_setup.sh`        | *Setup for local Django development*     |
| `manage.py`             | Django manage.py for the Django project  |
| `package.json`          | *NPM package definition*                 |
| `requirements.txt`      | Concrete Python requirements for the app |
| `requirements_test.txt` | Concrete Python requirements for testing |
| `setup.py`              | Python package definition                |
| `setup.sh`              | *Front-end build wrapper (npm, etc)*     |
| `src/`                  | *Front-end sources*                      |

Other features include:

- Travis integration
- flake8 integration
- *Tox integration*

*Italics* indicate areas where the resulting files or features are 
incomplete.

