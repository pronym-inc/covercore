# Pronym Service Template - RENAME THIS!!!!

## Project Summary

Some high-level, non-developer-friendly understanding of what this application is and why it's useful.  E.g., this is an application for users to track their time and bill clients.

Do not make this more than a paragraph.

## Development Setup

### Prerequisites

- Python 3.8 (should be available at command line as `python3.8`)
- Postgres Server (installed and running locally)
- An SSH Key configured to use with your GitHub account, which has access to the pronym-inc organization.

### Getting environment setup
You should be able to get started with a few commands.

```
$ git clone git@github.com:pronym-inc/covercore.git
Cloning into covercore ...
...
$ cd covercore
$ install/setup.sh
Creating database...
...
```

### Running the web server
A `manage.py` script is provided in the root of the directory which can be used for interacting with the Django application.
To run the webserver:
```
$ ./manage.py runserver
```

### Running tests
##### Unit Tests
```
$ venv/bin/pytest covercore/tests
```
##### Integration Tests
```
$ venv/bin/pytest covercore/integration_tests
```