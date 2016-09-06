.PHONY: dev prod

dev:
# rabbitmq-dev exposes ip and port for management
# producer-dev runs producer_test.py -> check ./log/consumer.log \
# for messages send by producer and saved by consumer
	docker-compose -f docker-compose-dev.yml up
prod:
	docker-compose up -d 
