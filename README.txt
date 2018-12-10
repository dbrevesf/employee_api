# Employee API using Django Rest Framework (ViewSets)

- Author: Daniel Breves Ferreira
- Email: dbrevesf@gmail.com

## Description

This project is a web application composed by an API and an Administrator panel. This application was developed using Python and the web framework Django.

## API

The only endpoint of this API is /employee. So, through the
Django Rest Framework this endpoint was developed basically through the 
creation of a model, a serializer and the viewset. Viewsets are a handy class 
in Django Rest Framework that makes the creation of an API very easy. If we
don't need any sophisticated procedure other than list, create, update and
delete, all that we've got to do is to create a ViewSet passing the queryset 
and the serializer class for the correspondent model and all the work is done. 
One interesting thing is that all the restriction inserted on the models, 
like maximum length, unique condition, etc., will be verified by the viewset, 
saving us a lot of work writing verifications within the HTTP methods. 
Finally, our API has the following methods:

- GET /employee: List all the employees
- GET /employee/id: List a single employee identified by its ID
- POST /employee: Create a new employee
- UPDATE /employee/id: Update an employee identified by its ID
- DELETE /employee/id: Delete an employee identified by its ID

Another great thing about Django Rest Framework is the creation of a beautiful 
UI for the API. So, through the link http://localhost:8000/ we can have access
to the API in a friendly user interface.

## Admin

The Django web framework automatically provides an administrator panel. The
only thing that's necessary to do is to create the method __str__ within the
model class in order to inform the Django how it should exhibit the objects on 
the admin panel. To access the admin panel: http://localhost:8000/admin/

## Database

As it won't be uploaded in production and because it was a techinal challenge,
I didn't want to spend time dealing with database configs and I used the 
default database system that Django provides: SQLite. But, for bigger 
applications that will be put in production, we need to chose a more robust 
system and make sure that the databases credentials will be stored in safety
places like the operating system environment variables. 

## Tests

For this technical challenge, some unit tests were written to make sure that 
everything is working properly. They're in the file tests.py and they can be 
executed with: python manage.py test

## Requirements

As a good practice of Python development, a virtual environment was created and
all the libraries needed to run this project are presents in requirements.txt.

## Running

In order to run this project, the first thing to do is to create a virtual
environent, install the requirements and execute: 

python manage.py runserver

The application will be running at: http://localhost:8000/



