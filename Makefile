
.PHONY: up down test docs

up:
	docker compose up -d --build

down:
	docker compose down -v

test:
	pytest -q

docs:
	cd dbt && dbt deps && dbt docs generate
