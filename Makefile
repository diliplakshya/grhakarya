clean:
	docker network prune -f
	docker container prune -f
	docker image prune -f
build:
	docker compose -f docker-compose.yaml build
up:
	docker compose -f docker-compose.yaml up -d --build --remove-orphans
start:
	docker compose -f docker-compose.yaml start
restart:
	docker compose -f docker-compose.yaml stop
	docker compose -f docker-compose.yaml up -d
stop:
	docker compose -f docker-compose.yaml stop
down:
	docker compose down
logs:
	docker compose logs
ps:
	docker ps -a
destroy:
	docker compose -f docker-compose.yaml down -v
