dev:
	uv run python manage.py runserver
migrate:
	uv run python manage.py migrate
model:
	uv run python manage.py makemigrations $(app)