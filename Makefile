SHELL = /bin/bash
.PHONY: dev prod clean

prod:
	docker-compose up -d 

dev:
# rabbitmq-dev exposes ip and port for management
# producer-dev runs producer_test.py -> check ./log/consumer.log \
# for messages send by producer and saved by consumer
	docker-compose -f docker-compose-dev.yml up

clean:
	docker-compose down
ifneq ($(shell docker volume ls -f dangling=true -q),)
	docker volume rm $$(docker volume ls -f dangling=true -q)
endif
