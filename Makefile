run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations
	
user-get:
	curl -H 'Accept: application/json; indent=4' -u admin:123 http://127.0.0.1:8000/api/v1/users | jq

# ========================================= viewset ===============================================

musican-viewset-create:
	curl -X POST "http://127.0.0.1:8000/api/v1/musican-viewset" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 1\", \"last_name\": \"first_name 1\", \"instrument\": \"piano\"}" \
		| jq

musican-viewset-list:
	curl "http://127.0.0.1:8000/api/v1/musican-viewset" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		| jq

musican-viewset-get:
	curl "http://127.0.0.1:8000/api/v1/musican-viewset/1" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		| jq

musican-viewset-put:
	curl -X PUT "http://127.0.0.1:8000/api/v1/musican-viewset/1" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 11\", \"last_name\": \"first_name 11\", \"instrument\": \"gita\"}" \
		| jq

musican-viewset-patch:
	curl -X PATCH "http://127.0.0.1:8000/api/v1/musican-viewset/2" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 123\", \"last_name\": \"first_name 321\"}" \
		| jq

musican-viewset-delete:
	curl -X DELETE "http://127.0.0.1:8000/api/v1/musican-viewset/1" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		| jq

musican-viewset-sample-action:
	curl "http://127.0.0.1:8000/api/v1/musican-viewset/2/sample-action" \
		-u admin:123 | jq

# ========================================= Generic view ===============================================
musican-generic-views-create:
	curl -X POST "http://127.0.0.1:8000/api/v1/musican-generic-views" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 100\", \"last_name\": \"first_name 100\", \"instrument\": \"piano\"}" \
		| jq

musican-generic-views-list:
	curl "http://127.0.0.1:8000/api/v1/musican-generic-views" | jq

musican-generic-views-get:
	curl "http://127.0.0.1:8000/api/v1/musican-generic-views/4" | jq

musican-generic-views-put:
	curl -X PUT "http://127.0.0.1:8000/api/v1/musican-generic-views/4" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 111\", \"last_name\": \"first_name 111\", \"instrument\": \"violon\"}" \
		| jq

musican-generic-views-patch:
	curl -X PATCH "http://127.0.0.1:8000/api/v1/musican-generic-views/4" \
		-H "Content-Type: application/json" \
		-d "{\"instrument\": \"Organ\"}" \
		| jq


musican-generic-views-delete:
	curl -X DELETE "http://127.0.0.1:8000/api/v1/musican-generic-views/4" | jq


musican-generic-views-sample-action:
	curl "http://127.0.0.1:8000/api/v1/musican-generic-views/5/sample-action" | jq


# ========================================= API view ===============================================
musican-api-views-create:
	curl -X POST "http://127.0.0.1:8000/api/v1/musican-api-views" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 000\", \"last_name\": \"last_name 000\", \"instrument\": \"piano 000\"}" \
		| jq

musican-api-views-list:
	curl "http://127.0.0.1:8000/api/v1/musican-api-views" | jq

musican-api-views-get:
	curl "http://127.0.0.1:8000/api/v1/musican-api-views/5" | jq

musican-api-views-put:
	curl -X PUT "http://127.0.0.1:8000/api/v1/musican-api-views/5" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 999\", \"last_name\": \"last_name 999\", \"instrument\": \"piano 999\"}" \
		| jq

musican-api-views-sample-action:
	curl "http://127.0.0.1:8000/api/v1/musican-api-views/5/sample-action" | jq

