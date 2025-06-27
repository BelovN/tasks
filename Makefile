IMAGE=tasks:latest
ENV_FILE=.env
VOLUME_PATH=./backend/db

build:
	docker build . -t $(IMAGE)

deploy:
	mkdir -p $(VOLUME_PATH)
	docker compose run --rm app python manage.py migrate

run:
	docker compose up -d

stop:
	docker compose stop

ruff:
	docker compose run --rm app ruff check .

env:
	touch $(ENV_FILE)
	rm $(ENV_FILE)
	echo "DEBUG=True\nSECRET_KEY=super-secret-key3495i036034956034596345" >> $(ENV_FILE)

test:
	docker compose run --rm app pytest