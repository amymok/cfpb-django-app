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
| `.bowerrc`              | Bower configuration                      |
| `.covereagerc`          | Coverage configuration                   |
| `.travis.yml`           | *Travis configuration*                   |
| `app_name/`             | The Django app itself                    |
| `app_name_proj/`        | A Django project in which to run the app |
| `bower.json`            | *The bower package definition*           |
| `develop.sh`            | Setup for local Django development       |
| `manage.py`             | Django manage.py for the Django project  |
| `package.json`          | *NPM package definition*                 |
| `requirements.txt`      | Concrete Python requirements for the app |
| `requirements_test.txt` | Concrete Python requirements for testing |
| `setup.py`              | Python package definition                |
| `setup.sh`              | *Front-end build wrapper (npm, etc)*     |
| `src/`                  | *Front-end sources*                      |
| `tox.ini`               | Tox configuration                        |

Other out-of-the-box features include:

- `develop.sh` script for setup ease
- nose and coverage integration for Python testing and code-coverage
- Tox integration for local multiple environment testing 
- Travis integration for Travis testing
- flake8 integration for Python linting
- Python 3.4 and 2.7 support

*Italics* indicate areas where the resulting files or features are 
incomplete.

### `develop.sh`

```
develop.sh
```

Once you've created your Django app you can start developing it. The
included `develop.sh` script is an easy way to get the basic environment
set up (for developers and for anyone else who may need to run it
locally.)

`develop.sh` creates the Python virtual environment, installs the app
runtime and testing requirements, initializes a SQLite database for the
local Django project, and has support for loading fixture data and
rebuilding a Haystack index. It will also run the front-end `setup.sh`
script to install NPM and Bower packages and run grunt or gulp to build
front-end assets.

If the virtual environment already exists, `develop.sh` will assume that
the remainder of the setup steps have been performed and will serve as a
wrapper for `workon`, activating the virtual environment.

This effectively means `develop.sh` should be usable the first time
someone needs to run the app locally, as well as all subsequent times.

### Testing (nose, coverage, flake8, Tox, and Travis)

```
python manage.py test
```

For testing your Django app, and keeping track of test coverage,
[nose](http://nose.readthedocs.org/en/latest/), 
[coverage](http://coverage.readthedocs.org/en/coverage-4.0.3/), and 
[django-nose](https://django-nose.readthedocs.org/en/latest/) are
included by default. The tests for your app are easily run by using the
`test` management command. The `setup.py` `test` command will also run
the tests. Code coverage will be included.

```
flake8 [app_name] --exclude=migrations
```

[flake8](https://flake8.readthedocs.org/en/latest/), a static syntax and 
style checker for your Python code, is also included in the test 
requirements (along with its dependencies), and can be invoked with the 
above command.

```
tox
```

All of the above can be invoked across multiple Python versions (2.7 and
3.4, by default) using Tox, for local automated testing, and Travis, for 
automated testing of the upstream repository. Configuration is included.

## TODO

- Include grunt or gulp for front-end building
- Make front-end build/packaging work
- Build out front-end sources
- Integrate front-end testing with Tox and Travis

