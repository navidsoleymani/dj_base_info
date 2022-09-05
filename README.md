# Django Base Information Application

This Django application was created to create tables and APIs related to basic information, and you can use this
application to achieve APIs related to Create, Update, Destroy, Retrieve and List.

## Required

- Django
- Django Rest Framework

## Installation

```
pip install Django 
pip install djangorestframework
pip install markdown    
pip install django-filter
pip install git+https://github.com/navidsoleymani/dj_base_info.git
```

Add to your INSTALLED_APPS setting.

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'base_information',
]
```

If you are going to have a browseable API, you will. Add the following to your root urls.py file.

```
urlpatterns = [
    ...
    path('base-information/', include('base_information.urls')),
]
```