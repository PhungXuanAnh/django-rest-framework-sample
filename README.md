This is initial code for create sample codes in in django rest framework
---

- [1. setup environment](#1-setup-environment)
- [2. create project and app user](#2-create-project-and-app-user)
  - [2.1. create project and app:](#21-create-project-and-app)
  - [2.2. create sample data](#22-create-sample-data)
- [3. Run server](#3-run-server)
- [4. Access admin site](#4-access-admin-site)
- [5. Access users/groups apis](#5-access-usersgroups-apis)
- [6. Music app](#6-music-app)
  - [6.1. Create new app and migrate database](#61-create-new-app-and-migrate-database)
  - [6.2. Views](#62-views)
    - [6.2.1. musican-api-views](#621-musican-api-views)
    - [6.2.2. musican-generic-views](#622-musican-generic-views)
    - [6.2.3. musican-viewset](#623-musican-viewset)
    - [6.2.4. musican-debug](#624-musican-debug)
  - [6.3. Serializers](#63-serializers)
    - [6.3.1. Common serializer](#631-common-serializer)
    - [6.3.2. Model serializer](#632-model-serializer)
- [7. Using serializer effectively](#7-using-serializer-effectively)
  - [7.1. In read data](#71-in-read-data)
    - [7.1.1. Using source keyword](#711-using-source-keyword)
    - [7.1.2. Using SerializerMethod](#712-using-serializermethod)
    - [7.1.3. Using to_representation](#713-using-to_representation)
  - [7.2. In write data](#72-in-write-data)
    - [7.2.1. Add custom field validator](#721-add-custom-field-validator)
    - [7.2.2. Cross field validation](#722-cross-field-validation)
    - [7.2.3. When and how to override to_internal_value()](#723-when-and-how-to-override-to_internal_value)
    - [7.2.4. When and how to override create()](#724-when-and-how-to-override-create)
  - [7.3. Other things](#73-other-things)
    - [7.3.1. Passing a value directly to the save method](#731-passing-a-value-directly-to-the-save-method)
    - [7.3.2. Get current user of the request](#732-get-current-user-of-the-request)
    - [7.3.3. HiddenField](#733-hiddenfield)
    - [7.3.4. access serializer raw input](#734-access-serializer-raw-input)
    - [7.3.5. Override data to force ordering](#735-override-data-to-force-ordering)
    - [7.3.6. Handling multiple creates/updates/deletes in nested serializers](#736-handling-multiple-createsupdatesdeletes-in-nested-serializers)

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

## 2.2. create sample data

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

### 7.2.1. Add custom field validator

Using it when want to validate a single field

Ex: field `password` in **MusicianModelSerializerReadEffective_SourceKeyword.validate_password()**

### 7.2.2. Cross field validation

Using it when we want to add some validation where we need to access multiple field simultaneously

Ex: validate that the `first_name` and `last_name` be different in **MusicianModelSerializerReadEffective_SourceKeyword.validate()**

### 7.2.3. When and how to override to_internal_value()

`to_internal_value()`  can be used to do some pre-processing before validation code is executed

Ex 1: Frontend or mobile app sends user information enclosed in another dictionary with key `user`

```json
{
	'user': {
		'first_name': 'john',
		'last_name': 'doe',
		'username': 'john',
		'password': 'abc123#'
	}
}
```

In such case, `user` info needs to be extracted out of the dictionary before the fields are validated. We can achieve this by overriding `to_internal_value()` in **MusicianModelSerializerReadEffective_SourceKeyword.to_internal_value()**

### 7.2.4. When and how to override create()

`create()` is called when `serializer.save()` is called

create() should be overridden when we want to do something different from this default behavior.

## 7.3. Other things

### 7.3.1. Passing a value directly to the save method

```python
serializer = EmailSerializer(data=request.data)
serializer.is_valid(raise_exception=True)
serializer.save(owner_id=request.user.id)   # <------ this passed value won't be validated
											# It may be used to force an override of the initial data
```

### 7.3.2. Get current user of the request

```python
serializers.CurrentUserDefault()
```

### 7.3.3. HiddenField

HiddenField is a field class that does not take a value based on user input, but instead takes its value from a default value or callable.

```python
modified = serializers.HiddenField(default=timezone.now)
owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
```

### 7.3.4. access serializer raw input

`serializer.initial_data`

### 7.3.5. Override data to force ordering

By default, Django querysets are not ordered at all. Enforcing ordering on the list view can easily be accomplished by adding ordering to the view’s `queryset`, but in cases where nested resources should also be ordered, it’s not so simple. For read-only fields, it can be done within `SerializerMethodField`, but what to do in a situation where a field has to be writable? In such a case, a serializer’s data property can be overridden, as shown in this example:

```python
@property
def data(self):
    data = super().data
    data['phone_numbers'].sort(key=lambda p: p['id'])
    return data
```

### 7.3.6. Handling multiple creates/updates/deletes in nested serializers

There are two paths you can follow in this case:

- use the quite popular, third party library DRF Writable Nested
- do it on your own
  
I would recommend choosing the second option at least once, so you will know what’s going underneath.

After analyzing incoming data, in most scenarios, we are able to make the following assumptions:

- all items that should be updated have id,
- all items that should be created don’t have id,
- all items that should be deleted are present in data storage (eg. database), but are missing in the incoming request.data
  
Based on this, we know what to do with particular items on the list. Below is a snippet that shows this process in detail:

```python
class CUDNestedMixin(object):
    @staticmethod
    def cud_nested(queryset: QuerySet,
                   data: List[Dict],
                   serializer: Type[Serializer],
                   context: Dict):
        """
        Logic for handling multiple updates, creates and deletes
        on nested resources.
        :param queryset: queryset for objects existing in DB
        :param data: initial data to validate passed from higher
                level serializer to nested serializer
        :param serializer: nested serializer to use
        :param context: context passed from higher level
                serializer
        :return: N/A
        """
        updated_ids = list()
        for_create = list()
        for item in data:
            item_id = item.get('id')
            if item_id:
                instance = queryset.get(id=item_id)
                update_serializer = serializer(
                    instance=instance,
                    data=item,
                    context=context
                )
                update_serializer.is_valid(raise_exception=True)
                update_serializer.save()
                updated_ids.append(instance.id)
            else:
                for_create.append(item)

        delete_queryset = queryset.exclude(id__in=updated_ids)
        delete_queryset.delete()

        create_serializer = serializer(
            data=for_create,
            many=True,
            context=context
        )
        create_serializer.is_valid(raise_exception=True)
        create_serializer.save()
```

And here is the simplified version of how a high-level serializer can make use of this mixin:

```python
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer,
                        CUDNestedMixin):
    phone_numbers = PhoneSerializer(
        many=True,
        source='phone_set',
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_numbers')

    def update(self, instance, validated_data):
        self.cud_nested(
            queryset=instance.phone_set.all(),
            data=self.initial_data['phone_numbers'],
            serializer=PhoneSerializer,
            context=self.context
        )
        ...
        return instance
```

Keep in mind that nested objects should consume `initial_data` instead of `validated_data`. That’s because running validation calls `field.to_internal_value()` on each of a serializer’s fields, which may modify data stored by a particular field (eg. by changing primary key to model instance).
