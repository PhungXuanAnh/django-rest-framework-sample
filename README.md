This is initial code for create sample codes in in django rest framework
---


# 1. setup environment

```shell
pyenv install -v 3.8.0
pyenv local 3.8.0
python --version
which python
venv-create     # if it detect wrong version of python, it need to open another shell
.venv
which python
pip install -r requirements.txt
```

# 2. create project and app user

create this app as link: https://www.django-rest-framework.org/tutorial/quickstart/

## 2.1. create project and app:

```shell
django-admin startproject main .
django-admin startapp user
```

## 2.2. create supper user

```shell
rm -rf db.sqlite3
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
```

## 2.3. create normal user

python create_sample_data.py

# 3. Run server

make run

# 4. Access admin site

http://127.0.0.1:8000/admin

Account as above: admin/123

# 5. Access users/groups apis

http://127.0.0.1:8000/users/
http://127.0.0.1:8000/groups/

login by above account: admin/123

or by command: 

```shell
make test-get-user
```

# New music app

## Create new app

```shell
django-admin startapp music
python manage.py makemigrations
python manage.py migrate
```

access: http://127.0.0.1:8000/swagger/

