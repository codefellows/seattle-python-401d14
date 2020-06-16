# Django Models

## Installation
```bash
poetry init -n
poetry add django
poetry add --dev black
poetry shell
```

### Create a django project
```bash
django-admin startproject snacks_project
tree snacks_project
```

### Create a django app
```bash
cd snacks_project/
python manage.py startapp snacks
tree
```

### Start the server
```bash
python manage.py runserver
```

### Migrate and Create DB
```bash
python manage.py migrate
```

## Views

### Create HomePageView

- Go to views.py

```python
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

```

### Setup the views

- Go to projects urls.py

```python
from django.urls import path, include

# inside urlpatterns
    path('', include('snacks.urls')),
```

### Add urls to app

- Create urls.py inside the app
- Add this code

```python
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

### Create a home page
- Create templates folder on the root
- Create home.html inside templates folder

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Snacks</title>
</head>
<body>
    <main>
        <h1>Welcomes to Snacks App</h1>
    </main>
</body>
</html>
```

### Fix the settings
- Go to settings.py

'DIRS': [os.path.join(BASE_DIR, 'templates')],



## Models

### Create a model
In models.py

```python
class Snack(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField()
    eater = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

- Cascade means when eater is deleted then snack should be deleted as well

### Add the model to be part of the project
- Go to settings under the projects
- Under Installed_Apps, add **'snacks.apps.SnacksConfig'**
- This means snacks folder => apps folder => SnackConfig class

### Sync model with database
```bash
python manage.py makemigrations
```
- Migrations with SQLite but in the future we will use PostgresSQL

- Apply the migrations:
```bash
python manage.py migrate
```

## Admin

### How to work with models? Admin is the way to go for now
- Go to /admin
- No access? Create a user

### Create a user
```bash
python manage.py createsuperuser
python manage.py runserver
```

### Register the model so tables show
- Go to admin.py

```python
from .models import Snack

admin.site.register(Snack)
```

### Add Data in admin

### Back to views, let's view the snacks
- Add snacks view to the views.py

```python
from django.views.generic import TemplateView, ListView
from .models import Snack

class HomePageView(TemplateView):
    template_name = 'home.html'

class SnacksView(ListView):
    template_name = 'snacks.html'
    model = Snack
```

### Add to urls

from .views import HomePageView, SnacksView

urlpatterns = [
     path('snacks/', SnacksView.as_view(), name='snacks'),
]

### Create the template
```html
<main>
        <h1>List of Snacks</h1>
        <ul>
            <li>1</li>
            <li>2</li>
        </ul>
    </main>
```

### Create base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Django Snacks</title>
</head>
<body>
  {% block content %}
  {% endblock content %}
</body>
</html>
```

### Modify home.html
```html
{% extends 'base.html' %}

{% block content%}
<h1>Welcomes to Snacks App</h1>
{% endblock content%}
```

### Modify snacks.html
```html
{% extends 'base.html' %}

{% block content %}
  <ul>
      <li>1</li>
      <li>2</li>
  </ul>
{% endblock content %}
```

### Render snacks (snacks.html)
```html
{% extends 'base.html' %}

{% block content %}
<h3>Snacks List</h3>

    {% for snack in object_list %}
    <h6>{{ snack.name }}</h6>
    {% endfor %}

{% endblock content %}
```


## Detailed View

### Link every Snack to a detailed page
Where to go? snacks/1 maybe???????

### Make a view
```python
from django.views.generic import TemplateView, ListView, DetailView

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack
```

### Add a url
```python
from .views import HomePageView, SnacksView, SnackDetailsView

urlpatterns = [
    path('snack/<int:pk>', SnackDetailsView.as_view(), name='snack_details')
]
```
### Create html file (snack_details.html)
```html
{% extends 'base.html' %}

{% block content %}
<h4>{{ snack.name }}</h4>
<h4>{{ snack.eater }}</h4>
{% endblock content %}
```


### Modify snacks.html
```html
    <h6><a href="{% url 'snack_details' snack.pk %}">{{ snack.name }}</a></h6>

```

## Migration

### Add a new field to model
```python
rank = models.IntegerField()
```

### Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

### Change the views
- Add the new field (rank)


## Styling

### Add styling
- Create a folder named static
- Inside static folder add the css files
- Add link to base.html
```html
{% load static %}
<link rel="stylesheet" href="{% static 'base.css' %}">
```
- Add to CSS file:
```css
h3{
    color:red;
}
```

### Add static files to settings.py
**STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]**


