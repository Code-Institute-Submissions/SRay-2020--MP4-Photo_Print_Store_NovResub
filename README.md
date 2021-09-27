



## Gitpod Reminders
----------------
To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

python3 -m http.server

A blue button should appear to click: Make Public,

Another blue button should appear to click: Open Browser.

To run a backend Python file, type python3 app.py, if your Python file is named app.py of course.

A blue button should appear to click: Make Public,

Another blue button should appear to click: Open Browser.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the sudo (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

Log in to your Heroku account and go to Account Settings in the menu under your avatar.
Scroll down to the API Key and click Reveal
Copy the key
In Gitpod, from the terminal, run heroku_config
Paste in your API key when asked
You can now use the heroku CLI program - try running heroku apps to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with Regenerate API Key.

## REQUIREMENTS

----------------

pip3 install -r requirements.txt

Creating New Apps
python3 manage.py startapp 'name'

Add to INSTALLED APPS in Settings.py

Setting Up Django Project
pip3 install django

django-admin startproject boutique_ado . - Creates files we'll need (settings.py, urls.py etc.)

touch .gitignore (create our git ignore file)

python3 manage.py runserver (Run project)

python3 manage.py migrate - To run migrations

python3 manage.py createsuperuser - To create admin user 23rd/09th - sray2021 pword = photoprints1

## Initial Commit

----------------------

Django-Allauth for authorisation
pip3 install django-allauth==0.41.0

Add allauth additional settings to settings and urls.py fils (see video Allauth Setup 1)

Navigate to admin of site - open port 8000 /admin + login details

Migrate app for new additions (python3 manage.py migrate)

Migrations
python3 manage.py makemigrations --dry-run

python3 manage.py makemigrations

python3 manage.py migrate --plan

python3 manage.py migrate

Loading Data
python3 manage.py loaddata frames

python3 manage.py loaddata prints

## Quickstart for project

------------------- 

pip3 install -r requirements.txt

python3 manage.py makemigrations --dry-run

python3 manage.py makemigrations

python3 manage.py migrate --plan

python3 manage.py migrate

python3 manage.py loaddata categories

python3 manage.py loaddata products

export STRIPE_SECRET_KEY=sk_test_51JYSDEAQb6q0x2KwYN4xfF2sbuhyLr1PP3L75QVtfa54AHeOZKL4LtABmw8R5CrElDKq6kDnLfsrMiGvQnmk7SuC00Che5f4US (old)

export STRIPE_PUBLIC_KEY=pk_test_51JYSDEAQb6q0x2KwgVMPWeio4ynVOjfeAOYiTKJY5j1PuNt9fq5ydDkuAeave2L5qf5YqBphC2KCkmhqzVQ0yQxA00dRAxgEED(old)

python3 manage.py runserver

## Heroku Login

---------------------------

If heroku login doesn't work, use

'heroku login -i'

'git push -u heroku' - *** No master!

## Code Refactoring
----------------
python3 -m flake8


## Making Templates 
--------------------

mkdir templates