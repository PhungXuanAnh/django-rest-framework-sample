-include Makefile.local

# ============================== git hooks =================================
git-hook-pre-commit__check-pylint: # https://towardsdatascience.com/keep-your-code-clean-using-black-pylint-git-hooks-pre-commit-baf6991f7376
	cp utilities/pre_commit.sh .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
	cat .git/hooks/pre-commit

git-hook-commit-msg__add-branch-name-to-commit: # https://stackoverflow.com/a/11524807/7639845
	cp utilities/commit-msg.sh .git/hooks/commit-msg
	chmod +x .git/hooks/commit-msg
	cat .git/hooks/commit-msg


## ======================================== dev ================================
dev-up:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

dev-ps:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml ps

dev-down:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml down

dev-build:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build --parallel
# docker compose build --build-arg  BUILD_ENV=dev backend


## ======================================== prod ================================
prod-up:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

prod-ps:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml ps

prod-down:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml down

prod-build:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml build --parallel

prod-restart:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml restart

## ======================================== int ================================
int-up:
	docker compose -f docker-compose.yml -f docker-compose.int.yml up -d

int-ps:
	docker compose -f docker-compose.yml -f docker-compose.int.yml ps

int-down:
	docker compose -f docker-compose.yml -f docker-compose.int.yml down

int-build:
	docker compose -f docker-compose.yml -f docker-compose.int.yml build --parallel

