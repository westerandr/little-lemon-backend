Make sure the following dependencies are installed either through venv or pipenv:
* django
* djangorestframework
* djoser
* mysqlclient

To test Database Connection, ensure the following:
* Database 'LittleLemon' is created
* MySQL User named 'admin'@'localhost' is created and has all privileges (not just littlelemon database, this is to allow unit testing i.e. creating a test database)
* You can use any password you used to create the admin but if you use the one provided then it is fine.

user - admin
password - littlelemon@123!

Make sure to run migrations after the DB connection is established.

Serving Static Content
* Visit /restaurant for index.html
* /static/restaurant/logo.png for Image

API Routes

* Menu Route
GET, POST - /restaurant/menu
PUT, PATCH, DELETE - /resaurant/menu/<int:pk>

* Booking Route
GET, POST - /restaurant/booking/tables
PUT, PATCH, DELETE - /restaurant/booking/tables/<int:pk>

* Auth Routes
Obtain Token - /restaurant/obtain-auth-token
Login - /auth/token/login
Logout - /auth/token/logout

* User Routes
User List - GET /auth/users
Register User - POST /auth/users

Testing the Django Web API
* Run `python manage.py test`