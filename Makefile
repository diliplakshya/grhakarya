clean:
	docker container prune -f
	docker image prune -f
build:
	docker compose -f docker-compose.yml up -d --build --remove-orphans
start:
	docker compose -f docker-compose.yml start
up:
	docker compose -f docker-compose.yml up -d
destroy:
	docker compose -f docker-compose.yml down -v
stop:
	docker compose -f docker-compose.yml stop
restart:
	docker compose -f docker-compose.yml stop
	docker compose -f docker-compose.yml up -d
down:
	docker compose down
logs:
	docker compose logs