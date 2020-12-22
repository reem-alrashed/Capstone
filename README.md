# fsnd-capstone
## Motivation
Capstone is the final project for Udacity Full-Stack web developer nanondegree.
It uses all of the learned concepts. Including using postgres, API development using Flask, Authorization, JWT authentication and deployment using Heroku.
## Project dependencies, local development and hosting instructions
This section will introduce you to how to run and setup the app locally.

### Dependencies
This project is based on Python 3 and Flask.

Installing dependencies:
```
$ pip install -r requirements.txt
```

### Local connection
Install postgres database and run it. then update database_params variable found in config.py file as shown below:
```
database_params = {
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "db_name": "casting_agency",
    "dialect": "postgresql"
}
```
Update auth0_params variable found in config.py with auth0 configurations
```
auth0_params = {

    "AUTH0_DOMAIN": 'dev-2ehmkqm9',
    "ALGORITHMS": ['RS256'],
    "API_AUDIENCE": "capstone"
}
```
Run the app locally
```
export FLASK_APP=app.py
flask run
```
Run test cases
You can run the unit test cases that are defined in test.py using the below command:
```
python test.py
```
