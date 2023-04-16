THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help runlocal local-linit init stop clear-data

help:
	@echo "local-init - init local without docker with SQLITE3"
	@echo "runlocal - Run local without docker with SQLITE3"
	@echo  "init - use it on first execute. Add  init and migrate method for DB"
	@echo "run - use it second and other times for start the project via Docker "
	@echo "stop - use it for stop the containers"
	@echo "clear-data - delete all containers,volumes and only project image dont touch postgres. BE CAREFUL WITH IT BETTER DO IT BY YOURSELF"

runlocal:
		python runner.py

local-init:
		pip install -r requirements.txt
		flask db init
		flask db migrate
		flask db upgrade

init:
		docker-compose up -d
		docker exec -it digfutsys_web flask db init
		docker exec -it digfutsys_web flask db migrate
		docker exec -it digfutsys_web flask db upgrade
run:
		docker-compose up -d
stop:
		docker stop digfutsys_db
		docker stop digfutsys_web
clear-data:
		docker rm digfutsys_web digfutsys_db
		docker rmi -f digfutsystask_web
		docker volume rm digfutsystask_postgres_data