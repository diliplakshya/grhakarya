ifeq ($(BUILD_ENV),testing)
 $(info testing)
 ENV_FILE=configuration/environment/.env.test
 COMPOSE_FILE=docker-compose.test.yaml
else ifeq ($(BUILD_ENV), production)
$(info production)
 ENV_FILE=configuration/environment/.env.prod
 COMPOSE_FILE=docker-compose.yaml
else
 $(info development)
 ENV_FILE=configuration/environment/.env.dev
 COMPOSE_FILE=docker-compose.yaml
endif

greet:
	@echo "Hello $(ENV_FILE)"

all: stop clean up
test: stop clean up runtest

clean:
	docker network prune -f
	docker container prune -f
	docker image prune -f
build:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) build
up:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d --build --remove-orphans
start:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) start
restart:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d
stop:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop
down:
	docker compose down
logs:
	docker compose logs
ps:
	docker ps -a
destroy:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down -v
runtest:
	docker compose -f $(COMPOSE_FILE) exec auth-test pytest /app
