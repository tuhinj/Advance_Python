**Django_Project_&_Dipendici:**
================================
***Step-1 (Directory):***
-------------------
> Creat a project folder and open it in VS code.

`Ex: my_project`

> Open termminal and install pip, pipenv, and django.

`ctl + til`

***Step-2 (Installation):***
----------------------------
> Install pip.

`sudo apt install pip`

> Install pipenv.

`pip install pipenv`

> Creat Virtual Enveroment.

`pipenv shell`

> Install Django.

`pipenv install django`

*Check dependency*
`pip freeze

***Step-3 (Project):***
-----------------------
> Creat Django project.

`django-admin startporject project_name .` (dot for create django dipendici in prasent folder)

> Live the project.

`python3 manage.py runserver` (out this process 'ctl + c' select)

***Step-4 (App):***
-------------
> Creat app.

`python3 manage.py startapp my_app`

> Edit setting.y

`myProject > settings.py > edit:INSTALLED_APP = ['my_app']`

> Edit models.py

`my_App > models.py > edit: from django.db import models <eter> <enter> class Product(models.Model):<enter>    name = models.CharField(max_length=200)<enter>    price = models.DecimalField(max_digits=8, decimal_places=2)<enter>    details = models.TextField()`

> Make database by migration

`python manage.py makemigrations`

> Add models.py data in migration database

`python manage.py migrate`

> Create Super user

`python manage.py createsuperuser`

*=> usern: "usern", email: "any email", passwd: "any passwd"*

> Run server again 

`python manage.py runserver`

*=> 127.0.01:8000/admin > login: usern, passwd*

> Model class register in admin panal

`my_App > admin.py > edit: from django.contrib import admin <enter> from .models import Product <enter> # Register your models here.<enter> admin.site.register(Product)`

> View the product name edit midels.py file

`my_App > models.py > (same class add new function)edit: def __str__(self):<enter>        return self.name`

> Make view in Views.py for user

`


`myProject > urls.py > edit:from django.urls import path,include > urlpatterns = [ path('',include('my_app.urls')),]`

> Creat urls.py in my_app directory and add this code.

`from django.contrib import admin <enter> from django.urls import views <enter> urlpatterns = []`





