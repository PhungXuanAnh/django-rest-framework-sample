run:
	.venv/bin/python manage.py runserver 127.0.0.1:8027

rm-old-data:
	rm -rf db.sqlite3

migrate:
	.venv/bin/python manage.py migrate

makemigrations:
	.venv/bin/python manage.py makemigrations

create-supperuser:
	.venv/bin/python manage.py shell -c "from django.contrib.auth.models import User; \
							User.objects.filter(username='admin').exists() or \
							User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

create-sample-data: rm-old-data migrate create-supperuser
	.venv/bin/python create_sample_data.py

user-get:
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8027/api/v1/users | jq

# ========================================= debug view ===============================================
debug-get:
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8027/api/v1/musican-debug/11 | jq

debug-list:
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8027/api/v1/musican-debug | jq

debug-create:
	curl -X POST -u admin:admin http://127.0.0.1:8027/api/v1/musican-debug \
		-u admin:admin \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 1\", \"last_name\": \"first_name 1\", \"instrument\": \"piano\"}" \
		| jq
# ========================================= viewset ===============================================

musican-viewset-create:
	curl -X POST "http://127.0.0.1:8027/api/v1/musican-viewset" \
		-u admin:admin \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 1\", \"last_name\": \"first_name 1\", \"instrument\": \"piano\"}" \
		| jq

musican-viewset-list:
	curl "http://127.0.0.1:8027/api/v1/musican-viewset" \
		-u admin:admin \
		-H "accept: application/json" \
		| jq

musican-viewset-get:
	curl "http://127.0.0.1:8027/api/v1/musican-viewset/10" \
		-u admin:admin \
		-H "accept: application/json" \
		| jq

musican-viewset-put:
	curl -X PUT "http://127.0.0.1:8027/api/v1/musican-viewset/1" \
		-u admin:admin \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 11\", \"last_name\": \"first_name 11\", \"instrument\": \"gita\"}" \
		| jq

musican-viewset-patch:
	curl -X PATCH "http://127.0.0.1:8027/api/v1/musican-viewset/2" \
		-u admin:admin \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 123\", \"last_name\": \"first_name 321\"}" \
		| jq

musican-viewset-delete:
	curl -X DELETE "http://127.0.0.1:8027/api/v1/musican-viewset/1" \
		-u admin:admin | jq

musican-viewset-sample-action:
	curl "http://127.0.0.1:8027/api/v1/musican-viewset/2/sample-action" \
		-u admin:admin | jq

# ========================================= Generic view ===============================================
musican-generic-views-create:
	curl -X POST "http://127.0.0.1:8027/api/v1/musican-generic-views" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 100\", \"last_name\": \"first_name 100\", \"instrument\": \"piano\"}" \
		| jq

musican-generic-views-list:
	curl "http://127.0.0.1:8027/api/v1/musican-generic-views" | jq

musican-generic-views-get:
	curl "http://127.0.0.1:8027/api/v1/musican-generic-views/4" | jq

musican-generic-views-put:
	curl -X PUT "http://127.0.0.1:8027/api/v1/musican-generic-views/4" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 111\", \"last_name\": \"first_name 111\", \"instrument\": \"violon\"}" \
		| jq

musican-generic-views-patch:
	curl -X PATCH "http://127.0.0.1:8027/api/v1/musican-generic-views/4" \
		-H "Content-Type: application/json" \
		-d "{\"instrument\": \"Organ\"}" \
		| jq


musican-generic-views-delete:
	curl -X DELETE "http://127.0.0.1:8027/api/v1/musican-generic-views/4" | jq


musican-generic-views-sample-action:
	curl "http://127.0.0.1:8027/api/v1/musican-generic-views/5/sample-action" | jq


# ========================================= API view ===============================================
musican-api-views-create:
	curl -X POST "http://127.0.0.1:8027/api/v1/musican-api-views" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 000\", \"last_name\": \"last_name 000\", \"instrument\": \"piano 000\"}" \
		| jq

musican-api-views-list:
	curl "http://127.0.0.1:8027/api/v1/musican-api-views" | jq

musican-api-views-get:
	curl "http://127.0.0.1:8027/api/v1/musican-api-views/5" | jq

musican-api-views-put:
	curl -X PUT "http://127.0.0.1:8027/api/v1/musican-api-views/5" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 999\", \"last_name\": \"last_name 999\", \"instrument\": \"piano 999\"}" \
		| jq

musican-api-views-sample-action:
	curl "http://127.0.0.1:8027/api/v1/musican-api-views/5/sample-action" | jq


# ========================================= Read affective ===============================================
musican-using-serializer-affective-source-keyword-list:
	curl "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-source-keyword" | jq

musican-using-serializer-affective-source-keyword-get:
	curl "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-source-keyword/1" | jq

musican-using-serializer-affective-serializer-method-list:
	curl "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-serializer-method" | jq

musican-using-serializer-affective-serializer-method-get:
	curl "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-serializer-method/1" | jq

# ========================================= Write affective ===============================================

musican-using-serializer-affective-create-fail:
	curl -X POST "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-source-keyword" \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: YPaIf55iLUaSz7KcrWT7vRoiLtInav23qIpU8RkDi2uasVyiHkiCtSQXzzWlVgO2" \
		-d "{ \"new_first_name\": \"string\", \"last_name\": \"string\", \"full_name\": \"string\", \"street\": \"string\", \"city\": \"string\", \"full_address\": \"string\", \"all_albums\": [], \"instruments\": [], \"password\": \"123\"}" \
		| jq


musican-using-serializer-affective-create-done:
	curl -X POST "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-source-keyword" \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: YPaIf55iLUaSz7KcrWT7vRoiLtInav23qIpU8RkDi2uasVyiHkiCtSQXzzWlVgO2" \
		-d "{ \"new_first_name\": \"string 1\", \"last_name\": \"string 2\", \"street\": \"string\", \"city\": \"string\", \"full_address\": \"string\", \"all_albums\": [], \"instruments\": [], \"password\": \"123abcA@\", \"profile\": 1}" \
		| jq