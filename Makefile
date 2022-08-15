super:
	python manage.py createsuperuser

reset:
	rm -rf *.sqlite
	rm -rf base/migrations/
	python manage.py makemigrations
	python manage.py migrate
