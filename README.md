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

## 2.3. create sample data

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

[music/serializers.py](music/serializers.py)

# 6. Music app

## 6.1. Create new app and migrate database

```shell
# django-admin startapp music
make makemigrations
make migrate
```
access: http://127.0.0.1:8027/swagger/

## 6.2. Views
### 6.2.1. musican-api-views

This set of apis describle how to using `APIView` to make api as basic and normal, code will be handle by yourself

**Test:**

```shell
make musican-api-views-
```

**Conclusion:**

Using api views when you want to custom detail in your api

### 6.2.2. musican-generic-views

This set of apis describle how to using `generics` view to make api code will be made shorter

**Test:**

```shell
make musican-generic-views-
```

**Conclusion:**

Using generic view when you want to combine some methods in one view, but not all, ex: only allow methods: CREATE/GET/LIST

### 6.2.3. musican-viewset

This set of apis describle how to using `ModelViewSet` to make code shortest

**Test:**

```shell
make musican-viewset-
```

**Conclusion:**

Using viewset when you want to add all methods(actions) of a object in one view, all methods will be routed automatically

### 6.2.4. musican-debug

This apis help to debug all django rest framework flow, how a request is handled through all layers of this framework

Uncomment below line in settings.py

```pythyon
MIDDLEWARE = [
    # 'main.middlewares.DebugpyMiddleware', 
```

```shell
make debug-
```

## 6.3. Serializers

### 6.3.1. Common serializer

This type of serializer you don't need to specify your model, but you must declare all neccessary fields manually

Ex: **MusicianSerializer** [music/serializers.py](music/serializers.py)

Ex: using this serializer here: [music/generic_views.py](music/generic_views.py)

### 6.3.2. Model serializer

You must specify your model in **Meta class**

You don't need to specify model field

Ex: [music/model_serializers.py](music/model_serializers.py)

# 7. Using serializer effectively

## 7.1. In read data

### 7.1.1. Using source keyword

Reference: https://medium.com/better-programming/how-to-use-drf-serializers-effectively-dc58edc73998

Using `source when you only want to get data, but not modify anything

code sample in this serializer: **MusicianModelSerializerReadEffective_SourceKeyword** in this file: [music/using_serializer_effective/serializers.py](music/using_serializer_effective/serializers.py)

- source=field_name to rename of this returned field, ex: `source='first_name'`
- source=Model.method() to get modified data, ex: `source='get_full_name'`
- source worker with relationships, ex: `OneToMany` or`ForeignKey`, `OneToOneField`, and `ManyToMany`
  - ex: `source='profile.street'` or `source='profile.city`
- source worker with methods of related objects, same `Model.method()`, ex: `source="profile.get_full_address"`
- source work with `OneToMany`, ex: `source='album_set'`. **NOTE** with `ManyToMany` don't need `source`, ex: `instruments` field

### 7.1.2. Using SerializerMethod

Using `SerializerMethod` when you want to custom more output data. For example:

- Convert `first_name` to titlecase during serialization.
- Convert `full_name` to uppercase.
- Set `albums` as `None` instead of an empty list if no groups are associated with the user.

All example in this serializer: **MusicianModelSerializerReadEffective_SerializerMethod** in file [music/using_serializer_effective/serializers.py](music/using_serializer_effective/serializers.py)

### 7.1.3. Using to_representation

Using to_representation when you want to custom mutiple data fields

All example in this serializer: **MusicianModelSerializerReadEffective_SerializerMethod** in file [music/using_serializer_effective/serializers.py](music/using_serializer_effective/serializers.py)


## 7.2. In write data

Reference: https://medium.com/@raaj.akshar/how-to-effectively-use-django-rest-framework-serializers-during-write-operations-dd73b62c26b5

### Add custom field validator

