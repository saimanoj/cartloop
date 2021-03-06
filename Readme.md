# Cartloop - Task
This task is a Django application that handles operator-client conversations. It has one GET API and one POST API.
* GET API returns details of the conversation
* POST API adds new message to the conversation
* In POST request, It check for valid characters and length of the string
* It sends an email to the client based on their active time zone (09:00-20:00)
* Used celery task to send emails every hour

## To run
### Step 1 : Clone the repository
### Step 2 : Run Docker
```
$ docker-compose build
$ docker-compose up -d
```
### Step 3 : Import Data
Send this request to import dummy data
```
GET /import_data/ HTTP/1.1
Host: http://localhost
```

## API's
#### To get conversation
```
GET /conversation/{id}/ HTTP/1.1
Host: http://localhost
```
#### To add message to conversation
```
POST /chat/ HTTP/1.1
Host: http://localhost
Content-Type: application/json
{
    "conversationId": 1,
    "chat": {
        "payload": "Sure {{ username }}. Here is your code {{ discountCode }}",
        "userId": 24
    }
}
```

### Configuration file
* Main configuration settings of the app is stored in app/settings.py
* Variables belonging to respective environments is loaded from app/.env
* Server needs to be restarted for .env file changes to take effect

### Modules
Each module has different app created and segregated into separate folders. We are currently following default Django folder structure.

##### MODULE FOLDER STRUCTURE
* Migrations : Migrations are autogenerated by Django command and used to sync database with Model definitions
* models.py: Contains Model classes, properties, methods related to the specific app. Respective database tables are created through migrations.
* urls.py: App specific URL declarations and mapped to specific method in views
* views.py: Respective Methods here are called from urls.py and sends response back to the client


```
├── app
│   ├── app
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── celerybeat-schedule
│   ├── conversation
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── decorators.py
│   │   ├── __init__.py
│   │   ├── mail.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── store
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── user
│   │   ├── admin.py
│   │    ├── apps.py
│   │    ├── __init__.py
│   │    ├── migrations
│   │    ├── models.py
│   │    ├── tests.py
│   │    ├── urls.py
│   │    └── views.py
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── initial_data.sql
│   ├── manage.py
├── docker-compose.yml
└── Readme.md
```