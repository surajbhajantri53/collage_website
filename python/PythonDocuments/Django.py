# Django Basics & Task Manager Project

# 1. Introduction to Web Frameworks
# What is a Web Framework?
A web framework is a collection of modules and tools that help developers build web applications efficiently.
Instead of writing everything from scratch, frameworks provide pre-built components like routing,
database management, and templating.

# Uses of Web Frameworks
- Faster development with reusable components.
- Security features like protection against SQL injection & XSS.
- Built-in functionalities for handling forms, authentication, and more.

# MVC Pattern vs MVT in Django
# MVC (Model-View-Controller)
- **Model: ** Handles database logic.
- **View: ** Controls UI and user interactions.
- **Controller: ** Processes input and interacts with Model & View.

# MVT (Model-View-Template) in Django
- **Model: ** Represents data(database tables).
- **View: ** Handles business logic.
- **Template: ** Controls the presentation(HTML output).

---

# 2. Introduction to Django
# What is Django?
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

# History & Design Philosophies
- Created in 2003 by Adrian Holovaty & Simon Willison.
- "Batteries-included" approach with built-in features.
- Security-first design.

# Advantages of Django
✅ Fast Development
✅ Secure(Built-in protections)
✅ Scalable
✅ Versatile(Supports various databases, APIs)

---

# 3. Installing Django & Setting Up a Project
# Installing Django
```bash
pip install django
```

# Creating a Django Project
```bash
django-admin startproject taskmanager
cd taskmanager
python manage.py runserver
```
- This creates the following structure:
  ```
  taskmanager/
      manage.py
      taskmanager/
          __init__.py
          settings.py
          urls.py
          wsgi.py
  ```

# Running the Server
```bash
python manage.py runserver
```
Visit `http: // 127.0.0.1: 8000/` to see Django's default page.

---

## 4. Creating the First App: Tasks
### Creating an App
```bash
python manage.py startapp tasks
```
This creates:
``` 
  tasks/
      migrations/
      __init__.py
      admin.py
      apps.py
      models.py
      tests.py
      views.py
  ```

### Registering the App in `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'tasks',  # Registering the tasks app
]
```

---

## 5. Creating a Simple View
### Defining a View in `tasks/views.py`
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Task Manager!")
```

### Mapping the View to a URL
Modify `taskmanager/urls.py`:
```python
from django.urls import path
from tasks.views import home

urlpatterns = [
    path('', home),
]
```
Now, visiting `http://127.0.0.1:8000/` will show "Welcome to the Task Manager!"

---

## 6. Database Setup & Creating Models
### Setting Up the Database
Django uses SQLite by default. The database is defined in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Creating the Task Model
Modify `tasks/models.py`:
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### Running Migrations
```bash
python manage.py makemigrations tasks
python manage.py migrate
```
This creates the `tasks_task` table in SQLite.

---

## 7. Admin Panel Setup
### Creating a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### Registering the Task Model in Admin
Modify `tasks/admin.py`:
```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```
Now, visit `http://127.0.0.1:8000/admin/`, log in, and manage tasks from the admin panel.

---
taskmanager/         # Root project directory
│── manage.py        # Command-line utility to manage Django project
│── taskmanager/     # Main project package
│   ├── __init__.py  # Marks this directory as a Python package
│   ├── settings.py  # Configuration file (DB, installed apps, etc.)
│   ├── urls.py      # Defines project-wide URL routing
│   ├── asgi.py      # ASGI config for async capabilities
│   ├── wsgi.py      # WSGI config for running on production servers
tasks/                 # The app that handles task management
│── migrations/        # Stores database changes (migrations)
│── __init__.py        # Marks this directory as a Python package
│── admin.py           # Registers models for Django Admin
│── apps.py            # App configuration
│── models.py          # Defines database tables (Task model)
│── views.py           # Defines what each page (view) does
│── urls.py            # Defines URL patterns for this app
│── forms.py           # Handles forms & user input
│── templates/         # Stores HTML files for this app
│── static/            # Stores CSS, JavaScript, images, etc.


## 8. CRUD Operations (Create, Read, Update, Delete)
### Creating a Form for Task Entry
Modify `tasks/forms.py`:
```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
```

### Creating Views for CRUD Operations
Modify `tasks/views.py`:
```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# List all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create a new task
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Update an existing task
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete a task
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```

---

## 9. File Uploads & Sending Emails
### Uploading an Image
- Modify models to store image fields.
- Create views & templates to handle file uploads.

### Sending Emails
- Using Django's `send_mail` & `send_mass_mail` functions.
- Sending emails with attachments.

Here’s the code for **File Uploads** and **Sending Emails** in Django.

---

### **File Uploads in Django**
#### **Step 1: Modify the Task Model to Support File Uploads**
Modify `tasks/models.py`:
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)  # File upload field

    def __str__(self):
        return self.title
```

#### **Step 2: Update Forms to Support File Uploads**
Modify `tasks/forms.py`:
```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'attachment']
```

#### **Step 3: Update Views to Handle File Uploads**
Modify `tasks/views.py`:
```python
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)  # Include request.FILES for file upload
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})
```

#### **Step 4: Modify HTML Template to Support File Uploads**
Modify `tasks/templates/tasks/task_form.html`:
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save Task</button>
</form>
```

#### **Step 5: Update Settings to Serve Uploaded Files**
Modify `settings.py`:
```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Modify `urls.py` to serve uploaded files during development:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### **Sending Emails in Django**
#### **Step 1: Configure Email Settings**
Modify `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-email-password'  # Use environment variables for security
```

#### **Step 2: Create a Function to Send Emails**
Modify `tasks/views.py`:
```python
from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request):
    subject = "Task Manager Notification"
    message = "This is a test email from Task Manager."
    from_email = "your-email@gmail.com"
    recipient_list = ["recipient@example.com"]  # Replace with actual recipient

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Email Sent Successfully!")
```

#### **Step 3: Add a URL Pattern**
Modify `tasks/urls.py`:
```python
from django.urls import path
from .views import send_email

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
]
```

Now, visiting `http://127.0.0.1:8000/send-email/` will send an email.

---

