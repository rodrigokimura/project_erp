run:
	@pipenv run python manage.py runserver 0.0.0.0:8080

migrations:
	@pipenv run python manage.py makemigrations

migrate:
	@pipenv run python manage.py migrate

reset:
	@rm db.sqlite3
