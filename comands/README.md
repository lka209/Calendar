# Start the Django project

'''
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py statapp contact
'''
# Config git

'''
git config --global user.name 'Your name'
git config --global user.email 'your_email@gmail.com'
git config --global init.defaultBranch main

# Configure .gitignore
git init
git add .
git commit -m 'Message'
git remote add origin URL_DO_GIT

# Migration of Django database
python manage.py makemigrations
python manage.py migrate

# Creating/modifying an admin password
python manage.py createsuperuser
python manage.py changepassword USERNAME

# Working with Django Model
# Import the module
from contact.models import Contact
# Create a contact (Lazy)
# Return the contact
contact = Contact(**fields)
contact.save()
# Create a contact (Non-lazy)
# Return the contact
contact = Contact.objects.create(**fields)
# Select a contact with id 10
# Return the contact
contact = Contact.objects.get(pk=10)
# Edit a contact
# Return the contact
contact.field_name1 = 'New value 1'
contact.field_name2 = 'New value 2'
contact.save()
# Deletes a contact
# Depends on the database, usually returns the number
# of values ​​manipulated in the database
contact.delete()
# Selects all contacts sorted by id DESC
# Returns QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Selects contacts using filters
# Returns QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
'''