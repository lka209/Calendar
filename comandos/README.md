# Iniciar o progeto Django

'''
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py statapp contact
'''
# Configurar o git

'''
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configurar o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Migracion of Django base of data
python manage.py makemigrations
python manage.py migrate

# Creating/modifiend a password admin
python manage.py createsuperuser
python manage.py changepassword USERNAME

'''