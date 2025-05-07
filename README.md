This AI application helps user to order daily meals based on user preference

Main Tool:
    VS Code:
        live preview


Environment:
    venv：
        psycopg2 # django-postgres



AI_recomend + campusOrder + community delivery

    Manual input menu data
        simple project
        scalable project


Checklist
    1. venv
        source .venv/bin/activate
    2. dependency
        pip install -r requirements.txt
    3. Postgres
        psql -d postgres
        DROP DATABASE IF EXISTS ez_ordering_db;
        DROP ROLE IF EXISTS ez_user;
        CREATE ROLE ez_user WITH LOGIN PASSWORD {''};
        CREATE DATABASE ez_ordering_db OWNER ez_user;
        \q
    4. mod settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'ez_ordering_db',
                'USER': 'ez_user',
                'PASSWORD': 'ez_pass',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
    5. Schema
        python manage.py makemigrations
        python manage.py migrate
    6. superuser/admin
        python manage.py createsuperuser
    7. runserver
        python manage.py runserver
        http://127.0.0.1:8000/admin
    8. scripts
        python manage.py populate_tags
        python manage.py populate_protein_types
