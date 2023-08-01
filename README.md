# Source Code Viewer Web Application (Django)  
This website gets a url and returns the HTML (source code) of the website.   

This code doesn't work on vercel (yet) so I copy-pasted my code to their Django template so it would deploy. I need to rewrite this code but for now its running here:  https://django-source-code.vercel.app/  
(I haven't fixed it yes, so it gives 403 error for some websites and don't work without cookies😅)  

![notes](notes1.jpg)  
![notes](notes2.jpg)  

## How to use?
$ python manage.py runserver   
go to http://127.0.0.1:8000/inspector/  

## To Do:
1. style the html files with separate CSS file (how to add CSS to Django?)
2. beautify the output HTML 
3. Publish it (?) if it isn't expensive
4. Fix the code so it'll work with: diabled cookies, websites that return 403 error,
5. Add tests
6. Add the url that was given in the input to the output url (/output/https://google.com) 

## How to create Django project from Macbook terminal?
$ cd Desktop  
$ mkdir sourcecode  
$ cd sourcecode  
$ python3 -m venv .venv  
$ source .venv/bin/activate 
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
