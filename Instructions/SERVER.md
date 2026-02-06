# Deployment Configuration – Django on Ubuntu 20.04 LTS
First steps

Prepare local_settings.py
Create your Ubuntu 20.04 LTS server (wherever you prefer)
python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"

# Create SSH key

ssh-keygen -C 'COMMENT'

# On the server
ssh user@SERVER_IP

# Initial system commands

sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.11-venv -y

sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git -y

# Git configuration
git config --global user.name 'Your name'
git config --global user.email 'your_email@gmail.com'
git config --global init.defaultBranch main

# Create progect folders and repositories
mkdir ~/agendarepo ~/agendaapp

# Configure repositories (server)

cd ~/agendarepo
git init --bare
cd ..
cd ~/agendaapp
git init
git remote add agendarepo ~/agendarepo
git add .
git commit -m 'Initial'
git push agendarepo main -u # error

# On your local computer
git remote add agendarepo user@SERVER_IP:~/agendarepo

git push agendarepo main
# Back on the server
cd ~/agendaapp
git pull agendarepo main
# PostgreSQL configuration
sudo -u postgres psql

create role agenda_user with login superuser createdb createrole password 'agenda_user_password';
create database agenda_project with owner agenda_user;

grant all privileges on database agenda_project to agenda_user;
\q
sudo systemctl restart postgresql
# Create local_settings.py on the server
nano ~/agendaapp/project/local_settings.py
Paste your configuration data
# Django environment setup
cd ~/agendaapp
python3.11 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install django
pip install pillow
pip install gunicorn
pip install psycopg
pip install faker

python manage.py runserver
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
# Allow larger uploads in Nginx
sudo nano /etc/nginx/nginx.conf
Add inside http {}:
client_max_body_size 30M;
sudo systemctl restart nginx