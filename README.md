Create a virtual environment:python -m venv venv
Activate the virtual environment:venv\Scripts\activate(windows)source venv/bin/activate(Mac)
install:pip install -r requirements.txt
Set up the database:python manage.py migrate
Run the server:python manage.py runserver
Access the application at http://127.0.0.1:8000/
