.PHONY: docker-up docker-down env-docker uv-backend-add uv-frontend-add

env-docker:
	cp .env backend/.env
	cp .env frontend/.env

docker-up: env-docker
	docker-compose up --build

docker-down:
	docker-compose down -v

uv-backend-add:
	cd backend && uv add $(pkg) --active && cd ..

uv-frontend-add:
	cd frontend && uv add $(pkg) --active && cd ..