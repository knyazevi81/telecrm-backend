DC = docker compose
ENV = --env-file .env 
DB_COMPOSE = compose/database-compose.yml

.PHONY: db
db:
	${DC} -f ${DB_COMPOSE} ${ENV} up

.PHONY: db-d
db-d:
	${DC} -f ${DB_COMPOSE} ${ENV} up -d

.PHONY: db-down
db-down:
	${DC} -f ${DB_COMPOSE} ${ENV} down
