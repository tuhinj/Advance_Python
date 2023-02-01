:Django_Project_&_Dipendici:
============================
Step-1 (Directory):
-------------------
> Creat a project folder and open it in VS code.

`Ex: my_project`

> Open termminal and install pip, pipenv, and django.

`ctl + til`

Step-2 (Installation):
----------------------
> Install pip.

`sudo apt install pip`

> Install pipenv.

`pip install pipenv`

> Creat Virtual Enveroment.

`pipenv shell`

> Install Django.

`pipenv install django`

Step-3 (Project):
-----------------
> Creat Django project.

`django-admin startporject project_name .` (dot for create django dipendici in prasent folder)

> Live the project.

`python3 manage.py runserver` (out this process 'ctl + c' select)

Step-4 (App):
-------------
> Creat app.

`python3 manage.py startapp my_app`

> Edit 2 file for link the app with the project (setting.y, urls.py)

`myProject > settings.py > edit:INSTALLED_APP = ['my_app']`

`myProject > urls.py > edit:from django.urls import path,include > urlpatterns = [ path('',include('my_app.urls')),]`

> Creat urls.py in my_app directory and add this code.

`from django.contrib import admin <enter> from django.urls import views <enter> urlpatterns = []`





