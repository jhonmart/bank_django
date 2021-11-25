# Django Bank

[![.github/workflows/github-actions-demo.yml](https://github.com/jhonmart/bank_django/actions/workflows/github-actions-demo.yml/badge.svg)](https://github.com/jhonmart/bank_django/actions/workflows/github-actions-demo.yml)

# Commands used
``` 
pip install -r requirements.txt
django-admin startproject bradesco .
python manage.py startapp users 

python manage.py runserver 3000

python manage.py migrate
python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate
```

# User object
```json
{
  "name": "Nome Sobrenome",
  "birthday": "2021-11-24",
  "sex": "Masculino",
  "email": "pessoa.email@server.com",
  "password": "ij19031hh7!"
}
```
