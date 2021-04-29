pylint-gen-rcfile:
	.venv/bin/pylint --generate-rcfile > pylintrc

pylint-test-config-file-pylintrc:
	.venv/bin/pylint --rcfile=.pylintrc manage.py

create-ssl-certificate: 
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx/certs/key.pem -out nginx/certs/cert.pem

create-nginx-account:
	# reference here: https://github.com/PhungXuanAnh/tech-note/blob/master/devops/nginx/nginx-configuration-snippets.md#enable-basic-authentication
	sudo apt-get install apache2-utils -y
	htpasswd nginx/htpasswd admin

run:
	reset && .venv/bin/python manage.py runserver 127.0.0.1:8027

# ============================== sqlite =================================
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

create-sample-data: rm-old-data migrate makemigrations create-supperuser
	.venv/bin/python scripts/create_sample_data.py

# ============================== postgres - docker =================================
docker-rm-old-data:
	docker-compose down
	docker volume rm django-rest-framework-sample_postgres_data
	docker-compose up -d
	sleep 3

docker-migrate:
	docker exec my-sample-backend python3 manage.py migrate

docker-makemigrations:
	docker exec my-sample-backend python3 manage.py makemigrations

docker-create-supperuser:
	docker exec my-sample-backend python3 manage.py shell -c "from django.contrib.auth.models import User; \
								User.objects.filter(username='admin').exists() or \
								User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

docker-create-sample-data: docker-rm-old-data docker-migrate docker-makemigrations docker-create-supperuser
	docker exec my-sample-backend python3 scripts/create_sample_data.py

# ================================ test get user =========================================
user-get:
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8027/api/v1/users | jq

user-get-via-nginx-http:
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:81/api/v1/users | jq

user-get-via-nginx-https:
	curl -k -H 'Accept: application/json; indent=4' -u admin:admin https://127.0.0.1:444/api/v1/users | jq

# ========================================= debug view ===============================================
debug-get:
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8027/api/v1/musican-debug/11 | jq

debug-list:
	reset && curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8027/api/v1/musican-debug?page_size=3 | jq

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
	# reset && curl "http://127.0.0.1:8027/api/v1/musican-generic-views" | jq
	reset && curl "http://127.0.0.1:8027/api/v1/musican-generic-views?page_size=250" | jq

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

musican-using-serializer-affective-SerializerMethod-list:
	curl "http://127.0.0.1:8027/api/v1/musican-using-serializer-affective-serializer-method" | jq

musican-using-serializer-affective-SerializerMethod-get:
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

## ================================================== ordering filter search ==================================
## ----------------------- ordering ---------------------------------
musican-sample-ordering-list-ORDERING-email:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-ordering?ordering=email" | jq

musican-sample-ordering-list-ORDERING-email-last_name:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-ordering?ordering=email,last_name" | jq

## ----------------------- search ---------------------------------
musican-sample-search-list-SEARCH-city:
	curl "http://127.0.0.1:8027/api/v1/musican-sample-search?search=Hanoi" | jq

musican-sample-search-list-SEARCH-last_name:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-search?search=Anh" | jq

musican-sample-search-list-SEARCH-last_name_only:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-search?search=Anh&last_name_only=True" | jq

## ----------------------- filter ---------------------------------

musican-sample-filter-list-FILTER:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-filter?first_name=Phung&last_name=Anh&min_num_stars=0&max_num_stars=200" | jq
		
musican-sample-filter-get-FILTER:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-filter/111?first_name=Le&last_name=Thoa" | jq

## ----------------------- filter search ordering ---------------------------------
musican-sample-search-list-SEARCH-ORDERING-city:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-search?search=Hanoi&ordering=email" | jq

musican-sample-filter-list-FILTER-ORDERING:
	reset && curl "http://127.0.0.1:8027/api/v1/musican-sample-filter?first_name=Phung&last_name=Anh&min_num_stars=0&max_num_stars=500&ordering=email" | jq

## ======================================== prod ================================
prod-up:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

prod-ps:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml ps

prod-down:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down

prod-build:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build --parallel

## ======================================== int ================================
int-up:
	docker-compose -f docker-compose.yml -f docker-compose.int.yml up -d

int-ps:
	docker-compose -f docker-compose.yml -f docker-compose.int.yml ps

int-down:
	docker-compose -f docker-compose.yml -f docker-compose.int.yml down

int-build:
	docker-compose -f docker-compose.yml -f docker-compose.int.yml build --parallel

## ======================================== dev ================================
dev-up:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

dev-ps:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml ps

dev-down:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

dev-build:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build --parallel
# docker-compose build --build-arg  BUILD_ENV=dev my-backend

## ======================================== Deploy development environment with sonarqube ================================
# NOTE: source env_file.sonarqube to pass variable SONARQUBE_POSTGRES_HOSTNAME
# to docker-compose.sonarqube.yml file
dev-sonarqube-up:
	set -a && \
	. sonarqube/env_file.sonarqube && \
	docker-compose --env-file sonarqube/env_file.sonarqube \
		-f docker-compose.yml \
		-f sonarqube/docker-compose.sonarqube.yml up -d
	
dev-sonarqube-ps:
	docker-compose -f docker-compose.yml \
		-f docker-compose.dev.yml \
		-f sonarqube/docker-compose.sonarqube.yml \
		ps

dev-sonarqube-down:
	docker-compose -f docker-compose.yml \
		-f docker-compose.dev.yml \
		-f sonarqube/docker-compose.sonarqube.yml \
		down

dev-sonarqube-build:
	docker-compose -f docker-compose.yml \
		-f docker-compose.dev.yml \
		-f sonarqube/docker-compose.sonarqube.yml \
		build

## ======================================== local ================================
local-up:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml up -d

local-ps:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml ps

local-down:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml down

local-build:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml build --parallel
