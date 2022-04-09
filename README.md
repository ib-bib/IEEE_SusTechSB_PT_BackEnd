# IEEE SusTech Student Branch - Project Team - Back End

Here I will upload my progress on learning Django, following this [tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) on a set schedule . I am using Windows 10, so all code below will be written is specifically windows-compatible

## Installation

Install [Python](https://python.org)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Django](https://docs.djangoproject.com/en/4.0/intro/install/)

```bash
py -m pip install Django
```

Go to a directory you want your project files to reside in.

Create a [virtual environment](https://docs.python.org/3/library/venv.html)

```bash
py -m venv NameOfVirtualEnvironment
```
Install Django again within the virtual environment, and upgrade pip if you need to

## Week One - The MVT design pattern and my first view:
### polls/urls.py 
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
```
### polls/views.py
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse('Hello Django, this is the index page of the polls app')
```
### mysite/urls.py
```python
from django.contrib import admin
from django.urls import path, include  # Imported the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls', include('polls.urls')),
    # Used the include function here to route to polls
]
```
