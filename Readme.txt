Technology - Python Django / sqllite / HTML / CSS / JS

File Structure 

procurement_management/
├── media/
├── manage.py
├── static/
│   ├── css/
│   │	 ├── styles.css
│   ├── js/
│   ├── images/
├── procurement_management/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── procurement/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── admin_dashboard.html
│   │   ├── user_dashboard.html
│   │   ├── create_procurement.html
│   │   ├── view_procurement.html
│   │   ├── continue_step.html
│   │   ├── delete_procurement.html
├── db.sqlite3
├── Readme.txt
└── requirements.txt

Database Migrations

	Run the following commands to create the necessary database tables:
		python manage.py makemigrations
		python manage.py migrate

Create Superuser
	Create a superuser to access the Django admin interface:

	python manage.py createsuperuser

Run the Development Server
	Start the development server:
		python manage.py runserver



