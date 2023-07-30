# Source Code Viewer Web Application (Django)  

## How to use?
$ python manage.py runserver   
go to http://127.0.0.1:8000/inspector/  

## To Do:
1. style the html files with separate CSS file (how to add CSS to Django?)
2. beautify the output HTML 
3. Publish it (?) if it isn't expensive

## How to create Django project from Macbook terminal?
$ cd Desktop  
$ mkdir sourcecode  
$ cd sourcecode  
$ pipenv install django  
$ code . (or open the new project in vscode)  
$ pipenv shell  
$ django-admin startproject sourcecode .  
$ python manage.py startapp inspector    

$ pip install urllib3
$ pip freeze > requirements.txt  

<!-- 
## From https://github.com/codesandbox/codesandbox-template-django:
$ python -m venv .venv  
$ source .venv/bin/activate  

(.venv) $ pip install -r requirements.txt  
(.venv) $ python manage.py migrate  
(.venv) $ python manage.py createsuperuser  
(.venv) $ python manage.py runserver  
Load the site at http://127.0.0.1:8000  

$ pipenv install  
$ pipenv shell  
(.venv) $ python manage.py migrate  
(.venv) $ python manage.py createsuperuser  
(.venv) $ python manage.py runserver  
Load the site at http://127.0.0.1:8000   

$ python -m venv .venv  
$ pip install django  
$ pip install urllib3  

https://codinggear.blog/how-to-upload-django-project-to-github/?expand_article=1  
-->