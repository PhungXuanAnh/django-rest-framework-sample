run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations
	
get-user:
	curl -H 'Accept: application/json; indent=4' -u admin:123 http://127.0.0.1:8000/users/

# ========================================= viewset ===============================================

musical-viewset-create:
	curl -X POST "http://127.0.0.1:8000/musican-viewset" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 1\", \"last_name\": \"first_name 1\", \"instrument\": \"piano\"}" \
		| jq

musical-viewset-list:
	curl "http://127.0.0.1:8000/musican-viewset" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		| jq

musical-viewset-get:
	curl "http://127.0.0.1:8000/musican-viewset/1" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		| jq

musical-viewset-put:
	curl -X PUT "http://127.0.0.1:8000/musican-viewset/1" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 11\", \"last_name\": \"first_name 11\", \"instrument\": \"gita\"}" \
		| jq

musical-viewset-patch:
	curl -X PATCH "http://127.0.0.1:8000/musican-viewset/2" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 123\", \"last_name\": \"first_name 321\"}" \
		| jq

musical-viewset-delete:
	curl -X DELETE "http://127.0.0.1:8000/musican-viewset/1" \
		-u admin:123 \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		| jq

# ========================================= Generic view ===============================================
