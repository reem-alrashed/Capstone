# fsnd-capstone
## Motivation
Capstone is the final project for Udacity Full-Stack web developer nanondegree.
It uses all of the learned concepts. Including using postgres, API development using Flask, Authorization, JWT authentication and deployment using Heroku.  

Hosted app link: https://capstone-fsnd-reem.herokuapp.com/
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
## API behavior and RBAC controls
### Error handling
Errors are returned in JSON format:
```
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```
The API will return these types of errors:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 500 - internal server error
- 401 - unauthorized 

### API Endpoints
This API supports two types of resources /actors and /movies.  
Each resource support four HTTP methods; GET, POST, PATCH, DELETE

Notes

You should update the ACCESS_TOKEN in the below requests with JWT valid token.
The below requests assumes you are running the app locally, so you need to update the requests with the base URL or your URL after deployment.
#### GET /actors
General: returns a list of all actors. 

Sample request:
```
curl -X GET http://127.0.0.1:5000/actors -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"
```
Sample response:
```
{
  "actors": [
    { "age": 38, "gender": "Female", "id": 1, "name": "Lauren Cohan" },
    { "age": 42, "gender": "Male", "id": 2, "name": "Ian Somerhalder" },
  ],
  "success": true
}
```
#### GET /movies
General: returns a list of all movies  

Sample request:
```
curl -X GET http://127.0.0.1:5000/movies -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"
```
Sample response:
```
{
  "movies": [
    {
      "actors": ["Ian Somerhalder"],
      "id": 1,
      "release_date": "Mon, 19 Jun 2014 00:00:00 GMT",
      "title": "The Anomaly"
    },
    {
      "actors": ["Lauren Cohan"],
      "id": 2,
      "release_date": "Mon, 19 Jun 2014 00:00:00 GMT",
      "title": "Heavenly"
    }
  ],
  "success": true
}
```
#### POST /actors
General: create a new actor  

Sample request:
```
curl -X POST http://127.0.0.1:5000/actors -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"  -d '{"name" : "Phoebe Tonkin", "age" : "31", "gender":"Female"}'
```
Sample response: returns the new actor id
```
{ "created": 3, "success": true }
```
#### POST /movies
General: create a new movie

Sample request:
```
curl -X POST http://127.0.0.1:5000/movies -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"title" : The ring", "release_date" : "12/6/2002"}'
```
Sample response: returns the new movie id
```
{ "created": 3, "success": true }
```
#### PATCH /actors/<int:actor_id>
General: update an existing actor. 

Sample request: you can update actor's name, gender and age
```
curl -X PATCH http://127.0.0.1:5000/actors/1 -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"name" : "Ian Somerhalder"}'
```
Sample response: returns the updated actor object
```
{
  "actor": { "age": 42, "gender": "Male", "id": 1, "name": "Ian Somerhalder" },
  "success": true
}
```
#### PATCH /movies/<int:movie_id>
General: update an existing movie  

Sample request: you can update movies's title and release date
```
curl -X PATCH http://127.0.0.1:5000/movies/1 -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"title" : "New title", "release_date" : "22/12/2020"
}'
```
Sample response: returns the updated movie object which includes the actors acting in this movie
```
{
  "movie": {
    "actors": ["Ian Somerhalder"],
    "id": 1,
    "release_date": "Mon, 22 December 2020 00:00:00 GMT",
    "title": "New title"
  },
  "success": true
}
```
#### DELETE /actors/<int:actor_id>
General: delete an actor. 

Sample request:
```
curl -X DELETE http://127.0.0.1:5000/actors/1 -H "Authorization: Bearer ACCESS_TOKEN"
```
Sample response: returns the deleted actor id
```
{ "delete": 1, "success": true }
```
#### DELETE /movies/<int:movie_id>
General: delete a movie  

Sample request:
```
curl -X DELETE http://127.0.0.1:5000/movies/1 -H "Authorization: Bearer ACCESS_TOKEN"
```
Sample response: returns the deleted movie id
```
{ "delete": 1, "success": true }
```
### Authentication and authorization
This API uses Auth0 for authentication, you will need to setup Auth0 application and API.  
You need to update auth0_params variable found in config.py.


#### Existing user roles
##### Casting Assistant:
- GET /actors: can get all actors
- GET /movies: can get all movies
##### Casting Director:
All permissions of Casting Assistant
- POST /actors: can create new actors
- PATCH /actors: can update existing actors
- PATCH /movies: can update existing movies
- DELETE /actors: can delete actors from database
##### Exectutive Director:
- All permissions of Casting Director
- POST /movies: Can create new movies
- DELETE /movies: Can delete movies from database
