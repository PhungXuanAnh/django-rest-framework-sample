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
musican-view-create:
	curl -X POST "http://127.0.0.1:8000/api/v1/musican-views" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 100\", \"last_name\": \"first_name 100\", \"instrument\": \"piano\"}" \
		| jq

musican-view-list:
	curl "http://127.0.0.1:8000/api/v1/musican-views" | jq

musican-view-get:
	curl "http://127.0.0.1:8000/api/v1/musican-views/4" | jq

musican-view-put:
	curl -X PUT "http://127.0.0.1:8000/api/v1/musican-views/4" \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 111\", \"last_name\": \"first_name 111\", \"instrument\": \"violon\"}" \
		| jq

musican-view-patch:
	curl -X PATCH "http://127.0.0.1:8000/api/v1/musican-views/4" \
		-H "Content-Type: application/json" \
		-d "{\"instrument\": \"Organ\"}" \
		| jq


musican-view-delete:
	curl -X DELETE "http://127.0.0.1:8000/api/v1/musican-views/4" | jq


musican-view-sample-action:
	curl "http://127.0.0.1:8000/api/v1/musican-views/5/sample-action" | jq
