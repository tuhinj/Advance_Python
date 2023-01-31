:Django_Project_&_Dipendici:
============================
Step-1:
-------
> Creat a project folder and open it in VS code.

`Ex: my_project`

> Open termminal and install pip, pipenv, and django.

`ctl + til`

Step-2:
-------
> Install pip.

`sudo apt install pip`

> Install pipenv.

`pip install pipenv`

> Creat Virtual Enveroment.

`pipenv shell`

> Install Django.

`pipenv install django`

Step-3:
-------
> Creat Django project.

`django-admin startporject project_name .` (dot for create django dipendici in prasent folder)

> Live the project.

`python3 manage.py runserver` (out this process 'ctl + c' select)

> Creat app.

`python3 manage.py startapp my_app`

Step-4:
-------
> Edit 2 file for link the app with the project (setting.y, urls.py)

`myProject > settings.py > edit:INSTALLED_APP = ['my_app']`

`myProject > urls.py > edit:from django.urls import path,include > urlpatterns = [path('admin/', admin.site.urls), path('',include('my_app.urls')),]




