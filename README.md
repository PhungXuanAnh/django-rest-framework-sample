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

# mac 
brew install jq
# ubuntu
sudo apt-get install jq -y
```

# 2. create project and app user

create this app as link: https://www.django-rest-framework.org/tutorial/quickstart/

## 2.1. create project and app:

```shell
django-admin startproject main .
django-admin startapp user
```

## 2.2. reset db and create supper user

```shell
rm -rf db.sqlite3
make migrate
make create-supperuser
```

## 2.3. create normal user

```shell
make create-sample-data
```

# 3. Run server

make run

# 4. Access admin site

http://127.0.0.1:8027/admin

Account as above: admin/admin

# 5. Access users/groups apis

http://127.0.0.1:8027/api/v1

login by above account: admin/admin

or by command: 

```shell
make user-get
```

# 6. New music app

## 6.1. Create new app and migrate database

```shell
# django-admin startapp music
make makemigrations
make migrate
```
access: http://127.0.0.1:8027/swagger/

## 6.2. musican-api-views

This set of apis describle how to using `APIView` to make api as basic and normal, code will be handle by yourself

```shell
make musican-api-views-
```

## 6.3. musican-generic-views

This set of apis describle how to using `generics` view to make api code will be made shorter

```shell
make musican-generic-views-
```

## 6.4. musican-viewset

This set of apis describle how to using `ModelViewSet` to make code shortest

```shell
make musican-viewset-
```


## 6.5. musican-debug

This apis help to debug all django rest framework flow, how a request is handled through all layers of this framework

Uncomment below line in settings.py

```pythyon
MIDDLEWARE = [
    # 'main.middlewares.DebugpyMiddleware', 
```

```shell
make debug-
```
