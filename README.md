# django_project

## Install Django framework: 
```
pip install django
```

## Activate the newly created virtual ENV (You can use in diff ways also) : 
```
source /Users/arunsingh/Documents/django_project/.venv/bin/activate
```

## Create new project: 
```
django-admin startproject Hello
```

## Create new App: 
```
python manage.py startapp Home
```

## Start the django server: 
```
python manage.py runserver
```

## Create the new migration file (it will happen only on new changes): 
```
python manage.py makemigrations
```

## Run the migrate to create or update the DB: 
```
python manage.py migrate
```

## Create the new super user: 
```
python manage.py createsuperuser
```
