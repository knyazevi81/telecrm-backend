DC = docker compose
ENV = --env-file .env 
DB_COMPOSE = compose/database-compose.yml
APP_COMPOSE = compose/docker-compose.yml

.PHONY: db
db:
	${DC} -f ${DB_COMPOSE} ${ENV} up

.PHONY: db-d
db-d:
	${DC} -f ${DB_COMPOSE} ${ENV} up -d

.PHONY: db-down
db-down:
	${DC} -f ${DB_COMPOSE} ${ENV} down

.PHONY: app
app:
	${DC} -f ${APP_COMPOSE} ${ENV} up

.PHONY: app-d
app-d:
	${DC} -f ${APP_COMPOSE} ${ENV} up -d 

.PHONY: app-b
app-b:
	${DC} -f ${APP_COMPOSE} ${ENV} up --build

.PHONY: app-down
app-down:
	${DC} -f ${APP_COMPOSE} ${ENV} down
