# Project Setup

Follow these steps to set up your project environment and run the application.

## 1. Create a Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv venv
```

## 2. Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system:

- **Windows**:
    ```bash
    venv\Scripts\activate
    ```
- **Mac/Linux**:
    ```bash
    source venv/bin/activate
    ```

## 3. Install Dependencies

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## 4. Set Up the Database

Apply migrations to set up your database:

```bash
python manage.py migrate
```

## 5. Run the Server

Start the development server:

```bash
python manage.py runserver
```

## 6. Access the Application

You can now access the application in your browser at:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
